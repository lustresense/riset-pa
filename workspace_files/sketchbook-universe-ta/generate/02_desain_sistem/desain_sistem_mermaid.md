# Desain Sistem Global — Mermaid Diagram
# Sketchbook Universe — Simulasi Interaktif Literasi AI

> **Catatan:** Diagram ini disederhanakan berdasarkan:
> 1. Gambar referensi dari Can (16/6/26)
> 2. Notulensi Bu Hesti 16/6/26
> 3. SATU diagram global, warna per scope, shape flowchart standar
>
> **Perubahan dari versi lama:**
> - Dekoratif DIHAPUS — hanya Solid + Danger
> - Login WAJIB gesture-based
> - Tidak ada kata "from"
> - Warna konsisten per scope

---

## Diagram 1 — Global IPO

```mermaid
flowchart TB
    START((START))

    subgraph INPUT["INPUT"]
        direction LR
        I1["Siswa SMP"]
        I2["Gesture Tangan + Kamera"]
        I3["Gambar Sketsa dari Canvas"]
        I4["Keputusan: Accept / Override"]
        I5["Konteks Level: Rintangan + Aturan"]
    end

    subgraph L1["LAYER 1 - INTERAKSI - Can"]
        A1["Onboarding + Tutorial"]
        A2["Finger Tracking - MediaPipe"]
        A3["Drawing Canvas"]
        A4["Probe UI - HITL Point"]
        A5["Gameplay 2D - Kaplay.js"]
        A6["Feedback Momo - Text Bubble"]
    end

    subgraph L2["LAYER 2 - KLASIFIKASI AI - Dias"]
        B1["Image Preprocessing"]
        B2["CNN MobileNet - TensorFlow.js"]
        B3["Top-3 + Confidence Score"]
    end

    subgraph L3["LAYER 3 - KEPUTUSAN - Shared"]
        C1{"Decision Resolver"}
        C2["Mapping: Solid / Danger Duri"]
        C3["Gameplay Outcome"]
    end

    subgraph L4["LAYER 4 - DATA - Dias"]
        D1["Interaction Data Logging"]
        D2["REST API ke SQLite"]
        D3["Feature Engineering"]
        D4["K-Means Clustering"]
        D5["Dashboard + Export CSV JSON"]
    end

    subgraph OUTPUT["OUTPUT"]
        direction LR
        O1["Prototype Literasi AI"]
        O2["Pengalaman HITL Siswa"]
        O3["Objek Game Solid / Danger"]
        O4["Dataset Log Interaksi"]
        O5["Analisis Pola Keputusan"]
        O6["Dashboard / CSV / JSON"]
    end

    END((END))

    START --> INPUT
    I1 --> A1
    I2 --> A2
    I3 --> A3
    I4 --> A4
    I5 --> A5
    A1 --> A2
    A2 --> A3
    A3 -->|"Canvas Image"| B1
    A4 --> C1
    A6 --> A5
    B1 --> B2
    B2 --> B3
    B3 -->|"Top-3 + Confidence"| A4
    C1 --> C2
    C2 --> C3
    C3 --> A5
    C3 --> D1
    D1 --> D2
    D2 --> D3
    D3 --> D4
    D4 --> D5
    D5 --> OUTPUT
    A5 --> O3
    D2 --> O4
    D4 --> O5
    D5 --> O6
    OUTPUT --> END
```

---

## Diagram 2 — Game Loop

```mermaid
flowchart LR
    DRAW["DRAW - Siswa gambar di Canvas"]
    INFER["INFER - CNN MobileNet klasifikasi"]
    PROBE["PROBE - Momo tampilkan tebakan AI"]
    DECIDE{"DECIDE - Siswa pilih"}
    ACCEPT["Accept - Setuju AI"]
    OVERRIDE["Override - Koreksi AI"]
    RENDER["RENDER - Hasil divisualisasi"]

    DRAW -->|"Canvas Image"| INFER
    INFER -->|"Top-3 + Conf"| PROBE
    PROBE -->|"Tebakan AI"| DECIDE
    DECIDE -->|"Setuju"| ACCEPT
    DECIDE -->|"Koreksi"| OVERRIDE
    ACCEPT --> RENDER
    OVERRIDE --> RENDER
    RENDER -->|"Next ronde"| DRAW
```

---

## Diagram 3 — Arsitektur Hybrid

```mermaid
flowchart LR
    subgraph BROWSER["BROWSER - Client - Can"]
        KAP["Kaplay.js Game Engine"]
        MP["MediaPipe Hands"]
        CV["Drawing Canvas"]
        MOMO["Momo Maskot"]
        TFJS["TensorFlow.js CNN"]
        PUI["Probe UI HITL"]
    end

    subgraph SERVER["SERVER - Backend - Dias"]
        API["REST API Express"]
        DB["SQLite Data Log"]
        KM["K-Means Clustering"]
        DASH["Dashboard Analisis"]
    end

    BROWSER <-->|"HTTP JSON /api/v1"| SERVER
```

---

## Diagram 4 — 3 Level Progression

```mermaid
flowchart TB
    L1["LEVEL 1 PEMANASAN - Top-1 only, Confidence 85-96%, Momo Senang, Tidak ada fail"]
    L2["LEVEL 2 KERAGUAN - Top-3 + Conf 55-70%, Momo Ragu, Kertas sobek sedikit"]
    L3["LEVEL 3 JEBAKAN - Top-1 Manipulasi salah, Momo Overconfident, Game Over atau Menang"]

    L1 -->|"Page turn"| L2
    L2 -->|"Page turn + awan"| L3
```
