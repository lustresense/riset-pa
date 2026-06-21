# MEMORY.md - Operational Context

This file is the required first-read context for any AI agent or teammate working on
Sketchbook Universe.

## Current Project

- Project name: Sketchbook Universe
- Research theme: Controlled Ambiguity in AI Sketching
- Core concept: Human-in-the-Loop (HITL) sketching where AI uncertainty is designed
  as part of the learning experience.
- Audience: junior high school students, grades 7-9.
- Institution context: PA / Sidang preparation for PENS D4 TRM.

## Team

| Member | Scope | Notes |
| --- | --- | --- |
| Farchan Deano Muhammad (Can) | Frontend, UI/UX, HITL, gameplay, mascot | Blue scope |
| Muhammad Dias Al-Izzat | Backend, AI model, API, logging, analytics | Green scope |

## Active Repository Structure

The repository now uses a 4-zone professional architecture:

```text
/
|-- 00_RESEARCH/
|   |-- meetings/
|   |-- literature/
|   |-- data_raw/
|   |-- experiments/
|   `-- ideation/
|-- 01_CORE_SYSTEM/
|   |-- extension/
|   |-- web-client/
|   |-- backend/
|   |-- shared/
|   `-- tests/
|-- 02_ARTIFACTS/
|   |-- proposal/
|   |-- reports/
|   |-- presentations/
|   |-- diagrams/
|   `-- demo/
|-- 03_DOCS/
|   |-- technical/
|   |-- user-manual/
|   `-- policy/
`-- scripts/
```

## Zone Rules

- `00_RESEARCH/`: raw discussion, literature, data dumps, experiments, and early ideas.
- `01_CORE_SYSTEM/`: production application code only. It is intentionally ready for
  Chrome extension, web client, backend, shared utilities, and tests.
- `02_ARTIFACTS/`: final or presentation-ready outputs: proposal, reports, slides,
  diagrams, and demo media.
- `03_DOCS/`: technical docs, user manuals, and policy/consent documents.
- `scripts/`: automation utilities for rendering, capture, build, deploy, or tests.

If a file is ambiguous, place it in `00_RESEARCH/ideation/` first. Promote it to
`02_ARTIFACTS/` only when it is explicitly final or presentation-ready.

## Current Research Decisions

- Controlled Ambiguity remains the main research mechanism.
- HITL is the interaction layer: users evaluate, correct, and override AI predictions.
- System architecture is hybrid: browser-side inference plus server-side logging and
  analytics.
- Login and history are required because the research needs user/session data.
- The agent must keep `README.md`, `MEMORY.md`, and `CHANGELOG.md` aligned with any
  major structural or research decision.

## Recursive Self-Improvement Rule

This repo uses a lightweight Recursive Self-Improvement workflow:

1. Read `.agent_protocol.md`.
2. Read this `MEMORY.md`.
3. Execute the task.
4. Update `MEMORY.md` and `CHANGELOG.md` if the task changes repository state,
   research direction, or operating rules.

## Latest Structural Decision

- Date: 2026-06-21
- Decision: Adopt the 4-zone architecture for PA/Sidang readiness.
- Impact:
  - Research materials are centralized under `00_RESEARCH/`.
  - Application code has dedicated placeholders under `01_CORE_SYSTEM/`.
  - Final artifacts are separated under `02_ARTIFACTS/`.
  - Technical/user/policy documentation is centralized under `03_DOCS/`.
  - Root directory is reserved for project-level files only.
