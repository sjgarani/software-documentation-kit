# Repository Guidelines

## Project Structure & Documentation

This repository is a documentation starter kit; its content is maintained as Markdown rather than application source code. `README.md` explains how to adopt the kit. The `docs/` directory contains its navigation guide and reusable materials: `adr/` for architectural decisions, `specs/` for change requirements, `runbooks/` for operational procedures, and `guides/` for recurring practices. Keep related documents together and link to them with relative paths.

## Development Workflow

There is no build, package manager, or automated test command configured. Preview Markdown in a renderer when reviewing layout, and verify changed relative links and template instructions by reading them in context. Keep examples copyable and ensure referenced paths and filenames match the repository.

## Writing Style & Naming

Write in Portuguese for project documentation, matching the existing README and templates. Use Markdown headings, concise direct language, short examples, and ISO dates (`AAAA-MM-DD`). Prefer one source of truth with links instead of duplicated guidance. Name Specs `AAAA-MM-DD-assunto.md`, ADRs `NNNN-titulo-curto.md`, and give runbooks and guides descriptive lowercase filenames with hyphens. Preserve template fields and section order when improving a template unless the document’s purpose requires a change.

## Documentation Validation

Review every changed document for clear ownership, state, and related links where relevant. Specs should have observable acceptance criteria; ADRs should explain context, alternatives, decision, and consequences; runbooks should give verifiable steps and recovery guidance. Do not add credentials, personal data, or restricted information. Update `README.md` or `docs/README.md` when the structure or getting-started workflow changes.

## Commits & Pull Requests

The available checkout has no Git history to establish a repository-specific commit convention. Use short imperative commit subjects, such as `Document ADR naming guidance`. Pull requests should summarize the documentation change and its reason, link related issues or documents, and note any review or validation performed. Include rendered screenshots only when a visual change is difficult to assess from the Markdown diff.
