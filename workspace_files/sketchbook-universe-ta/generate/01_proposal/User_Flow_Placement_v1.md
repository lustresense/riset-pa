# User Flow Placement — Section v1 (Post-Pivot 16/6/26)

> **Project:** Sketchbook Universe — TA Can (Frontend)
> **Task ID:** usecase-superadmin-v1
> **Tanggal:** 16 Juni 2026
> **Status:** Pre-LaTeX, siap di-include ke Bab 3 Can (section 3.2.2 Alur Pengguna)
> **Catatan Khusus:** Penulis (Can) akan melengkapi diagram alur pengguna sendiri pada tahap implementasi. Dokumen ini hanya menyediakan **placement + kerangka textual + sequence diagram key flows**.

---

## 1. Catatan Penulis (Bersifat Sementara)

> **Alur pengguna akan dilengkapi oleh penulis (Can) pada tahap implementasi.** Dokumen ini menyediakan kerangka alur secara textual, placeholder untuk diagram alur pengguna, dan tiga sequence diagram Mermaid untuk key flows (Login, Override + Top-6 Check, Data Logging). Diagram alur pengguna lengkap dengan visual flowchart akan diproduksi oleh penulis menggunakan tool seperti Figma atau draw.io setelah playtest awal dilakukan.

---

## 2. Kerangka Alur Pengguna (Textual)

Alur pengguna Sketchbook Universe dirancang secara **linear** dengan sembilan fase utama. Linearitas dipilih berdasarkan prinsip \textit{Child--Computer Interaction} (CCI)~[2] yang menekankan bahwa interaksi untuk anak usia 12--15 tahun harus sederhana dan dapat diprediksi. Alur linear juga memastikan progresi scaffolding~[6][7] terjadi secara terprediksi: siswa selalu mengalami trust building sebelum ambiguitas, dan ambiguitas sebelum situasi yang membutuhkan override.

Sembilan fase alur pengguna:

1. **Login** — Siswa memilih class\_id dari dropdown lalu menginput nomor absen. Momo menyambut dengan text bubble "Hai, siswa nomor X!". Tidak ada password (post-pivot 16/6/26 PIVOT \#1).
2. **Onboarding** — Splash screen + perkenalan Momo + tutorial general (1 layar overview aturan objek Solid/Danger, bukan step-by-step per mekanik — sesuai arahan Bu Hesti).
3. **Level Select** — Siswa memilih level yang akan dimainkan (Level 1 unlocked by default; Level 2 unlocked setelah Level 1 selesai; Level 3 unlocked setelah Level 2 selesai).
4. **Tutorial (per level)** — Brief singkat level: objective, batasan (erase allowed/tidak, drawing attempts), Momo emotion baseline level tersebut.
5. **Main Gameplay** — Siswa menggambar objek di canvas dengan tombol UI resize/rotate (post-pivot Decision \#4) dan timer count-up (post-pivot Decision \#3).
6. **Probe UI** — Saat siswa selesai menggambar, gameplay \textit{pause} dan Probe UI muncul: menampilkan Top-3 prediksi AI + confidence score + Momo reaction. Siswa memilih Accept / Correct (Level 2+) / Override (Level 2+, Level 3 satu-satunya opsi koreksi).
7. **Top-6 Verification (jika Override)** — Backend memeriksa apakah label override ada di Top-6 prediksi (rahasia). Jika ADA → AUTO-ACCEPT, objek masuk game world. Jika TIDAK ADA → sistem minta re-draw (post-pivot PIVOT \#2).
8. **Result & Feedback** — Objek masuk game world dengan perilaku sesuai mapping (Solid/Danger). Stickman bergerak. Momo menampilkan state emosi sesuai outcome (HAPPY jika sukses, CONFUSED jika gagal). Tidak ada skor/leaderboard --- konsekuensi gameplay adalah feedback (sesuai prinsip \textit{Narrative as Feedback}).
9. **Next Level / Retry** — Jika sukses, siswa dapat lanjut ke level berikutnya atau replay. Jika gagal, siswa dapat retry level yang sama. Level Summary di akhir setiap level menampilkan refleksi Momo tentang keputusan yang diambil siswa selama level.

```
Login → Onboarding → Level Select → Tutorial → Main Gameplay
                                              ↓
                                              Probe UI
                                              ↓
                                       [Override?]
                                        ├── No → Result & Feedback → Next Level
                                        └── Yes → Top-6 Verification
                                                  ├── Match → Result & Feedback (sukses)
                                                  └── No Match → Redraw → Main Gameplay
```

---

## 3. Placeholder untuk User Flow Diagram

Diagram alur pengguna lengkap akan diproduksi oleh penulis pada tahap implementasi. Placeholder untuk diagram ditampilkan di bawah, dengan caption yang sudah disiapkan untuk LaTeX.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Alur Pengguna Sistem Sketchbook Universe --- 9 Fase Linear (Login, Onboarding, Level Select, Tutorial, Main Gameplay, Probe UI, Top-6 Verification, Result \& Feedback, Next Level)}
    \label{fig:alur-pengguna-global}
\end{figure}

> **Catatan untuk penulis:** Diagram alur pengguna akan dibuat oleh Can menggunakan Figma/draw.io setelah playtest awal. Shape flowchart mengikuti arahan Bu Hesti: Input=parallelogram, Proses=rectangle, Decision=diamond. Font diperbesar. Tidak ada warna dekoratif (hanya hitam-putih atau maksimal 2 warna untuk membedakan scope).

---

## 4. Sequence Diagrams Mermaid (POLOSAN) — Key Flows

Tiga sequence diagram berikut merinci key flows sistem yang menjadi titik kritis interaksi aktor-frontend-backend-database. Diagram menggunakan Mermaid \texttt{sequenceDiagram} tanpa styling (POLOSAN, no classDef, no fill color).

### 4.1 Login Flow (Siswa → Frontend → Backend → Database)

```mermaid
sequenceDiagram
    actor Siswa
    participant FE as Frontend (Kaplay.js)
    participant BE as Backend API
    participant DB as Database

    Note over Siswa,DB: FASE 1 LOGIN (Post-Pivot 16/6/26: Nomor Absen, no password)

    Siswa->>FE: Pilih class_id (dropdown)
    FE->>BE: GET /classes
    BE->>DB: SELECT class_id, label FROM classes WHERE is_active=true
    DB-->>BE: Daftar kelas aktif
    BE-->>FE: 200 OK JSON daftar kelas
    FE-->>Siswa: Tampilkan dropdown kelas

    Siswa->>FE: Input nomor_absen (numerik 1-99)
    FE->>FE: Validasi format (integer, range 1-99)
    FE->>BE: POST /auth/login {class_id, nomor_absen}

    BE->>DB: SELECT * FROM students WHERE class_id=? AND nomor_absen=? AND is_active=true
    DB-->>BE: Student record (or null)

    alt Student valid (record ditemukan)
        BE->>BE: Generate session_token (JWT, payload={student_id, class_id, school_id}, expiry=4 jam)
        BE->>DB: INSERT INTO sessions (student_id, token, issued_at, expires_at)
        BE-->>FE: 200 OK {session_token, student_id, class_label}
        FE->>FE: Store session_token di localStorage
        FE-->>Siswa: Momo HAPPY: "Hai, siswa nomor X! Siap main?"
        FE-->>Siswa: Redirect ke Onboarding (FASE 2)
    else Student tidak ditemukan
        BE-->>FE: 404 Not Found {error: student_not_found}
        FE-->>Siswa: Momo CONFUSED: "Nomor absen belum terdaftar di kelas ini."
        FE-->>Siswa: Tetap di layar login, input nomor_absen di-reset
    end
```

### 4.2 Override + Top-6 Check Flow (Post-Pivot PIVOT #2)

```mermaid
sequenceDiagram
    actor Siswa
    participant FE as Frontend (Probe UI)
    participant CNN as CNN Model (TF.js, client-side)
    participant BE as Backend API
    participant DB as Database

    Note over Siswa,DB: FASE 6 PROBE UI + FASE 7 TOP-6 VERIFICATION

    Siswa->>FE: Selesai menggambar objek di canvas (FASE 5 selesai)
    FE->>FE: canvas.toBlob() → preprocess (resize 28x28, normalize, tensor)
    FE->>CNN: tensor input
    CNN-->>FE: Top-6 predictions + confidence scores (client-side inference)
    Note over FE: Tampilkan Top-3 saja ke siswa (transparent, sesuai XAI prinsip [3])<br/>Top-4 s/d Top-6 disimpan internal (rahasia, untuk anti-cheat)

    FE-->>Siswa: Probe UI muncul: Top-3 predictions + confidence bar + Momo reaction (state sesuai confidence)

    Siswa->>FE: Klik tombol Override (Level 2+ atau Level 3 satu-satunya opsi)
    FE-->>Siswa: Form input label sendiri (text, max 32 char)
    Siswa->>FE: Submit label (mis: "tangga")
    FE->>FE: Validasi label (non-empty, max 32 char, no special char)

    FE->>BE: POST /probe/override {session_token, drawing_blob_url, top6, override_label, level, probe_id, time_spent_ms}
    BE->>BE: Validate session_token + extract student_id
    BE->>BE: Top-6 Check: case-insensitive match override_label vs top6[].label

    alt Label ADA di Top-6 (AUTO-ACCEPT)
        BE->>DB: INSERT INTO interaction_logs (student_id, class_id, school_id, level, probe_id, event_type=override, decision_type=override, override_label, top6_match=true, time_spent_ms, confidence_top1, confidence_top6, timestamp)
        DB-->>BE: ACK insert success
        BE-->>FE: 200 OK {accepted: true, reason: top6_match, label_mapping: solid}
        FE-->>Siswa: Momo EXCITED: "Hebat! Kamu berani percaya diri."
        FE->>FE: Spawn objek sebagai Solid sesuai mapping (label_mapping=solid)
        FE-->>Siswa: Lanjut ke FASE 8 Result & Feedback
    else Label TIDAK ADA di Top-6 (FORCE VERIFY)
        BE->>DB: INSERT INTO interaction_logs (student_id, ..., top6_match=false, ...)
        DB-->>BE: ACK insert success
        BE-->>FE: 200 OK {accepted: false, reason: top6_no_match, action: redraw}
        FE-->>Siswa: Momo CONFUSED: "Aku belum kenal itu. Gambar ulang yuk?"
        FE->>FE: Reset canvas, increment attempt_counter
        FE-->>Siswa: Kembali ke FASE 5 Main Gameplay (dengan attempt_counter +1)
    end
```

### 4.3 Data Logging Flow (Frontend → Backend → DB → K-Means Offline Batch)

```mermaid
sequenceDiagram
    actor Siswa
    participant FE as Frontend
    participant BE as Backend API
    participant DB as Database
    participant KM as K-Means Worker (offline batch)

    Note over Siswa,FE: FASE 5-8: Setiap aksi HITL menghasilkan event log (fire-and-forget)

    Siswa->>FE: Aksi gameplay (draw_start, draw_end, accept, correct, override, move_stickman, complete_level, fail_level)
    FE->>FE: Pack event {event_type, payload, timestamp_ms, level, probe_id, time_spent_ms}
    FE->>BE: POST /logs/event {session_token, event}

    BE->>BE: Validate session_token + extract student_id, class_id, school_id
    BE->>DB: INSERT INTO interaction_logs (student_id, class_id, school_id, level, probe_id, event_type, payload_json, time_spent_ms, confidence_top1, confidence_top6, decision_type, override_label, top6_match, timestamp)
    DB-->>BE: ACK insert success
    BE-->>FE: 204 No Content (fire-and-forget, tidak menunggu ACK untuk gameplay)

    Note over Siswa,FE: Gameplay berlanjut tanpa blocking

    Note over KM: ===== OFFLINE BATCH (cron 23:00 daily atau on-demand Guru) =====

    actor Guru
    Guru->>BE: POST /analysis/trigger-kmeans {class_id, date_range}
    BE->>BE: Validate guru has access to class_id
    BE->>KM: Submit job {class_id, student_ids[], log_window_start, log_window_end}
    KM->>DB: SELECT student_id, event_type, decision_type, time_spent_ms, confidence_top1, override_label, top6_match FROM interaction_logs WHERE class_id=? AND timestamp BETWEEN ? AND ?
    DB-->>KM: Log rows (raw, per-event)

    KM->>KM: Feature engineering per student:<br/>- decision_type_ratio (accept/correct/override percentages)<br/>- mean_latency_ms (avg time_spent_ms per probe)<br/>- confidence_gap_mean (avg |top1-top2|)<br/>- override_frequency (override count / total probes)<br/>- top6_match_rate (top6_match=true / total override)

    KM->>KM: Run K-Means (k=3 atau elbow method, max_iter=100)
    KM->>DB: INSERT INTO clusters (class_id, student_id, cluster_id, centroid_distance, run_at, feature_vector_json)
    KM-->>BE: Job done {cluster_count, students_per_cluster, centroid_profiles}
    BE-->>Guru: 200 OK {cluster_distribution, centroid_profiles, run_summary}

    Note over Guru: Guru dapat melihat hasil cluster di dashboard

    Guru->>BE: GET /analysis/clusters/{class_id}
    BE->>DB: SELECT * FROM clusters WHERE class_id=? ORDER BY cluster_id, student_id
    DB-->>BE: Cluster assignments + centroid distances
    BE-->>Guru: JSON cluster distribution + drill-down per cluster
    Guru-->>Guru: Visualisasi bar chart distribusi siswa per cluster + centroid profile per cluster
```

---

## 5. LaTeX-Ready Section — 3.2.2 Alur Pengguna

> Section berikut siap di-include ke `bab3_can.tex` sebagai pengganti atau ekspansi dari subsection 3.2.2 (Alur Pengguna) yang lama. Subsection lama hanya berisi alur global siswa tanpa pembedaan per aktor; versi ini membedakan alur per aktor (Siswa, Guru, Superadmin) sesuai PIVOT #1 16/6/26 yang menambahkan aktor Superadmin.

### 3.2.2 Alur Pengguna

\label{subsec:alur-pengguna}

Alur pengguna dirancang secara linear dengan sembilan fase utama: Login, Onboarding, Level Select, Tutorial, Main Gameplay, Probe UI, Top-6 Verification (jika Override), Result \& Feedback, dan Next Level. Linearitas alur didasarkan pada prinsip \textit{Child--Computer Interaction} (CCI)~[2] yang menekankan bahwa interaksi untuk anak usia 12--15 tahun harus sederhana dan dapat diprediksi, serta prinsip scaffolding~[6][7] yang mensyaratkan progresi trust building $\rightarrow$ ambiguitas $\rightarrow$ override terjadi secara terprediksi.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Alur Pengguna Sistem Sketchbook Universe --- 9 Fase Linear}
    \label{fig:alur-pengguna-global}
\end{figure}

> \textbf{Catatan penulis:} Diagram alur pengguna lengkap (Gambar~\ref{fig:alur-pengguna-global}) akan dilengkapi oleh penulis pada tahap implementasi setelah playtest awal. Kerangka alur secara textual sudah final dan dijelaskan pada sub-bab ini.

#### 3.2.2.1 Alur Pengguna Siswa

Alur pengguna Siswa mengikuti sembilan fase linear yang dijelaskan di atas. Tiga titik kritis pada alur Siswa adalah: (1) Login dengan nomor absen --- menggantikan gesture MediaPipe yang dideprecate post-pivot 16/6/26; (2) Probe UI sebagai titik jeda evaluatif sesuai prinsip XAI~[3] dan HITL~[4]; dan (3) Top-6 Verification yang menggantikan Override Budget post-pivot 16/6/26 (PIVOT \#2) --- mekanisme anti-cheat yang lebih elegant karena tidak membatasi jumlah override, melainkan memverifikasi kewajaran label override terhadap Top-6 prediksi AI.

> \textbf{Catatan penulis:} Diagram alur pengguna Siswa lengkap (flowchart per fase dengan decision branch) akan dilengkapi oleh penulis pada tahap implementasi.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Alur Pengguna Siswa --- 9 Fase dengan Decision Branch (Override Top-6 Check)}
    \label{fig:alur-pengguna-siswa}
\end{figure}

#### 3.2.2.2 Alur Pengguna Guru / Admin Sekolah

Alur pengguna Guru bersifat non-gameplay dan berfokus pada analisis data. Lima fase alur Guru: (1) Login dengan username + password yang dibuat superadmin; (2) View Assigned Classes --- melihat daftar kelas yang ditugaskan; (3) View Class Dashboard --- melihat dashboard analitik per kelas (decision distribution, confidence calibration, decision latency); (4) Drill-down opsional --- View Individual Student History atau Trigger K-Means Cluster Analysis; (5) Export Class Data (opsional, untuk analisis eksternal di Excel/SPSS).

> \textbf{Catatan penulis:} Diagram alur pengguna Guru lengkap akan dilengkapi oleh penulis pada tahap implementasi.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Alur Pengguna Guru / Admin Sekolah --- 5 Fase Analitik}
    \label{fig:alur-pengguna-guru}
\end{figure}

#### 3.2.2.3 Alur Pengguna Superadmin (BARU)

Alur pengguna Superadmin --- aktor baru post-pivot 16/6/26 --- berfokus pada provisioning dan management entitas. Tujuh fase alur Superadmin: (1) Login superadmin (credentials yang dibuat saat deployment, bukan dari sistem); (2) View All Schools Overview --- melihat daftar sekolah yang sudah terdaftar; (3) Create School (jika sekolah baru) --- input nama sekolah, alamat, jenjang; (4) Create Class --- input nama kelas di bawah sekolah tertentu; (5) Generate Nomor Absen Siswa --- tentukan jumlah slot (mis: 40) dan sistem membuat 40 entitas siswa kosong; (6) Create Guru Account + Assign Guru to Class --- buat akun guru dan tugaskan ke kelas; (7) View All Classes per School (monitoring) --- drill-down ke kelas untuk verifikasi assignment.

> \textbf{Catatan penulis:} Diagram alur pengguna Superadmin lengkap akan dilengkapi oleh penulis pada tahap implementasi.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Alur Pengguna Superadmin --- 7 Fase Provisioning Multi-Sekolah}
    \label{fig:alur-pengguna-superadmin}
\end{figure}

#### 3.2.2.4 Sequence Diagram Key Flows

Tiga sequence diagram key flows sistem ditunjukkan pada Gambar~\ref{fig:seq-login}, Gambar~\ref{fig:seq-override}, dan Gambar~\ref{fig:seq-logging}. Diagram-diagram ini merinci interaksi antar komponen (Siswa, Frontend, Backend, Database, K-Means Worker) pada tiga titik kritis: Login, Override + Top-6 Check, dan Data Logging.

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Sequence Diagram --- Login Flow (Siswa $\rightarrow$ Frontend $\rightarrow$ Backend $\rightarrow$ Database)}
    \label{fig:seq-login}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Sequence Diagram --- Override + Top-6 Check Flow (Post-Pivot PIVOT \#2 16/6/26)}
    \label{fig:seq-override}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{placeholder}
    \caption{Sequence Diagram --- Data Logging Flow (Frontend $\rightarrow$ Backend $\rightarrow$ Database $\rightarrow$ K-Means Offline Batch)}
    \label{fig:seq-logging}
\end{figure}

> \textbf{Catatan penulis:} Source Mermaid untuk ketiga sequence diagram tersedia di file \texttt{User\_Flow\_Placement\_v1.md} Section 4. Render ke PNG via \texttt{mmdc input.mmd -o output.png -b white} sebelum di-include ke LaTeX.

---

## 6. Referensi & Sumber

- `MEMORY.md` Section 10 — PIVOT #1 (Login gesture → nomor absen + superadmin)
- `MEMORY.md` Section 10 — PIVOT #2 (Override Budget → Top-6 Check)
- `MEMORY.md` Section 10 — DECISION #3 (Timer spontaneous)
- `MEMORY.md` Section 10 — DECISION #4 (Resize & Rotate buttons)
- `Outline_dan_Sitasi_PreLatex.md` Section 8 — Outline Bab 3 Can (3.2.2 Alur Pengguna)
- `bab3_can.tex` existing (lines 66--82) — Alur Pengguna section lama (Onboarding + Core Gameplay Loop + Level Summary, 3 fase)
- A02 (Casal-Otero et al. 2022) — CCI K-12, dasar alur linear
- A04 (Mosqueira-Rey et al. 2023) — HITL, dasar Probe UI sebagai jeda
- A05 (Memarian & Doleck 2025) — HITL roles, dasar Accept/Correct/Override
- A06 (Videnovik et al. 2023) — Game-based learning, dasar consequence-driven feedback
- A07 (Chan, Wan & King 2024) — Flow Theory, dasar progresi skill > challenge → challenge > skill

---

## 7. Mermaid Diagrams v2 — Placeholder Replacements (POLOSAN)

> **Tujuan:** Section ini menyediakan 9 diagram Mermaid (POLOSAN — tanpa `classDef`, tanpa `style`, tanpa `fill`, tanpa emoji, tanpa hex color code) sebagai pengganti placeholder `\placeholderfig{...}` di `draf_proposal_can_v0.0.0.tex`. Setiap diagram dikaitkan dengan nomor Gambar pada LaTeX Can (Gambar 3.1, 3.4–3.7, 3.11–3.14). Konvensi shape: stadium `([text])` untuk Start/End, parallelogram `[/text/]` untuk Input/Output, rectangle `[text]` untuk Process, diamond `{text?}` untuk Decision. Semua label berbahasa Indonesia.

### 7.1 Waterfall SDLC (Gambar 3.1 — Metode Pengembangan)

Diagram alur metode pengembangan Waterfall SDLC 5 tahap berurutan dengan dua feedback loop (defect found dari Verification ke Design, dan playtest feedback dari Maintenance ke Requirements).

```mermaid
%% Gambar 3.1 — Waterfall SDLC 5 Tahap Berurutan
%% POLOSAN: no classDef, no style, no fill color, no emoji
%% Shape: rectangle untuk tahap proses, dotted arrow untuk feedback loop
flowchart LR
    R[Requirements Analysis<br/>analisis kebutuhan fungsional<br/>+ non-fungsional, pivot 16/6/26] --> D[System Design<br/>arsitektur hybrid CNN+REST<br/>use case 3 aktor, fishbone 6M]
    D --> I[Implementation<br/>frontend Kaplay.js<br/>backend REST API, K-Means worker]
    I --> V[Verification<br/>pengujian SUS + black-box<br/>K-Means clustering validation<br/>confusion matrix CNN]
    V --> M[Maintenance<br/>deploy ke kelas SMP<br/>monitoring, iterasi post-playtest]

    %% Feedback loops
    V -.->|defect found| D
    M -.->|playtest feedback| R
```

> Render via `mmdc 7-1-waterfall-sdlc.mmd -o 7-1-waterfall-sdlc.png -b white` untuk di-include ke LaTeX.

### 7.2 User Flow Global 9 Fase (Gambar 3.4 — Alur Pengguna Global)

Diagram alur pengguna global 9 fase linear dengan satu decision diamond utama (Override?) dan sub-decision (Match?) untuk Top-6 Verification.

```mermaid
%% Gambar 3.4 — Alur Pengguna Global 9 Fase Linear
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start]) --> L[/Login<br/>input class_id + nomor_absen/]
    L --> O[Onboarding<br/>Momo intro + tutorial]
    O --> LS[Level Select]
    LS --> T[Tutorial per Level]
    T --> MG[Main Gameplay<br/>draw + resize atau rotate<br/>timer count-up]
    MG --> P[Probe UI<br/>Top-3 + Momo reaction]
    P --> D{Override?}
    D -->|No| RF[Result and Feedback]
    RF --> NL[Next Level atau Retry]
    D -->|Yes| TV[Top-6 Verification]
    TV --> DM{Match?}
    DM -->|Yes| RF2[Result and Feedback<br/>sukses]
    RF2 --> NL
    DM -->|No| RD[Redraw]
    RD --> MG
    NL --> E([End])
```

> Render via `mmdc 7-2-user-flow-global.mmd -o 7-2-user-flow-global.png -b white` untuk di-include ke LaTeX.

### 7.3 User Flow Siswa (Gambar 3.5 — Alur Pengguna Siswa dengan Decision Branch Override Top-6 Check)

Diagram alur pengguna Siswa secara granular: login via nomor absen, onboarding, level select, main gameplay dengan tombol Resize/Rotate/Erase, Probe UI, dan tiga branch keputusan (Accept, Correct, Override dengan Top-6 Check).

```mermaid
%% Gambar 3.5 — Alur Pengguna Siswa 9 Fase dengan Decision Branch Override Top-6 Check
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start]) --> L1[/Pilih class_id dropdown/]
    L1 --> L2[/Input nomor_absen 1-99/]
    L2 --> L3[Validasi backend]
    L3 --> L4[Momo HAPPY greeting]
    L4 --> O[Onboarding<br/>splash 2s + Momo perkenalan<br/>tutorial 1 layar aturan Solid/Danger]
    O --> LS[Level Select<br/>Level 1 unlocked<br/>Level 2 atau 3 progressive unlock]
    LS --> T[Tutorial singkat level<br/>objective + batasan<br/>Momo emotion baseline]
    T --> MG[Main Gameplay<br/>draw canvas + Resize + Rotate + Erase<br/>Timer count-up]
    MG --> SB[/Submit gambar/]
    SB --> P[Probe UI appears<br/>gameplay pause<br/>Top-3 + confidence bar<br/>Momo THINKING]
    P --> D{Siswa pilih aksi?}
    D -->|Accept| R1[Result: Solid atau Danger behavior<br/>Momo HAPPY]
    D -->|Correct Level 2 plus| C2[/Pilih Top-2 atau Top-3/]
    C2 --> R2[Result<br/>Momo HAPPY]
    D -->|Override Level 2 atau 3| OI[/Input label sendiri/]
    OI --> T6[Top-6 Check]
    T6 --> DM{Match?}
    DM -->|Yes| AA[Auto-accept<br/>Result<br/>Momo EXCITED]
    DM -->|No| RD[Redraw attempt_counter plus 1<br/>Momo CONFUSED]
    RD --> MG
    R1 --> RF[Result and Feedback<br/>stickman moves<br/>Momo state per outcome]
    R2 --> RF
    AA --> RF
    RF --> LSM[Level Summary]
    LSM --> NL[Next Level atau Retry]
    NL --> E([End])
```

> Render via `mmdc 7-3-user-flow-siswa.mmd -o 7-3-user-flow-siswa.png -b white` untuk di-include ke LaTeX.

### 7.4 User Flow Guru / Admin Sekolah (Gambar 3.6 — 5 Fase Analitik)

Diagram alur pengguna Guru/Admin Sekolah: login dengan kredensial dari superadmin, view assigned classes, view class dashboard dengan tiga chart analitik, drill-down opsional (Individual Student History atau K-Means Cluster Analysis), dan export CSV.

```mermaid
%% Gambar 3.6 — Alur Pengguna Guru atau Admin Sekolah 5 Fase Analitik
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start]) --> L[/Login<br/>username + password dari superadmin/]
    L --> V[Validasi]
    V --> AC[View Assigned Classes<br/>hanya kelas yang di-assign]
    AC --> PK[Pilih kelas]
    PK --> CD[View Class Dashboard<br/>decision distribution chart<br/>confidence calibration chart<br/>decision latency chart]
    CD --> D{Drill-down?}
    D -->|Individual| ISH[View Individual Student History]
    ISH --> FS[Filter by student]
    FS --> LT[Lihat log timeline per siswa]
    D -->|K-Means| TKC[Trigger K-Means Cluster Analysis]
    TKC --> SJ[/Submit job<br/>date range/]
    SJ --> WH[Tunggu hasil]
    WH --> LC[Lihat 3 cluster distribution<br/>+ centroid profiles]
    LT --> EX[/Export Class Data CSV/]
    LC --> EX
    EX --> E([End])
```

> Render via `mmdc 7-4-user-flow-guru.mmd -o 7-4-user-flow-guru.png -b white` untuk di-include ke LaTeX.

### 7.5 User Flow Superadmin (Gambar 3.7 — 7 Fase Provisioning Multi-Sekolah)

Diagram alur pengguna Superadmin (aktor baru post-pivot 16/6/26 PIVOT #1): login dengan kredensial deployment, view all schools overview, dua decision (sekolah baru? kelas baru?), generate nomor absen siswa, create guru account, assign guru to class, monitoring.

```mermaid
%% Gambar 3.7 — Alur Pengguna Superadmin 7 Fase Provisioning Multi-Sekolah
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start]) --> L[/Login superadmin<br/>credentials dari deployment<br/>bukan dari sistem/]
    L --> ASO[View All Schools Overview]
    ASO --> D1{Sekolah baru?}
    D1 -->|Yes| CS[Create School<br/>nama, alamat, jenjang]
    CS --> ASO
    D1 -->|No| PS[Pilih sekolah]
    PS --> VCP[View Classes per School]
    VCP --> D2{Kelas baru?}
    D2 -->|Yes| CC[Create Class<br/>nama kelas, level SMP]
    CC --> VCP
    D2 -->|No| PK[Pilih kelas]
    PK --> GNA[Generate Nomor Absen Siswa<br/>tentukan slot count mis: 40<br/>sistem create 40 student records kosong]
    GNA --> CGA[Create Guru Account<br/>username, password, nama]
    CGA --> AGC[Assign Guru to Class]
    AGC --> VAC[View All Classes per School<br/>monitoring, verifikasi assignment]
    VAC --> E([End])
```

> Render via `mmdc 7-5-user-flow-superadmin.mmd -o 7-5-user-flow-superadmin.png -b white` untuk di-include ke LaTeX.

### 7.6 User Flow Level 1 — Guided Recognition (Gambar 3.11 — Trust Building)

Diagram alur pengguna Level 1: fokus trust building siswa terhadap AI. Siswa hanya bisa Accept (tidak ada Correct/Override button di Level 1). Momo selalu HAPPY untuk membangun trust awal.

```mermaid
%% Gambar 3.11 — Alur Pengguna Level 1 Guided Recognition Trust Building
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start Level 1]) --> MI[Momo intro:<br/>Yuk kenalan, AI ini bisa tebak gambar kamu!]
    MI --> OP[/Show object prompt<br/>mis: Gambar PISANG/]
    OP --> DG[Siswa gambar di canvas<br/>Resize atau Rotate atau Eraser available<br/>timer count-up]
    DG --> SB[/Submit/]
    SB --> AC[AI classify<br/>CNN MobileNet]
    AC --> T3[Top-3 predictions shown<br/>transparent]
    T3 --> AC2[Siswa Accept<br/>default, tidak ada Correct atau Override button<br/>di Level 1]
    AC2 --> RS[Result: objek spawn sebagai Solid<br/>mis: pisang = Stickman bisa makan<br/>atau Danger mis: knife = Stickman kena damage]
    RS --> MH[Momo HAPPY:<br/>Hebat! AI tebak dengan benar.]
    MH --> LSM[Level Summary<br/>3 sampai 5 objek]
    LSM --> NL[Next Level 2 unlock]
    NL --> E([End Level 1])
```

> Render via `mmdc 7-6-user-flow-level-1.mmd -o 7-6-user-flow-level-1.png -b white` untuk di-include ke LaTeX.

### 7.7 User Flow Level 2 — Ambiguous Choice (Gambar 3.12 — Doubt & Calibration)

Diagram alur pengguna Level 2: fokus doubt dan calibration. Confidence gap sengaja kurang dari 0.10 (ambiguitas). Siswa bisa Accept, Correct, atau Override. Override memicu Top-6 Check.

```mermaid
%% Gambar 3.12 — Alur Pengguna Level 2 Ambiguous Choice Doubt Calibration
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start Level 2]) --> MI[Momo intro:<br/>Kadang AI bingung. Kamu bisa bantu pilih!]
    MI --> OP[/Show object prompt<br/>mis: Gambar SEPATU/]
    OP --> DG[Siswa gambar]
    DG --> SB[/Submit/]
    SB --> AC[AI classify]
    AC --> T3[Top-3 shown<br/>confidence gap kurang dari 0.10<br/>ambiguitas sengaja]
    T3 --> MC[Momo CONFUSED:<br/>Hmm, aku ragu sama tebakan ini.]
    MC --> D{Siswa pilih aksi?}
    D -->|Accept Top-1| A1[Result<br/>Momo HAPPY atau CONFUSED<br/>depending on outcome]
    D -->|Correct Top-2 atau Top-3| C1[Result<br/>Momo HAPPY:<br/>Pilihan bagus!]
    D -->|Override| OI[/Input label sendiri/]
    OI --> T6[Top-6 Check]
    T6 --> DM{Match?}
    DM -->|Yes| AA[Auto-accept<br/>Result<br/>Momo EXCITED]
    DM -->|No| RD[Redraw attempt plus 1<br/>Momo CONFUSED:<br/>Aku belum kenal itu.]
    RD --> DG
    A1 --> LSM[Level Summary]
    C1 --> LSM
    AA --> LSM
    LSM --> NL[Next Level 3 unlock]
    NL --> E([End Level 2])
```

> Render via `mmdc 7-7-user-flow-level-2.mmd -o 7-7-user-flow-level-2.png -b white` untuk di-include ke LaTeX.

### 7.8 User Flow Level 3 — Risk & Override (Gambar 3.13 — Human Agency)

Diagram alur pengguna Level 3: fokus human agency. Siswa FORCED to override (tidak ada Accept/Correct button). AI sengaja miss-classify. Momo EXCITED saat siswa berhasil override dengan label yang ada di Top-6 rahasia.

```mermaid
%% Gambar 3.13 — Alur Pengguna Level 3 Risk and Override Human Agency
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start Level 3]) --> MI[Momo intro:<br/>Sekarang kamu bos. Kalau AI salah, katakan saja.]
    MI --> OP[/Show object prompt<br/>mis: Gambar TANGGA/]
    OP --> DG[Siswa gambar]
    DG --> SB[/Submit/]
    SB --> AC[AI classify<br/>sengaja salah atau miss-classify<br/>mis: tangga dikira sword]
    AC --> T3[Top-3 shown<br/>confidence rendah kurang dari 50 persen]
    T3 --> MC[Momo CONFUSED:<br/>Aku yakin ini sword, tapi kamu?]
    MC --> OVR[Siswa OVERRIDE<br/>satu-satunya opsi koreksi di Level 3<br/>tidak ada Accept atau Correct button]
    OVR --> OI[/Input label sendiri: tangga/]
    OI --> T6[Top-6 Check]
    T6 --> DM{Match?}
    DM -->|Yes tangga ada di Top-6 rahasia| AA[Auto-accept<br/>objek spawn sebagai Solid<br/>Momo EXCITED:<br/>Hebat! Kamu berani percaya diri.]
    DM -->|No| RD[Redraw attempt plus 1<br/>Momo CONFUSED:<br/>Aku belum kenal itu. Gambar ulang yuk?]
    RD --> DG
    AA --> LSM[Level Summary<br/>refleksi Momo tentang keputusan siswa]
    LSM --> GC[Game Complete]
    GC --> MEF[Momo EXCITED:<br/>Kamu lulus Sketchbook Universe!]
    MEF --> E([End Game])
```

> Render via `mmdc 7-8-user-flow-level-3.mmd -o 7-8-user-flow-level-3.png -b white` untuk di-include ke LaTeX.

### 7.9 Top-6 Check Flow Diagram (Gambar 3.14 — Mekanisme Anti-Cheat Post-Pivot PIVOT #2 16/6/26)

Diagram alur mekanisme Top-6 Check: siswa submit override label → frontend validasi → POST ke backend → backend validate session → Top-6 case-insensitive match → dua branch (MATCH: auto-accept dan spawn Solid; NO MATCH: redraw dengan attempt_counter+1). Log insertion ke `interaction_logs` di kedua branch.

```mermaid
%% Gambar 3.14 — Mekanisme Top-6 Check Flow Diagram Post-Pivot PIVOT #2 16/6/26
%% POLOSAN: no classDef, no style, no fill color
%% Shape: stadium Start/End, parallelogram Input, rectangle Process, diamond Decision
flowchart TD
    S([Start: Siswa submit override label<br/>text, max 32 char, no special char]) --> FV[Frontend validasi label<br/>non-empty, length, character whitelist]
    FV --> POST[POST endpoint probe-override<br/>body: session_token, drawing_blob_url,<br/>top6, override_label, level,<br/>probe_id, time_spent_ms]
    POST --> BV[Backend: validate session_token<br/>extract student_id, class_id, school_id]
    BV --> T6[Backend: Top-6 Check<br/>case-insensitive match<br/>override_label vs top6 label<br/>top6 = 6 prediksi teratas CNN<br/>hanya Top-3 ditampilkan ke siswa]
    T6 --> D{Label ADA di Top-6?}
    D -->|Yes MATCH| IY[INSERT interaction_logs<br/>top6_match true<br/>decision_type override<br/>override_label, time_spent_ms,<br/>confidence_top6]
    IY --> RY[200 OK<br/>accepted true<br/>reason top6_match<br/>label_mapping solid]
    RY --> FY[Frontend: Momo EXCITED]
    FY --> SY[Spawn objek Solid]
    SY --> RF[Result and Feedback]
    D -->|No NO MATCH| IN[INSERT interaction_logs<br/>top6_match false<br/>lainnya sama seperti branch MATCH]
    IN --> RN[200 OK<br/>accepted false<br/>reason top6_no_match<br/>action redraw]
    RN --> FN[Frontend: Momo CONFUSED]
    FN --> RN2[Reset canvas<br/>attempt_counter plus 1]
    RN2 --> MG[Main Gameplay]
    RF --> E([End])
    MG --> E2([End])
```

> Render via `mmdc 7-9-top-6-check.mmd -o 7-9-top-6-check.png -b white` untuk di-include ke LaTeX.

---

> **Catatan akhir Section 7:** Semua 9 diagram di atas sudah POLOSAN (tidak ada `classDef`, `style`, `fill`, `stroke`, `color`, `linkStyle`, `css`, `%%{init: ...}%%`, emoji, atau hex color code). Setiap diagram dapat di-render langsung via Mermaid CLI (`mmdc`) ke PNG dengan background putih (`-b white`), lalu di-include ke `draf_proposal_can_v0.0.0.tex` sebagai pengganti placeholder `\placeholderfig{...}` yang bersesuaian (Gambar 3.1, 3.4, 3.5, 3.6, 3.7, 3.11, 3.12, 3.13, 3.14). Section 4 (Sequence Diagrams Mermaid) tidak diubah dan tetap menjadi rujukan untuk sequence diagram key flows.
