# 📝 CHANGELOG.md — Riwayat Perubahan File

---

## [16/06/2026] - Restrukturisasi folder ke sketchbook-universe-ta
- **Edit**: Migrasi seluruh struktur dari `escape-the-sketchbook/` ke `sketchbook-universe-ta/`
- **Alasan**: User request restrukturisasi dengan pemisahan upload/ vs generate/ yang lebih jelas
- **Impact**: Semua file di folder lama masih accessible, folder baru jadi primary

## [16/06/2026] - 7 Subagent task execution (paralel)
- **Edit**: Generated 7 files dari 7 subagent paralel
  - Task A: `00_Audit_File.md` — Audit file upload
  - Task B: `05_Poin_Bu_Hesti.md` — 20 poin keputusan Bu Hesti 16/6/26
  - Task C: `02_Desain_Sistem.md` — Desain sistem global berwarna (v1)
  - Task D: `06_Desain_Momo.md` — 3 opsi maskot Momo + rekomendasi
  - Task E: `api_spec.md` — 5 API endpoints + SQLite schema
  - Task F: `04_Riset_Metode_Penelitian.md` — Fishbone 4-tulang + MIX
  - Task G: `01_Desain_Level.md` — Game design 3 level
- **Alasan**: Big prompt execution dari user
- **Impact**: Raw versions di `08_cache/`, final versions perlu di-generate ke folder baru

## [16/06/2026] - MEMORY.md + CHANGELOG.md dibuat
- **Edit**: Created initial MEMORY.md and CHANGELOG.md
- **Alasan**: Instruksi big prompt Section 2
- **Impact**: Foundation untuk semua file generate selanjutnya

## [16/06/2026] - Big Prompt V2 — 5 content files generated
- **Edit**: Generated 5 final content files via paralel subagents
  - `02_desain_sistem/desain_sistem_global_v2.md` (779 lines) — Diagram global berwarna 🔵🟢⚪
  - `02_desain_sistem/api_data_log_spec.md` (1077 lines) — 6 API endpoints + SQLite
  - `03_maskot/maskot_concept.md` (initial) — Konsep Momo + 3 opsi
  - `04_game_design/game_design_document.md` (717 lines) — GDD 3 level
  - `05_metodologi/mixed_method_integration.md` (1284 lines) — Fishbone + MIX
- **Alasan**: Big prompt terstruktur dari user
- **Impact**: Priority 1 & 2 files complete

## [16/06/2026] - Maskot concept updated — canonical IP story + floating Momo
- **Edit**: `03_maskot/maskot_concept.md` — Major overhaul
  - Replaced generic IP story with canonical 5-babak + epilog from Can
  - Momo = FLOATING, NO legs, NO wings (user: "dia bisa terbang")
  - Color changed from coral (#FF6B6B) → green highlighter (#00E676) matching "tinta highlighter hijau"
  - All ASCII art updated to show floating + shadow
  - All behavior states rewritten for floating (bob, drift, spin in air)
  - Added Merged Context analysis to `08_cache/merged_context_analysis.md`
- **Alasan**: User provided canonical IP story + design feedback
- **Impact**: maskot_concept.md now 1630 lines (was 1295), game_design_document.md may need consistency check

## [16/06/2026] - Quick Draw Category Analysis v3.0 generated
- **Edit**: Created `04_game_design/quickdraw_category_analysis.md` (1044 lines, 63 KB)
- **Alasan**: Bigprompt v3.0 dari user Can — analisis 345 kategori Quick Draw Google
- **Initial Output**: 317/345 diklasifikasi (TIER 1: 146, TIER 2: 116, TIER 3: 55). Golden Set 148 kategori.
- **Impact**: File siap review oleh Can & Dias

## [16/06/2026] - 🔁 RSI Iteration #1 — Over-Inclusiveness Bias Fix
- **Trigger**: User angry feedback — Quick Draw analysis terlalu over-inclusive:
  - "animal gausa dimasukin anjng kenapa malah jadi lu recommend dah" → 40+ hewan di TIER 1 (cat, dog, elephant, lion, tiger, bear, horse, dll)
  - "yang ga terlalu sulit dan ga terlalu gampang makanya gw minta line circle dihapus" → masih bahas line/circle/square di TIER 3 Banned
  - "yang ga terlalu sulit juga bukan cuma aircraft" → masih include aircraft carrier & item kompleks
  - "jancok malah lama2in game cok" → hewan bikin game lambat (stroke complexity + confusion matrix)
  - "riset ulang dan pahami apa maksud gw dengan 'Recursive Self-Improvement'" → user mau gw terapkan RSI ke workflow
- **Root Cause Analysis**:
  - Bias "comprehensive coverage" — aku masukkan semua yang familiar tanpa filter gameplay pace
  - Lupa kalau game ini **fast-paced drawing** (bukan art class) — butuh medium difficulty only
  - Hewan punya stroke complexity tinggi + confusion matrix antar hewan (cat↔dog↔lion↔tiger↔bear)
- **Rule Added (MEMORY.md Section 9 — RSI Rules)**:
  - **RSI-1: SWEET SPOT FILTER** — Kurasi kategori WAJIB filter ke medium difficulty only
  - Geometric primitives (line, circle, square, triangle, zigzag, squiggle) → HAPUS TOTAL dari analisis
  - Semua hewan → BANNED (stroke complexity + confusion matrix)
  - Landmark/kompleks ekstrem (Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier) → BANNED
  - Single-stroke items (smiley, dot, eye) → BANNED
  - FOKUS: Everyday objects + simple food + nature + basic vehicles (stroke 4-15)
- **Action**: Revisi `quickdraw_category_analysis.md`:
  - Hapus SEMUA hewan dari TIER 1 & Golden Set
  - Hapus mention line/circle/square (cuma 1 line exclusion note)
  - Hapus aircraft carrier, Eiffel Tower, Mona Lisa dari TIER 2 conditional
  - Rebuild Golden Set dengan medium-difficulty only
- **Impact**: MEMORY.md + CHANGELOG.md updated dengan RSI rule. Revisi markdown akan regenerate.

---

## Template Entry Baru
```
## [DD/MM/YYYY] - [Deskripsi Singkat]
- **Edit**: File apa yang diubah
- **Alasan**: Kenapa diubah (referensi notulensi/user request)
- **Impact**: File lain yang terpengaruh
```
