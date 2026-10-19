# Every uv call goes through the vendored helper, which cleans the environment,
# uses the global uv cache, runs offline first and goes online at most once. See
# https://github.com/leynos/shared-actions/tree/main/uv_gate for the contract.
UV_GATE ?= python3 scripts/uv_gate.py
UV ?= uv
# The helper finds uv on PATH, so a caller's UV=/path/to/uv is honoured by putting
# that uv's directory first on PATH for every recipe.
export PATH := $(if $(findstring /,$(UV)),$(patsubst %/,%,$(dir $(UV))):)$(PATH)
.DEFAULT_GOAL := check

# A pipeline reports only its last command's status by default, so a failing
# `git ls-files` would be masked by a successful `xargs`. pipefail propagates it.
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c

MD_GLOB := **/*.md
PYTHON_SOURCES := tests

# The skill manifest contract. SKILL_DIRS defaults to every shipped skill and
# can be overridden to check one skill or a test fixture, for example
# `make skill-manifest-check SKILL_DIRS=skills/typescript-router/`.
SKILL_DIRS ?= $(sort $(dir $(wildcard skills/*/SKILL.md)))
SKILLS_REF := $(UV_GATE) run --group dev -- skills-ref
YAMLLINT := $(UV_GATE) run --group dev -- yamllint
RUFF := $(UV_GATE) run --group dev -- ruff
SKILL_YAMLLINT_CONFIG := {extends: default, rules: {line-length: disable}}

# `make fmt` and `make check-fmt` call mdtablefix directly. `--git` selects the
# Markdown files Git tracks and `--include-untracked` adds the untracked files
# Git does not ignore, so a new document is formatted before it is staged.
# Both modes need mdtablefix 0.6.1 or later.
MDLINT ?= markdownlint-cli2
MDTABLEFIX ?= mdtablefix
MDTABLEFIX_SELECT = --git --include-untracked
MDTABLEFIX_RULES = --wrap --renumber --breaks --ellipsis --fences

# The TypeScript example gate. Positive examples must type-check and every
# diagnostics fixture must raise exactly the errors its `@ts-expect-error`
# markers claim, under the TypeScript release pinned in examples/package.json.
BUN ?= bun
EXAMPLES := examples

.PHONY: prepare help fmt markdownlint nixie lint check check-fmt typecheck test \
	examples examples-install skill-frontmatter-lint skill-manifest-validate \
	skill-manifest-check

prepare: ## Install the locked development environment, offline first
	$(UV_GATE) prepare --group dev

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*## "}; {printf "  %-24s %s\n", $$1, $$2}'

fmt: prepare ## Format Python, reflow Markdown tables, and apply markdownlint fixes
	$(RUFF) format $(PYTHON_SOURCES)
	$(MDTABLEFIX) --in-place $(MDTABLEFIX_SELECT) $(MDTABLEFIX_RULES)
	$(MDLINT) --fix "$(MD_GLOB)"

markdownlint: ## Lint every Markdown file
	$(MDLINT) '$(MD_GLOB)'

nixie: ## Validate every Mermaid diagram
	nixie .

lint: markdownlint nixie skill-manifest-check ## Run all lint gates
	$(RUFF) check $(PYTHON_SOURCES)

# `set -e` matters: without it the loop exits with the status of its final
# iteration, so a conformant trailing skill would mask a malformed earlier one.
skill-frontmatter-lint: prepare ## Lint each skill manifest's YAML frontmatter
	@set -euo pipefail; for skill_dir in $(SKILL_DIRS); do \
		skill_file="$${skill_dir%/}/SKILL.md"; \
		echo "yamllint $$skill_file frontmatter"; \
		awk 'NR == 1 { if ($$0 != "---") exit 1; print; next } $$0 == "---" { found = 1; print; exit } { print } END { if (!found) exit 1 }' "$$skill_file" \
		  | $(YAMLLINT) -d '$(SKILL_YAMLLINT_CONFIG)' -; \
	done

skill-manifest-validate: prepare ## Validate each skill against the Agent Skills schema
	@set -eu; for skill_dir in $(SKILL_DIRS); do \
		echo "skills-ref validate $$skill_dir"; \
		$(SKILLS_REF) validate "$$skill_dir"; \
	done

skill-manifest-check: skill-frontmatter-lint skill-manifest-validate ## Verify every skill manifest

check-fmt: prepare markdownlint ## Formatting gate
	$(RUFF) format --check $(PYTHON_SOURCES)
	$(MDTABLEFIX) --check $(MDTABLEFIX_SELECT) $(MDTABLEFIX_RULES)

typecheck: prepare ## Type-check the test suite
	$(UV_GATE) run --group dev -- mypy

examples-install: ## Install the pinned TypeScript used by the example gate
	$(BUN) install --frozen-lockfile --cwd $(EXAMPLES)

examples: examples-install ## Type-check the positive examples and diagnostics fixtures
	cd $(EXAMPLES) && $(BUN) run check

test: prepare ## Run the test suite
	$(UV_GATE) run --group dev -- pytest

check: check-fmt lint typecheck examples test ## Run every commit gate
