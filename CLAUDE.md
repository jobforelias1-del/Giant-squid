# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) and other AI assistants when working with code in this repository.

## Repository Overview

**Giant-squid** is a research repository about giant squid (per the README: "Research Giant Squid"). It is currently at the very beginning of its life: the only content is `README.md`, and there is no source code, build system, test suite, or CI configuration yet.

## Current State

```
Giant-squid/
└── README.md   # Project name and one-line description
```

There are **no** package manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.), **no** lint/format/test commands, and **no** CI workflows. Do not assume or invent build or test commands — none exist. If asked to run tests or a build, state that the repository has no tooling configured yet and offer to set it up.

## Development Workflow

- **Default branch:** `main`.
- **Feature branches:** work happens on feature branches (e.g. `claude/<topic>-<suffix>`), which are pushed and merged into `main` via pull requests.
- **Commits:** use clear, descriptive commit messages. The history is currently a single "Initial commit".

## Guidance for AI Assistants

1. **Do not fabricate structure.** This file describes an empty repository on purpose. Never reference directories, commands, or conventions that do not exist in the working tree.
2. **Keep this file in sync.** When you add meaningful structure — a language/toolchain, source directories, tests, CI — update this CLAUDE.md in the same change so it reflects the real state of the repository:
   - Add a "Common Commands" section (install, build, test, lint) once tooling exists.
   - Replace the "Current State" tree with the actual layout.
   - Document any architecture decisions as they are made.
3. **Ask before choosing a stack.** Because nothing is scaffolded, decisions like programming language, framework, and repository layout belong to the repository owner. Propose options rather than unilaterally committing to a stack, unless the request already specifies one.
4. **Research content:** if the repository accumulates research material (notes, datasets, references about giant squid), prefer an organized layout such as `notes/`, `data/`, and `references/`, and document whatever layout is adopted here.
