# Escape the Sketchbook — Project Repository

> **Interactive HITL AI Literacy Simulation untuk Siswa SMP Kelas 7-9**
> Final Project D4 TRM — Politeknik Elektronika Negeri Surabaya (PENS)

---

## Tim

| Anggota | NIM | Fokus |
|---------|-----|-------|
| **Farchan Deano Muhammad (Can)** | 31226000xx | Frontend / UI·UX / Kaplay.js / MediaPipe / Narrative / Probe UI / Animation |
| **Muhammad Dias Al-Izzat** | 31226000xx | Backend / CNN MobileNet / TensorFlow.js / Data Logging / K-Means / Dashboard |

---

## Struktur Folder

```
escape-the-sketchbook/
│
├── 01_proposal/          ← Proposal LaTeX (Bab 1-3 + Daftar Pustaka) — FINAL SUBMIT
│   ├── can/              ← Proposal Can
│   │   ├── proposal-can.tex         [UTAMA] Proposal lengkap kating A5
│   │   ├── proposal-can_v1_a4.tex   [BACKUP] Versi A4 lama
│   │   ├── bab2_can.tex             Bab 2 standalone
│   │   └── bab3_can.tex             Bab 3 standalone
│   └── dias/             ← Proposal Dias
│       ├── proposal-dias.tex        [UTAMA] Proposal lengkap kating A5
│       ├── proposal-dias_v1_a4.tex  [BACKUP] Versi A4 lama
│       ├── bab2_dias.tex            Bab 2 standalone
│       └── bab3_dias.tex            Bab 3 standalone
│
├── 02_riset/             ← Riset & referensi akademik (living documents)
│   ├── 00_Referensi_Akademik_Fitur.md  Peta fitur → sitasi akademik
│   ├── 01_Desain_Level.md              Desain 3 level + confidence threshold
│   ├── 02_Desain_Sistem.md             Arsitektur hybrid HITL
│   ├── 03_Riset_Arsitektur.md          Riset model diagram (IPO/Block/DFD)
│   └── 04_Riset_Metode_Penelitian.md   Mixed Methods + Fishbone + SUS + R&D
│
├── 03_diagram/           ← Semua visual & diagram
│   ├── 01_arsitektur_sistem.png        Arsitektur hybrid (browser+server)
│   ├── 02_user_flow.png                Alur pengguna per level
│   ├── 03_level_design.png             Level 1-3 confidence mapping
│   ├── 04_cnn_behavior_mapping.png     CNN behavior → HITL trigger mapping
│   ├── daffa_architecture_diagram.png  Referensi format kating Daffa
│   ├── harun_page39_img0.png           Referensi format kating Harun
│   └── sources/                        HTML editable source untuk diagram
│
├── 04_dokumen/           ← Dokumen generated (PDF, PPT brief)
│   ├── Dokumen_Desain_Sistem_HITL.pdf  Dokumen desain sistem lengkap
│   ├── cover_hitl.pdf                  Cover HITL document
│   ├── body_hitl.pdf                   Body HITL document
│   ├── Brief_PPT.md                    Brief untuk slide presentasi
│   └── sources/                        HTML source
│
├── 05_scripts/           ← Utility scripts (capture, generate, render)
│   ├── capture_level_design.js         Screenshot level design dari HTML
│   ├── capture_cnn_behavior.js         Screenshot CNN mapping dari HTML
│   ├── generate_pdf_body.py            Generate PDF body
│   └── render_flow.py                  Render user flow diagram
│
├── 06_raw/               ← Data mentah (search results, temp files)
│   └── search_*.json                   Hasil riset web (10 file)
│
├── 07_referensi_kating/  ← Contoh proposal senior (format reference)
│   ├── daffa_proposal_pa_fix.pdf       Proposal Daffa (format kating)
│   └── harun_proposal_pa_fix.pdf       Proposal Harun (format kating)
│
└── 08_development/       ← (FUTURE) Kode project implementation
    ├── frontend/          Kaplay.js + MediaPipe + Narrative Engine + UI
    ├── backend/           REST API + SQLite + K-Means Analysis
    └── models/            CNN MobileNet + TensorFlow.js Conversion
```

---

## Konsep Inti Project

### "Controlled Ambiguity"
AI **sengaja tidak sempurna** agar momen HITL (Human-in-the-Loop) terjadi secara natural. Siswa tidak sekadar mengamati AI — mereka **harus mengevaluasi, mengoreksi, dan mengambil keputusan** atas output AI.

### Arsitektur Hybrid
- **Browser-Based Inference** — TensorFlow.js + MobileNet untuk klasifikasi sketsa real-time di browser
- **Server-Side Active Services** — REST API untuk data logging (SQLite) + K-Means clustering analisis pola keputusan

### Desain 3 Level

| Level | Nama | Confidence | Mekanisme |
|-------|------|-----------|-----------|
| L1 | Trust Building | >85% | AI akurat → siswa belajar mempercayai |
| L2 | Ambiguous Choice | 55-70% | AI ragu → siswa harus mengevaluasi |
| L3 | Risk & Override | 35-51% | AI salah → siswa HARUNG override |

### Metodologi Penelitian
- **Mixed Methods** (Kuantitatif + Kualitatif)
- **R&D** (Research & Development)
- **SDLC Waterfall + Prototype**
- **Fishbone Diagram (Ishikawa 6M)** — Teknik analisis data
- **SUS (System Usability Scale)** — Pengujian usability
- **Black-Box Testing** — Pengujian fungsionalitas
- **K-Means Clustering** — Analisis pola keputusan siswa
- **Paired t-test** — Pengujian signifikansi

---

## Roadmap (Fase Project)

| Fase | Status | Deskripsi |
|------|--------|-----------|
| **Riset & Proposal** | ✅ Selesai | Bab 1-3 + Daftar Pustaka terima jadi |
| **Review Proposal** | 🔜 Next | Sidang proposal di PENS |
| **Development** | 📋 Planned | Implementasi kode (`08_development/`) |
| **Testing** | 📋 Planned | SUS, Black-Box, K-Means clustering |
| **Laporan Akhir** | 📋 Planned | Thesis / TA report |

---

## Sumber & Referensi

- **Notulensi Bimbingan** (`/upload/Notes_Notulensi Bimbingan.txt`) — Sumber kebenaran tertinggi
- **Merged Context** (`/upload/Merged Context.txt`) — Evolusi arsitektur & reasoning
- **Proposal Original** (`/upload/Proposal_PA_*.docx`) — Bab 1 original (TIDAK diubah)

---

## Quick Access

| Butuh... | Buka... |
|----------|---------|
| Compile proposal Can | `01_proposal/can/proposal-can.tex` |
| Compile proposal Dias | `01_proposal/dias/proposal-dias.tex` |
| Cek referensi akademik | `02_riset/00_Referensi_Akademik_Fitur.md` |
| Lihat diagram arsitektur | `03_diagram/01_arsitektur_sistem.png` |
| Edit diagram | `03_diagram/sources/*.html` |
| Baca riset metode | `02_riset/04_Riset_Metode_Penelitian.md` |
| Contoh format kating | `07_referensi_kating/` |

---

*Last updated: 2026-06-15*
