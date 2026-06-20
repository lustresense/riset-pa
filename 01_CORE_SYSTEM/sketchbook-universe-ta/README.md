# Sketchbook Universe — Project Repository

> **Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9**
> Tugas Akhir D4 TRM — Politeknik Elektronika Negeri Surabaya (PENS)

---

## Tim

| Anggota | Fokus | Warna |
|---------|-------|-------|
| **Can (Farchan Deano M.)** | Frontend / Kaplay.js / MediaPipe / Maskot Momo / Gameplay / UI/UX | 🔵 BIRU |
| **Dias (Muhammad Dias Al-I.)** | Backend / CNN MobileNet / TensorFlow.js / API / DB / K-Means | 🟢 HIJAU |

---

## Struktur Folder

```
sketchbook-universe-ta/
│
├── upload/                    ← FILE DARI USER — JANGAN DI-EDIT
│   ├── notulensi_bu_hesti_15jun26.md     Transkrip bimbingan (MASTER REFERENCE)
│   ├── contoh_daffa.pdf                   Proposal senior (format ref)
│   ├── contoh_harun.pdf                   Proposal senior (format ref)
│   └── reference_images/                  Gambar inspirasi
│       └── architecture_referensi.png     Diagram referensi teman
│
├── generate/                  ← HASIL KERJA Z AI — BOLEH DI-UPDATE
│   │
│   ├── MEMORY.md              ⚡ INGATAN AGENT — BACA DULU!
│   ├── CHANGELOG.md           Riwayat perubahan file
│   │
│   ├── 01_proposal/           Dokumen proposal LaTeX
│   │   ├── can/               Bagian Can (Frontend/HITL)
│   │   │   ├── proposal-can.tex
│   │   │   ├── bab2_can.tex
│   │   │   └── bab3_can.tex
│   │   └── dias/              Bagian Dias (Backend/CNN)
│   │       ├── proposal-dias.tex
│   │       ├── bab2_dias.tex
│   │       └── bab3_dias.tex
│   │
│   ├── 02_desain_sistem/      ⭐ DESAIN SISTEM GLOBAL
│   │   ├── desain_sistem_global_v2.md     Diagram global berwarna (779 lines)
│   │   └── api_data_log_spec.md           API endpoint spec (1077 lines)
│   │
│   ├── 03_maskot/             ⭐ RISET MASKOT MOMO
│   │   └── maskot_concept.md              Konsep visual + behavior (1295 lines)
│   │
│   ├── 04_game_design/        ⭐ GAME DESIGN
│   │   └── game_design_document.md        GDD lengkap (717 lines)
│   │
│   ├── 05_metodologi/         ⭐ FISHBONE + METOPEN
│   │   └── mixed_method_integration.md    MIX methodology (1284 lines)
│   │
│   ├── 06_diagram/            Visual outputs (PNG + HTML sources)
│   ├── 07_scripts/            Utility scripts
│   └── 08_cache/              Temporary/raw files (boleh dihapus)
│
└── README.md                  ← You are here
```

---

## Quick Access

| Butuh... | Buka... |
|----------|---------|
| Baca ingatan project | `generate/MEMORY.md` |
| Lihat desain sistem baru | `generate/02_desain_sistem/desain_sistem_global_v2.md` |
| Cek API specification | `generate/02_desain_sistem/api_data_log_spec.md` |
| Baca konsep maskot Momo | `generate/03_maskot/maskot_concept.md` |
| Baca game design | `generate/04_game_design/game_design_document.md` |
| Baca metodologi + fishbone | `generate/05_metodologi/mixed_method_integration.md` |
| Baca notulensi Bu Hesti | `upload/notulensi_bu_hesti_15jun26.md` |
| Compile proposal Can | `generate/01_proposal/can/proposal-can.tex` |
| Compile proposal Dias | `generate/01_proposal/dias/proposal-dias.tex` |

---

## File Generation Summary

| File | Lines | Priority | Status |
|------|-------|----------|--------|
| MEMORY.md | 71 | P1 | ✅ |
| CHANGELOG.md | 35 | P1 | ✅ |
| desain_sistem_global_v2.md | 779 | P1 | ✅ |
| api_data_log_spec.md | 1077 | P1 | ✅ |
| maskot_concept.md | 1295 | P2 | ✅ |
| game_design_document.md | 717 | P2 | ✅ |
| mixed_method_integration.md | 1284 | P2 | ✅ |
| **TOTAL** | **5258** | | |

---

## Key Decisions (from Bu Hesti 16/6/26)

1. Desain sistem = SATU global diagram + warna scope (BIRU/HIJAU)
2. Login WAJIB (changed from session-only)
3. 3 level saja, tanpa decorative
4. Level 1: Top-1 only, Level 2: Top-3 + confidence, Level 3: AI overconfident wrong
5. Use case = aktor + aktivitas (bukan flow)
6. Metodologi MIX + Fishbone wajib ada
7. Data log = matriks + kesimpulan kalimat
8. Maskot = text bubble saja, tanpa NLP/suara

---

*Last updated: 2026-06-16*
