# Gaussian Explorer

A Python project developed with an AI-assisted, approval-gated SDLC workflow.

## Development approach

This repository follows an AI-assisted, documentation-driven software development lifecycle. AI may support analysis, planning, implementation, testing, and documentation, but designated artifacts require human approval before work proceeds to the next stage.

Start with [`sdlc_docs/00_project_context/project_context.md`](sdlc_docs/00_project_context/project_context.md) and consult [`WORKFLOW.md`](WORKFLOW.md) for the complete sequence.

## Setup

```bash
uv sync --all-groups
uv run pre-commit install
```

## Quality checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

## Documentation

```bash
uv run mkdocs serve
```

## Project metadata

- **Type:** application
- **Python:** 3.12+
- **Author:** Your Name <name@example.org>
- **License:** MIT
