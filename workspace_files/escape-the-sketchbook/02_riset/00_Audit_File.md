# Audit File — Upload Directory & Download Cleanup

> **Tanggal Audit:** 2026-03-04
> **Scope:** `/home/z/my-project/upload/` → klasifikasi file untuk project "Escape the Sketchbook"
> **Prinsip:** Audit saja — TIDAK ada file yang dipindah atau dihapus

---

## 1. Tabel File di `/upload/` — Klasifikasi Lengkap

| # | File | Status | Destination Folder | Notes |
|---|------|--------|--------------------|-------|
| 1 | `Proposal_PA_Muhammad_Dias_Al_Izzat_Proper_3_BAB (1).docx` | **Valid — CRITICAL** | `01_proposal/sources/` | Proposal ORIGINAL Dias. Sumber primer Bab 1. Sangat penting — JANGAN dihapus. |
| 2 | `Proposal_PA_Farchan_Deano_Muhammad_Proper_3_BAB.docx` | **Valid — CRITICAL** | `01_proposal/sources/` | Proposal ORIGINAL Can. Sumber primer Bab 1. Sangat penting — JANGAN dihapus. |
| 3 | `Notes_Notulensi Bimbingan.txt` | **Valid — Already Handled** | `02_riset/` | Sudah disalin ke `02_riset/Notes_Notulensi_Bimbingan.txt` (hash identik). Bisa diabaikan dari upload. |
| 4 | `Merged Context.txt` | **Valid — CRITICAL** | `02_riset/` | Context utama project: histori kronologis arsitektur, reasoning, dan evolusi desain. ~75 KB. Referensi penting untuk konsistensi. |
| 5 | `5322600003 - Harun Budiseto - Proposal PA FIX.pdf` | **Duplicate — Already Handled** | `07_referensi_kating/` | Sudah ada di `07_referensi_kating/harun_proposal_pa_fix.pdf` (hash identik). Tidak perlu disalin lagi. |
| 6 | `5322600024_Muhammad Daffa Husen Nadia_Proposal PA FIX.pdf` | **Duplicate — Already Handled** | `07_referensi_kating/` | Sudah ada di `07_referensi_kating/daffa_proposal_pa_fix.pdf` (hash identik). Tidak perlu disalin lagi. |
| 7 | `pasted_image_1781596442846.png` | **Valid — Already Handled** | `03_diagram/sources/` | Sudah disalin ke `03_diagram/sources/referensi_desain_sistem_teman.png` (hash identik). Tidak perlu disalin lagi. |
| 8 | `pasted_image_1781473587058.png` | **Valid** | `03_diagram/sources/` | Referensi diagram. 804×540, mostly white background — kemungkinan diagram flowchart/arsitektur. Perlu disalin. |
| 9 | `pasted_image_1781473594444.png` | **Valid** | `03_diagram/sources/` | Referensi diagram. 1046×690, dark sidebar — kemungkinan diagram dengan tema gelap / wireframe. Perlu disalin. |
| 10 | `pasted_image_1781489014032.png` | **Valid** | `03_diagram/sources/` | Referensi diagram. 1376×768, warna hijau di tengah — kemungkinan diagram level design / architecture. Perlu disalin. |
| 11 | `Slide 2.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial (beda hash dari versi di zip). |
| 12 | `Slide 4.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial. |
| 13 | `Slide 5.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial. |
| 14 | `Slide 6.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial. |
| 15 | `Slide 7.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial. |
| 16 | `Slide 8.png` | **Valid** | `03_diagram/sources/slides/` | Referensi slide presentasi. Versi CROPPED/partial. |
| 17 | `23 SLIDE NGANGONG.txt` | **Valid** | `04_dokumen/sources/` | Konten lengkap 23 slide presentasi (text format). Berisi narasi, flowchart Mermaid, interaction matrix, wireframe, level flow, arsitektur sistem, sequence diagram, data schema. Sumber penting untuk Brief_PPT. |
| 18 | `ppt fix (2).zip` | **Valid** | `04_dokumen/sources/` | Berisi 24 slide PNG + Form Bimbingan PNG. Versi FULL slide (beda hash dari Slide*.png di upload — kemungkinan versi lebih lengkap/higher-res). |
| 19 | `proposal-formatbehavior (1).pdf` | **Valid** | `07_referensi_kating/` | 7 halaman. "Laporan Format dan Behavior Penulisan Proposal PA" — panduan format penulisan berdasarkan analisis proposal kating. Relevan sebagai referensi format. |
| 20 | `qwen.txt` | **Junk** | — | Chat dump dari sesi Qwen AI. Berisi percakapan awal tentang topik TA dan draf awal. Kontennya sudah tercover di Merged Context.txt dan proposal final. Tidak ada info unik. |
| 21 | `meta.txt` | **Junk** | — | Concatenated raw text dari qwen.txt + Merged Context + Notulensi. Format berantakan, duplikat 100% dari file lain. Tidak ada nilai tambah. |

---

## 2. Ringkasan Status

| Status | Jumlah | File |
|--------|--------|------|
| **Valid — CRITICAL** | 3 | `Proposal_PA_Dias.docx`, `Proposal_PA_Can.docx`, `Merged Context.txt` |
| **Valid — Needs Copy** | 8 | 3 pasted_image_*.png, 6 Slide*.png (kecuali yang sudah handled) |
| **Valid — Already Handled** | 3 | `Notes_Notulensi Bimbingan.txt`, `5322600003...pdf`, `5322600024...pdf`, `pasted_image_1781596442846.png` |
| **Valid — Reference** | 3 | `23 SLIDE NGANGONG.txt`, `ppt fix (2).zip`, `proposal-formatbehavior (1).pdf` |
| **Junk** | 2 | `qwen.txt`, `meta.txt` |

---

## 3. Cleanup di Download Folder

| Lokasi | Masalah | Rekomendasi |
|--------|---------|-------------|
| `/home/z/my-project/download/README.md` | File README lama di root download. Isi hanya "Here are all the generated files." — tidak relevan. | **HAPUS** — Tidak ada gunanya, dan bisa membingungkan. |
| `/home/z/my-project/download/escape-the-sketchbook/README.md` | README project yang masih valid dan ter-update. | **PERTAHANKAN** — Ini README utama project. |
| `/home/z/my-project/download/escape-the-sketchbook/02_riset/` | Tidak ada file duplikat/old version ditemukan. Semua file riset unik dan current. | **OK** — Tidak perlu cleanup. |
| `/home/z/my-project/download/escape-the-sketchbook/01_proposal/can/proposal-can_v1_a4.tex` | Backup versi A4 lama. Ditandai [BACKUP] di README. | **PERTAHANKAN** — Berguna sebagai referensi jika perlu format A4. |
| `/home/z/my-project/download/escape-the-sketchbook/01_proposal/dias/proposal-dias_v1_a4.tex` | Backup versi A4 lama. Ditandai [BACKUP] di README. | **PERTAHANKAN** — Berguna sebagai referensi jika perlu format A4. |

---

## 4. Rekomendasi Aksi

### A. File yang HARUS disalin dari upload ke download (belum ada di download)

| File Sumber | Tujuan | Prioritas |
|-------------|--------|-----------|
| `Proposal_PA_Muhammad_Dias_Al_Izzat_Proper_3_BAB (1).docx` | `01_proposal/sources/Proposal_PA_Dias_Original.docx` | **HIGH** |
| `Proposal_PA_Farchan_Deano_Muhammad_Proper_3_BAB.docx` | `01_proposal/sources/Proposal_PA_Can_Original.docx` | **HIGH** |
| `Merged Context.txt` | `02_riset/Merged_Context.txt` | **HIGH** |
| `pasted_image_1781473587058.png` | `03_diagram/sources/referensi_diagram_1.png` | MEDIUM |
| `pasted_image_1781473594444.png` | `03_diagram/sources/referensi_diagram_2.png` | MEDIUM |
| `pasted_image_1781489014032.png` | `03_diagram/sources/referensi_diagram_3.png` | MEDIUM |
| `Slide 2.png` – `Slide 8.png` (6 file) | `03_diagram/sources/slides/` | MEDIUM |
| `23 SLIDE NGANGONG.txt` | `04_dokumen/sources/23_Slide_Content.txt` | MEDIUM |
| `ppt fix (2).zip` | `04_dokumen/sources/ppt_slides_full.zip` | MEDIUM |
| `proposal-formatbehavior (1).pdf` | `07_referensi_kating/panduan_format_proposal.pdf` | LOW |

### B. File yang TIDAK perlu disalin (sudah ada / duplikat)

- `Notes_Notulensi Bimbingan.txt` → sudah di `02_riset/`
- `5322600003...pdf` → sudah di `07_referensi_kating/`
- `5322600024...pdf` → sudah di `07_referensi_kating/`
- `pasted_image_1781596442846.png` → sudah di `03_diagram/sources/`

### C. File yang BOLEH dihapus dari upload (junk)

- `qwen.txt` — chat dump, tanpa nilai unik
- `meta.txt` — concatenation duplikat, tanpa nilai unik

### D. Cleanup download folder

- **HAPUS** `/home/z/my-project/download/README.md` — hanya berisi placeholder, tidak berguna

---

## 5. Catatan Tambahan

1. **Slide PNG vs ZIP**: Slide PNG yang terpisah di upload (`Slide 2.png`–`Slide 8.png`) berbeda hash dari versi di dalam `ppt fix (2).zip`. Ini berarti keduanya adalah versi berbeda — kemungkinan slide terpisah adalah versi cropped/edited, sedangkan zip berisi versi full export. **Keduanya layak disimpan.**

2. **Pasted Images**: Ketiga pasted image (`1781473587058`, `1781473594444`, `1781489014032`) berbeda dari `1781596442846` yang sudah disalin. Mereka perlu diberi nama deskriptif saat disalin (setelah dilihat kontennya lebih detail).

3. **Merged Context.txt** sangat besar (~75 KB). Meskipun isinya sudah tersebar di berbagai file riset, file ini penting sebagai "single source of truth" untuk histori reasoning dan evolusi desain.

4. **Proposal DOCX**: Kedua file `.docx` adalah dokumen ORIGINAL yang digunakan sebagai dasar proposal LaTeX. Jangan pernah menghapus atau menimpa file ini.

---

*Audit selesai. Tidak ada file yang dipindah atau dihapus selama proses ini.*
