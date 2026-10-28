# Spec: Change title

- **Status:** Draft | In Review | Approved | In Progress | Completed | Cancelled
- **Owner:** name or team
- **Date:** YYYY-MM-DD
- **Related:** ADRs, issues, pull requests, metrics, or documents

## Summary

In a few sentences, what is changing and why?

## Problem and context

Who experiences the problem? How does it appear today? Include relevant evidence, constraints, and background.

## Goals

- ...

## Out of scope

- ...

## Requirements and acceptance criteria

Use observable, verifiable criteria. Identify relevant functional and non-functional requirements.

- [ ] Given ..., when ..., then ...

## Proposal

Describe the expected behavior and the experience for users or systems. Include examples or flows where useful.

## Technical design

Describe affected components, interfaces, data, dependencies, and relevant decisions. Record lasting decisions in separate ADRs and link them here.

## Security, privacy, and accessibility

Record relevant impacts and requirements. If there is no material impact, briefly explain why.

## Migration and compatibility

How will existing customers, data, and integrations be affected? Describe migration, compatibility, and rollback.

## Observability and operations

What logs, metrics, alerts, or procedures are needed? How will we know the change is working?

## Delivery plan

Describe phases, feature flags, gradual rollout, communication, and rollback plan where applicable.

## Validation

How will the acceptance criteria be demonstrated? List manual or automated checks, metrics, or experiments.

## Open questions

- [ ] Question — owner — deadline or condition for resolution

Use the transitions defined in [ADR 0001](../adr/0001-documentation-workflow-and-agent-rules.md). The `tools/docflow.py` utility validates and updates the status field.
Follow the [Spec workflow](spec-workflow.md) when reviewing or changing a Spec status.

## History

| Date | Change | Owner |
|---|---|---|
| YYYY-MM-DD | Initial draft | Name |
