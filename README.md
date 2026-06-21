# Sketchbook Universe: Controlled Ambiguity in AI Sketching

![Research Status](https://img.shields.io/badge/status-PA%20Research-blue)
![Version](https://img.shields.io/badge/version-2.0.0-green)
![Architecture](https://img.shields.io/badge/repo-4--Zone%20Architecture-lightgrey)

## Tentang Project

Sketchbook Universe adalah riset interaktif tentang literasi AI untuk siswa SMP.
Konsep utamanya adalah Controlled Ambiguity: AI sengaja dibuat memiliki momen
ketidakpastian agar siswa perlu mengevaluasi, mengoreksi, dan mengambil keputusan.

Lapisan Human-in-the-Loop (HITL) menjadi inti pengalaman belajar. Siswa tidak hanya
melihat output AI, tetapi juga berlatih memahami kapan AI bisa dipercaya, kapan AI
ragu, dan kapan output AI perlu dikoreksi.

## Struktur Repository

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
|-- scripts/
|-- README.md
|-- MEMORY.md
|-- CHANGELOG.md
|-- .agent_protocol.md
|-- .gitignore
`-- package.json (if added later)
```

## Quick Start

```bash
git clone https://github.com/lustresense/riset-pa.git
cd riset-pa
```

Read the operating context before working:

```bash
cat MEMORY.md
cat .agent_protocol.md
```

Application code is prepared under `01_CORE_SYSTEM/`. When a package is added, run
the relevant install and development commands from the matching app folder, for
example:

```bash
cd 01_CORE_SYSTEM/web-client
npm install
npm run dev
```

Automation scripts are stored in `scripts/`.

## Tim

| Anggota | Fokus |
| --- | --- |
| Farchan Deano Muhammad (Can) | Frontend, UI/UX, HITL, gameplay, mascot |
| Muhammad Dias Al-Izzat | Backend, AI model, API, data logging, analytics |

## Konteks Mendalam

Read [`MEMORY.md`](MEMORY.md) for current decisions, repository rules, and the
latest operational context.
