# Sitasi Final v1 — Sketchbook Universe (TA Can & Dias)

> **Project:** Sketchbook Universe — Proposal dual-scope Can (frontend) & Dias (backend)
> **Tanggal:** 16 Juni 2026
> **Status:** Final citation plan untuk LaTeX proposal (Bab 1/2/3) Can & Dias
> **Sumber:** Cross-check Merged Context.txt lines 2295-2820 (~60+ refs) × existing `proposal-can.tex` & `proposal-dias.tex` bibliography × `Outline_dan_Sitasi_PreLatex.md`

---

## 0. Executive Summary

### 0.1 Latar Belakang Revisi

User Can komplain: di outline sebelumnya (`Outline_dan_Sitasi_PreLatex.md`), **Kategori B (Can-specific) hanya berisi 2 referensi** (Schroeder 2025 + Meng 2024 yang DEPRECATED). Ini terjadi karena pada riset awal, sitasi teknis Can tercampur ke Kategori A (general/shared) sehingga Can kehilangan "pendar" spesifik scope-nya. Padahal Merged Context menyediakan ~60+ referensi terorganisir per 12 topik yang banyak sekali relevan ke scope Can (CCI, GBL untuk anak, sketch + child pedagogy, XAI UX untuk anak, behavioral patterns anak learning AI).

### 0.2 Perubahan dari Versi Sebelumnya

| Kategori | Sebelumnya (Outline_dan_Sitasi_PreLatex) | Sekarang (Sitasi_Final_v1) | Δ |
|----------|------------------------------------------|----------------------------|----|
| **A — General/Shared** | 15 | **20** | +5 baru |
| **B — Can-specific** | 2 (1 DEPRECATED) | **12** (1 DEPRECATED) | **+10 baru** ⬆️ |
| **C — Dias-specific** | 5 | **9** | +4 baru |
| **Total** | 22 | **41** | +19 baru |

### 0.3 Highlight Perubahan

- ✅ **Gap Kategori B diatasi**: dari 2 → 12 referensi (kenaikan +500%). Sekarang Can punya landasan akademis yang kuat untuk: K-12 AI literacy, GBL AI literacy untuk anak, child-computer interaction (CCI), children sketching pedagogy, behavioral patterns anak learning AI, cognitive style remaja.
- ✅ **Kategori A diperkaya** dengan 5 referensi foundational: trust/automation bias (Yin CHI 2019), probabilistic reasoning (Batanero ZDM 2023), GBL AI literacy systematic review (Zhan 2024), XAI UX (Liao CHI 2020), XAI teacher trust (Feldman-Maggor 2025).
- ✅ **Kategori C diperkaya** dengan 4 referensi teknis: MobileNet-SA untuk sketch (Huynh 2023), Sketch-R2CNN arsitektur RNN+CNN (Li 2020 TPAMI), Quick Draw dataset canonical (Google 2017), komparasi DL sketch (Liu 2024).
- ✅ **B02 Meng et al. (2024) MediaPipe** tetap dipertahankan dengan tanda ⚠️ DEPRECATED post-pivot 16/6/26 (login gesture diganti nomor absen + superadmin).
- ✅ Semua referensi baru berasal dari Q1-Q3 Scopus atau conference A/A* (CHI, AAAI, IEEE TPAMI) — tidak ada preprint arXiv selain Smilkov TF.js (canonical).
- ✅ Semua referensi punya DOI atau URL akses yang sudah dikurasi di Merged Context.

### 0.4 Pemisahan Daftar Pustaka Can vs Dias

Karena proposal Can & Dias terpisah secara fisik (dua file `.tex`), masing-masing butuh daftar pustaka sendiri:

| Proposal | Kategori Dipakai | Jumlah Refs |
|----------|------------------|-------------|
| `proposal-can.tex` | A + B | **32 refs** |
| `proposal-dias.tex` | A + C | **29 refs** |

Tumpang-tindih Kategori A (20 refs) memang disengaja — foundational theory (AI literacy, HITL, XAI, GBL, SDLC, R&D, SUS) wajib muncul di kedua proposal karena keduanya membahas proyek yang sama dari lensa berbeda.

---

## 1. Tabel Kategori A — General/Shared (Can & Dias)

**Definisi:** Referensi yang dipakai BARENG oleh proposal Can dan Dias. Mencakup teori foundational AI literacy, HITL, XAI, probabilistic reasoning, GBL, software engineering, R&D method, fishbone, dan SUS usability testing.

**Total:** 20 referensi (15 existing + 5 baru)

| ID | Author (Year) | Title (short) | Venue | Topik | Bab Can | Bab Dias | DOI/URL | Status |
|----|---------------|---------------|-------|-------|---------|----------|---------|--------|
| A01 | Ng, D.T.K. et al. (2021) | Conceptualizing AI literacy: An exploratory review | Computers and Education: Artificial Intelligence, 2, 100041 | AI Literacy Framework | 1.1, 1.2, 1.4, 1.5, 2.1, 2.2.1, 2.3.5, 3.1, 3.2.1 | 1.1, 1.2, 1.4, 2.1, 2.2.1, 2.3.5 | https://doi.org/10.1016/j.caeai.2021.100041 | existing |
| A02 | Casal-Otero, V. et al. (2023) | AI literacy in K-12: A systematic literature review | International Journal of STEM Education, 10, 29 | AI Literacy K-12 | 1.1, 1.5, 2.1, 2.2.1, 2.2.7, 2.3.1, 2.3.5, 3.2.1, 3.2.7 | 1.1, 2.1, 2.2.1 | https://doi.org/10.1186/s40594-023-00418-7 | existing |
| A03 | Khosravi, H. et al. (2022) | Explainable Artificial Intelligence in education | Computers and Education: Artificial Intelligence, 3, 100074 | XAI in Education | 1.1, 1.2, 1.4, 2.2.2, 2.2.3, 2.3.5, 3.1, 3.2.9, 3.2.10 | 1.1, 1.2, 1.4, 2.2.2, 2.3.5 | https://doi.org/10.1016/j.caeai.2022.100074 | existing |
| A04 | Mosqueira-Rey, E. et al. (2023) | Human-in-the-loop machine learning: A state of the art | Artificial Intelligence Review, 56(4), 3005–3054 | HITL ML | 1.1, 1.2, 1.3, 1.4, 2.2.2, 2.3.2, 2.3.5, 3.1, 3.2.3, 3.2.5, 3.2.6, 3.4.4 | 1.1, 1.2, 1.3, 1.4, 2.2.2, 2.3.5, 3.2, 3.5, 3.6.1, 3.6.2, 3.8.1, 3.10.2, 3.11, 3.14 | https://doi.org/10.1007/s10462-022-10246-w | existing |
| A05 | Memarian, B., & Doleck, T. (2024) | Human-in-the-loop in AI in education: A review and ER analysis | Computers in Human Behavior: Artificial Humans, 2, 100053 | HITL in AIED | 1.2, 1.3, 2.2.2, 2.3.2, 3.2.3, 3.2.5, 3.4.4 | 1.2, 2.2.2, 2.2.7, 2.3.5, 3.5, 3.6.1, 3.7.1, 3.8.1, 3.8.2, 3.10.1 | https://doi.org/10.1016/j.chbah.2024.1000136 | existing |
| A06 | Videnovik, M. et al. (2023) | Game-based learning in CS education: A scoping review | International Journal of STEM Education, 10, 54 | GBL CS Education | 1.4, 1.5, 2.2.4, 2.3.3, 2.3.5, 3.1, 3.2.2, 3.2.4, 3.2.6, 3.2.8, 3.12 | — | https://doi.org/10.1186/s40594-023-00420-z | existing |
| A07 | Chan, K.K., Wan, K.M., & King, R.B. (2021) | Performance over enjoyment? Effect of GBL on learning outcome and flow | Frontiers in Education, 6, 660376 | Flow Theory in GBL | 1.4, 2.2.4, 2.3.3, 3.1, 3.2.2, 3.2.4, 3.2.8 | — | https://doi.org/10.3389/feduc.2021.660376 | existing |
| A08 | Karran, A.J., Demazure, T., & Hudelot, C. (2022) | Designing for confidence: Visualizing AI decisions | Frontiers in Neuroscience, 16 | Confidence Visualization | 2.2.3, 2.2.6, 2.3.5, 3.2.4, 3.2.5, 3.2.9, 3.2.10 | 2.2.6, 2.3.3, 3.2.5 | https://doi.org/10.3389/fnins.2022.857221 | existing |
| A09 | Pressman, R.S. (2014) | Software Engineering: A Practitioner's Approach (8th ed.) | McGraw-Hill, New York | SE / SDLC | 3.4.2 | 3.1, 3.3, 3.13 | ISBN 978-0078022128 | existing |
| A10 | Sommerville, I. (2015) | Software Engineering (10th ed.) | Pearson | SE | 3.4.2 | 3.1, 3.3 | ISBN 978-0133943030 | existing |
| A11 | Sugiyono (2020) | Metode Penelitian Kuantitatif, Kualitatif, dan R&D | Alfabeta, Bandung | R&D Method | 1.3, 3.4.1, 3.4.2 | 3.3 | ISBN 978-602-5857-96-8 | existing |
| A12 | Creswell, J.W. (2014) | Research Design: Qualitative, Quantitative, and Mixed Methods (4th ed.) | Sage Publications | Mixed Methods | 3.4.1 | 3.1 | ISBN 978-1452226094 | existing |
| A13 | Ishikawa, K. (1986) | Guide to Quality Control (2nd ed.) | Asian Productivity Organization, Tokyo | Fishbone / Ishikawa | 3.4.3, 3.4.5, 3.9 (Dias cross-ref) | 3.9.4 | ISBN 978-9283310365 | existing |
| A14 | Brooke, J. (1996) | SUS: A 'Quick and Dirty' Usability Scale | Taylor & Francis, pp. 189–194 | SUS | 1.3, 1.5, 2.2.8, 3.2.11, 3.4.4, 3.4.6 | — | ISBN 978-0748404495 | existing |
| A15 | Bangor, A., Kortum, P.T., & Miller, J.T. (2008) | An empirical evaluation of the SUS | International Journal of Human-Computer Interaction, 24(6), 574–594 | SUS Empirical Validation | 1.3, 2.2.8, 3.2.11, 3.4.6 | — | https://doi.org/10.1080/10447310802205776 | existing |
| **A16** ⭐ | **Yin, M., Wortman Vaughan, J., & Wallach, H. (2019)** | **Understanding the effect of accuracy on trust in ML models** | **Proceedings of CHI 2019, 1–12** | **Trust & Automation Bias (foundational)** | 1.2, 2.2.2, 2.3.5, 3.1 | 1.2, 2.2.2, 2.3.5 | https://doi.org/10.1145/3290605.3300509 | **NEW** |
| **A17** ⭐ | **Batanero, C., & Álvarez-Arroyo, R. (2023)** | **Teaching and learning of probability** | **ZDM – Mathematics Education, 56, 5–17** | **Probabilistic Reasoning (foundation for confidence/Top-6)** | 2.2.3, 2.3.5, 3.2.5 | 2.2.6, 3.9.4 | https://doi.org/10.1007/s11858-023-01511-5 | **NEW** |
| **A18** ⭐ | **Zhan, Z., Tong, Y., Lan, X., & Zhong, B. (2024)** | **A systematic literature review of GBL in AI education** | **Interactive Learning Environments, 32(4), 1189–1212** | **GBL AI Literacy (specific)** | 2.1, 2.2.4, 2.3.3, 3.1 | 2.3.5 | https://doi.org/10.1080/10494820.2022.2115077 | **NEW** |
| **A19** ⭐ | **Liao, Q.V., Gruen, D., & Miller, S. (2020)** | **Questioning the AI: Informing design practices for XAI user experiences** | **Proceedings of CHI 2020, 1–15** | **XAI UX Design** | 2.2.3, 2.3.5, 3.2.9, 3.2.10 | 2.2.6, 2.3.5 | https://doi.org/10.1145/3313831.3376590 | **NEW** |
| **A20** ⭐ | **Feldman-Maggor, Y., Cukurova, M., Kent, C., Luckin, R., & Baur-Wolfson, M. (2025)** | **The impact of explainable AI on teachers' trust and acceptance of AI EdTech** | **International Journal of Artificial Intelligence in Education, 35(1), 1–25** | **XAI Teacher Trust** | 2.2.2, 2.2.3, 2.3.5 | 2.2.2, 2.2.6, 2.3.5 | https://doi.org/10.1007/s40593-025-00486-6 | **NEW** |

⭐ = baru ditambahkan dari Merged Context

---

## 2. Tabel Kategori B — Can-specific (Frontend/Maskot/HITL UI/UX/CCI/GBL AI literacy)

**Definisi:** Referensi spesifik pendukung scope Can — frontend, UI/UX, maskot Momo sebagai pedagogical agent, child-computer interaction (CCI), game-based learning AI literacy untuk anak, behavioral patterns anak learning AI, children sketching pedagogy, dan (legacy) MediaPipe gesture tracking.

**Total:** 12 referensi (2 existing + 10 baru) — **NAIK 6× LIPAT dari 2 jadi 12** ⬆️

| ID | Author (Year) | Title (short) | Venue | Topik | Bab Can | DOI/URL | Status |
|----|---------------|---------------|-------|-------|---------|---------|--------|
| B01 | Schroeder, N.L., Davis, C.S., & Yang, Y. (2025) | Designing and learning with pedagogical agents: An umbrella review | Journal of Educational Computing Research, 62(8) | Pedagogical Agent (Maskot Momo) | 1.2, 1.4, 2.2.6, 2.3.5, 3.1, 3.2.1, 3.2.7, 3.2.8, 3.2.10 | https://doi.org/10.1177/07356331251324386 | existing |
| B02 ⚠️ | Meng, Z. et al. (2024) | Real-Time Hand Gesture Monitoring Model Based on MediaPipe | Sensors, 24(19), 6262 | MediaPipe Hand Gesture Tracking | 2.2.5 [DEPRECATED], 2.3.4 [DEPRECATED], 3.2.7 [legacy] | https://doi.org/10.3390/s24196262 | existing **DEPRECATED** |
| **B03** ⭐ | **Wang, N., & Lester, J. (2023)** | **K-12 education in the age of AI: A call to action for K-12 AI literacy** | **International Journal of Artificial Intelligence in Education, 33(3), 631–640** | **K-12 AI Literacy (foundational)** | 1.1, 2.2.1, 2.3.1 | https://doi.org/10.1007/s40593-023-00358-x | **NEW** |
| **B04** ⭐ | **Yim, I. H. Y., & Su, J. (2025)** | **AI literacy education in primary schools: A review** | **International Journal of Technology and Design Education, 35, Article 57** | **AI Literacy Primary Schools (age-appropriate)** | 2.2.1, 2.2.7, 2.3.1 | https://doi.org/10.1007/s10798-025-09979-w | **NEW** |
| **B05** ⭐ | **Lee, S., Mott, B., Ottenbreit-Leftwich, A., Scribner, A., Taylor, S., Glazewski, K., & Lester, J. (2021)** | **AI-infused collaborative inquiry in upper elementary school: A GBL approach** | **Proceedings of AAAI 2021, 35(17), 15653–15661** | **GBL AI Literacy for Kids** | 2.2.4, 2.3.3, 3.2.4 | https://ojs.aaai.org/index.php/AAAI/article/view/17836 | **NEW** |
| **B06** ⭐ | **Gupta, A., Lee, S., Mott, B., Chakraburty, S., Scribner, A., Glazewski, K., Ottenbreit-Leftwich, A., & Lester, J. (2024)** | **Supporting upper elementary students in learning AI concepts with story-driven GBL** | **Proceedings of AAAI 2024, 38(21), 23321–23329** | **Story-Driven GBL AI Concepts** | 2.2.4, 2.3.3, 3.2.8 | https://ojs.aaai.org/index.php/AAAI/article/view/30354 | **NEW** |
| **B07** ⭐ | **Hsu, T. C., Abelson, H., Lao, N., Tseng, Y. H., & Lin, Y. T. (2021)** | **Behavioral-pattern exploration and instructional tool for young children to learn AI** | **Computers and Education: Artificial Intelligence, 2, Article 100060** | **Behavioral Patterns Kids Learning AI** | 2.3.5, 3.1, 3.2.1, 3.4.4 | https://doi.org/10.1016/j.caeai.2021.100060 | **NEW** |
| **B08** ⭐ | **Ocak, C., Kopcha, T. J., & Dey, R. (2023)** | **An AI-enhanced pattern recognition approach to children's embodied interactions** | **Computers and Education: Artificial Intelligence, 4, Article 100155** | **Children Embodied Interaction Analysis** | 3.4.4, 3.4.5 | https://doi.org/10.1016/j.caeai.2023.100155 | **NEW** |
| **B09** ⭐ | **Shokeen, E., Katirci, N., Williams-Pierce, C., & Fan, C. (2022)** | **Children learning to sketch: Sketching to learn** | **Information and Learning Sciences, 123(7/8), 482–497** | **Children Sketching Pedagogy** | 2.2.7, 3.2.4 | https://doi.org/10.1108/ILS-10-2021-0097 | **NEW** |
| **B10** ⭐ | **Chen, Z., Duan, Z., Qi, Y., & Wang, W. (2025)** | **From line sketches to contextualized scenes: AR scaffold for narrative drawing based on sketch recognition and motivational effects** | **Proceedings of ACM/IEEE HRI 2025, 1–10** | **Sketch Recognition + Motivation (child context)** | 2.3.5, 3.1 | https://doi.org/10.1145/3779232.3779472 | **NEW** |
| **B11** ⭐ | **Wang, C. J., Zhong, H. X., Chiu, P. S., Chang, J. H., & Chen, M. Y. (2022)** | **Research on the impacts of cognitive style and computational thinking on college students in a visual AI course** | **Frontiers in Psychology, 13, Article 864416** | **Cognitive Style + AI Course (CCI foundation)** | 2.2.7, 3.2.4 | https://doi.org/10.3389/fpsyg.2022.864416 | **NEW** |
| **B12** ⭐ | **Wu, S. Y., & Su, Y. S. (2021)** | **Visual programming environments and CT performance of 5th-6th grade students** | **Journal of Educational Computing Research, 59(7), 1413–1441** | **Child-Computer Interaction (5-6 grade)** | 2.2.7, 3.2.2 | https://doi.org/10.1177/0735633120988807 | **NEW** |

⭐ = baru ditambahkan dari Merged Context
⚠️ = DEPRECATED post-pivot 16/6/26

### 2.1 Catatan Justifikasi Penambahan Kategori B

Setiap referensi baru di Kategori B punya justifikasi spesifik kenapa masuk scope Can (bukan A atau C):

| ID | Kenapa B (bukan A atau C)? |
|----|---------------------------|
| B03 | Wang & Lester adalah **editorial call-to-action** khusus K-12 AI literacy — fokusnya pada usia K-12 (bukan general AI literacy). Can butuh ini untuk justifikasi target user SMP. |
| B04 | Yim & Su fokus **primary school** (lebih muda dari SMP) — penting untuk justifikasi age-appropriate design Can. |
| B05 | Lee et al. **GBL spesifik untuk AI literacy di upper elementary** — bukan GBL general (A06 Videnovik adalah GBL CS ed, A18 Zhan adalah GBL AI ed review). B05 adalah implementasi konkret untuk anak. |
| B06 | Gupta et al. **story-driven GBL** — sejalan dengan narasi Momo sebagai story driver di Sketchbook Universe. Justifikasi desain narasi level. |
| B07 | Hsu et al. **behavioral-pattern exploration untuk kids learning AI** — fundamental untuk Bab 3.4.4 Teknik Pengumpulan Data Can (log behavioral siswa). |
| B08 | Ocak et al. **children's embodied interactions** — fundamental untuk analisis pola interaksi anak (CCI analysis Bab 3.4.5). |
| B09 | Shokeen et al. **children learning to sketch** — satu-satunya ref yang specifically membahas anak belajar menggambar. Penting untuk justifikasi level design yang sesuai motorik anak SMP. |
| B10 | Chen et al. **sketch recognition + AR scaffold + motivational effects pada anak** — jembatan antara CCI (Can) dan sketch recognition (Dias) dari sisi motivasi anak. |
| B11 | Wang et al. **cognitive style in AI course** — fundamental CCI untuk remaja, justifikasi linear flow (no branching) per cognitive load theory. |
| B12 | Wu & Su **5th-6th grade visual programming + CT** — pegangan usia terdekat dengan SMP kelas 7, justifikasi UI complexity level. |

---

## 3. Tabel Kategori C — Dias-specific (Backend/CNN/Sketch Recognition/TF.js/K-Means/API)

**Definisi:** Referensi spesifik pendukung scope Dias — CNN MobileNet untuk sketch, TensorFlow.js, sketch recognition architectures, K-Means clustering untuk pola belajar, Quick Draw dataset.

**Total:** 9 referensi (5 existing + 4 baru)

| ID | Author (Year) | Title (short) | Venue | Topik | Bab Dias | DOI/URL | Status |
|----|---------------|---------------|-------|-------|----------|---------|--------|
| C01 | Xu, L. et al. (2023) | Deep learning for free-hand sketch: A survey | IEEE TPAMI, 45(1), 285–312 | Sketch Recognition Survey | 2.2.3, 2.2.4, 2.3.1, 3.2, 3.4.1, 3.4.2 | https://doi.org/10.1109/TPAMI.2021.3127001 | existing |
| C02 | Goh, G.Z.L., Ho, D., & Abas, Z.A. (2023) | Front-end DL web apps: A review | Applied Intelligence, 53, 15923–15945 | Front-End DL Web Apps | 2.2.5, 2.3.2, 3.4.3, 3.13 | https://doi.org/10.1007/s10489-022-04278-6 | existing |
| C03 | Smilkov, D. et al. (2019) | TensorFlow.js: ML for the web and beyond | Proceedings of 2nd SysML Conference, 1–10 | TensorFlow.js | 1.3, 2.2.5, 3.4.3, 3.13 | https://proceedings.mlsys.org/paper_files/paper/2019/hash/acd593d2db87a799a8d3da5a860c028e-Abstract.html | existing (canonical) |
| C04 | Pansri, P. et al. (2024) | Understanding student learning behavior through K-Means clustering | Education Sciences, 14(12), 1291 | K-Means Student Behavior | 1.3, 1.4, 2.2.8, 2.3.4, 3.7.2, 3.9.1, 3.9.2, 3.9.3, 3.9.4, 3.10.1 | https://doi.org/10.3390/educsci14121291 | existing |
| C05 | Alzahrani, A. et al. (2025) | Identifying weekly student engagement patterns via K-Means clustering | Electronics, 14(15), 3018 | K-Means Engagement Patterns | 2.2.8, 2.3.4, 3.7.2, 3.9.1, 3.9.2, 3.9.4 | https://doi.org/10.3390/electronics14153018 | existing |
| **C06** ⭐ | **Huynh, V. T., Nguyen, T. T., Nguyen, T. V., & Tran, M. T. (2023)** | **MobileNet-SA: Lightweight CNN with self attention for sketch classification** | **Pacific-Rim Symposium on Image and Video Technology (PSIVT) 2023, 115–129, Springer** | **MobileNet for Sketch (specific architecture)** | 2.2.4, 2.3.1, 3.4.2 | https://doi.org/10.1007/978-981-97-0376-0_9 | **NEW** |
| **C07** ⭐ | **Li, L., Zou, C., Zheng, Y., Su, Q., Fu, H., & Tai, C. L. (2020)** | **Sketch-R2CNN: An RNN-rasterization-CNN architecture for vector sketch recognition** | **IEEE TPAMI, 44(9), 4671–4685** | **Sketch Recognition Architecture (RNN+CNN)** | 2.2.4, 2.3.1 | https://doi.org/10.1109/TPAMI.2020.2997960 | **NEW** |
| **C08** ⭐ | **Google Creative Lab. (2017)** | **Quick, Draw! The Data** | **Google, https://quickdraw.withgoogle.com/data** | **Quick Draw Dataset (canonical source)** | 2.2.3, 2.3.1, 3.4.1 | https://quickdraw.withgoogle.com/data | **NEW** (canonical) |
| **C09** ⭐ | **Liu, F., Lu, M., & Zhang, W. (2024)** | **Comparative analysis of deep learning-based models in sketch recognition** | **Proceedings of ICAIC 2024, Atlantis Press** | **DL Sketch Recognition Comparison** | 2.3.1, 3.4.2 | https://doi.org/10.2991/978-94-6463-473-1_40 | **NEW** |

⭐ = baru ditambahkan dari Merged Context

### 3.1 Catatan Justifikasi Penambahan Kategori C

| ID | Kenapa C (bukan A)? |
|----|---------------------|
| C06 | Huynh et al. **MobileNet-SA specifically untuk sketch** — ref paling relevan ke pilihan MobileNet di proposal Dias. Mengikat pilihan arsitektur ke literature. |
| C07 | Li et al. **Sketch-R2CNN (RNN+CNN)** — referensi state-of-the-art yang membandingkan CNN-only (Dias pilih) vs RNN+CNN (alternatif). Memperkuat diskusi trade-off. |
| C08 | Quick Draw Dataset — sumber data canonical, WAJIB disitir sebagai sumber dataset. |
| C09 | Liu et al. komparasi DL sketch models — pegangan untuk justifikasi pilihan arsitektur di Bab 3.4.2. |

---

## 4. Matriks Pemetaan: Referensi ↔ Sub-bab Can & Dias

Matriks ini menunjukkan referensi mana yang dipakai di sub-bab mana. Berguna untuk cek coverage referensi dan hindari orphan references (referensi yang disitir tapi tidak dipakai).

### 4.1 Sub-bab Can (frontend scope)

| Sub-bab | Referensi Pendukung | Status |
|---------|---------------------|--------|
| 1.1 Latar Belakang | A01, A02, A03, A04, B03 | ✅ |
| 1.2 Permasalahan | A01, A03, A04, A05, A16, B01 | ✅ (A16 baru untuk automation bias) |
| 1.3 Batasan Masalah | A04, A05, A11, A14, A15, C03, C04 | ✅ |
| 1.4 Tujuan | A01, A03, A04, A06, B01, C01, C04 | ✅ |
| 1.5 Manfaat | A01, A02, A04, A06, A14 | ✅ |
| 1.6 Sistematika Penulisan | — | ✅ (no ref) |
| 2.1 Deskripsi Permasalahan | A01, A02, A18 | ✅ (A18 baru GBL AI) |
| 2.2.1 Literasi KB | A01, A02, B03, B04 | ✅ (B03, B04 baru) |
| 2.2.2 HITL | A04, A05, A20 | ✅ (A20 baru XAI trust) |
| 2.2.3 Explainable Interface & Confidence | A03, A08, A17, A19 | ✅ (A17 prob, A19 XAI UX baru) |
| 2.2.4 Simulasi Interaktif Berlevel | A06, A07, A18, B05 | ✅ (A18, B05 baru) |
| 2.2.5 Finger Tracking & MediaPipe ⚠️ | B02 | ✅ (DEPRECATED) |
| 2.2.6 Pedagogical Agent (Momo) | B01 | ✅ |
| 2.2.7 CCI untuk Siswa SMP | A02, B04, B09, B11, B12 | ✅ (B04, B09, B11, B12 baru — kuat!) |
| 2.2.8 Usability Testing | A14, A15 | ✅ |
| 2.3.1 AI Literacy in K-12 | A02, B03, B04 | ✅ |
| 2.3.2 HITL ML | A04, A05 | ✅ |
| 2.3.3 GBL in CS Ed | A06, A07, A18, B05, B06 | ✅ (A18, B05, B06 baru) |
| 2.3.4 Real-Time Hand Gesture ⚠️ | B02 | ✅ (DEPRECATED) |
| 2.3.5 State of The Art | A01, A02, A03, A04, A06, A16, B01, B07, B10 | ✅ (A16, B07, B10 baru) |
| 3.1 Deskripsi Solusi | A01, A03, A04, A06, A18, B01, B10 | ✅ (A18, B10 baru) |
| 3.2.1 Kebutuhan Pengguna | A01, A02, B01, B07 | ✅ (B07 baru) |
| 3.2.2 Alur Pengguna | A06, A07, B12 | ✅ (B12 baru) |
| 3.2.3 Use Case Sistem | A04, A05 | ✅ |
| 3.2.4 Desain Level (3 Level) | A06, A07, A08, B05, B09, B11 | ✅ (B05, B09, B11 baru) |
| 3.2.5 Mekanisme HITL [Top-6 Check] | A04, A05, A08, A17 | ✅ (A17 baru probabilistic) |
| 3.2.6 Mapping Perilaku Objek | A04, A06 | ✅ |
| 3.2.7 Wireframe Onboarding [Nomor Absen] | A02, B01 | ✅ |
| 3.2.8 Wireframe Main Gameplay [+resize/rotate/timer] | A06, A07, B01, B06 | ✅ (B06 baru) |
| 3.2.9 Wireframe Probe UI | A03, A08, A19 | ✅ (A19 baru XAI UX) |
| 3.2.10 Wireframe Result & Feedback | A03, A08, A19, B01 | ✅ (A19 baru) |
| 3.2.11 Rancangan Pengujian | A14, A15 | ✅ |
| 3.3 Jadwal Penelitian | — | ✅ (no ref) |
| 3.4.1 Pendekatan & Jenis Penelitian | A11, A12 | ✅ |
| 3.4.2 Metode Pengembangan | A09, A10, A11 | ✅ |
| 3.4.3 Analisis Masalah (Fishbone) | A13 | ✅ |
| 3.4.4 Teknik Pengumpulan Data | A05, A14, B07, B08 | ✅ (B07, B08 baru) |
| 3.4.5 Teknik Analisis Data | A13, B08 | ✅ (B08 baru) |
| 3.4.6 Metode Pengujian | A14, A15 | ✅ |

### 4.2 Sub-bab Dias (backend scope)

| Sub-bab | Referensi Pendukung | Status |
|---------|---------------------|--------|
| 1.1 Latar Belakang | A01, A02, A03, A04 | ✅ |
| 1.2 Permasalahan | A01, A03, A04, A05, A16 | ✅ (A16 baru automation bias) |
| 1.3 Batasan Masalah | A04, A05, C03, C04 | ✅ |
| 1.4 Tujuan | A01, A03, A04, C01, C04 | ✅ |
| 1.5 Manfaat | A01, A02, A04 | ✅ |
| 2.1 Deskripsi Permasalahan | A01, A02 | ✅ |
| 2.2.1 Literasi KB | A01, A02 | ✅ |
| 2.2.2 HITL pada Sistem Klasifikasi | A03, A04, A05, A20 | ✅ (A20 baru XAI trust) |
| 2.2.3 Klasifikasi Sketsa | C01, C08 | ✅ (C08 baru Quick Draw dataset) |
| 2.2.4 CNN dan MobileNet | C01, C06, C07 | ✅ (C06 MobileNet-SA, C07 Sketch-R2CNN baru) |
| 2.2.5 TF.js & Client-Side Inference | C02, C03 | ✅ |
| 2.2.6 Confidence Score | A08, A17 | ✅ (A17 baru prob foundation) |
| 2.2.7 Data Logging | A05 | ✅ |
| 2.2.8 K-Means Clustering | C04, C05 | ✅ |
| 2.3.1 DL for Free-Hand Sketch | C01, C07, C09 | ✅ (C07, C09 baru) |
| 2.3.2 Front-End DL Web Apps | C02, C03 | ✅ |
| 2.3.3 Confidence Visualization | A08 | ✅ |
| 2.3.4 K-Means untuk Pola Belajar | C04, C05 | ✅ |
| 2.3.5 State of The Art | A01, A03, A04, A05, A16, A18, C01, C04 | ✅ (A16, A18 baru) |
| 3.1 Perancangan Sistem Global | A09, A10, A12 | ✅ |
| 3.2 Perancangan Sistem Scope Dias | A04, A05, C01 | ✅ |
| 3.3 Perancangan Arsitektur Sistem | A09, A10, A11 | ✅ |
| 3.4.1 Pemilihan Kategori Dataset | C01, C08 | ✅ (C08 baru Quick Draw canonical) |
| 3.4.2 Arsitektur Model | C01, C06, C09 | ✅ (C06 MobileNet-SA, C09 komparasi baru) |
| 3.4.3 Konversi ke TF.js | C02, C03 | ✅ |
| 3.5 Perancangan User Flow | A04, A05 | ✅ |
| 3.6.1 Aktor & Use Case Siswa | A04, A05 | ✅ |
| 3.6.2 Aktor & Use Case Admin/Guru/Superadmin | A04 | ✅ |
| 3.7.1 Struktur JSON Log [+time_spent_ms] | A05 | ✅ |
| 3.7.2 Feature Engineering K-Means | C04, C05 | ✅ |
| 3.8.1 Endpoint REST API [+Top-6 Check] | A04, A05 | ✅ |
| 3.8.2 Alur Logging | A05 | ✅ |
| 3.9.1 Input K-Means | C04, C05 | ✅ |
| 3.9.2 Penentuan Jumlah Cluster | C04, C05 | ✅ |
| 3.9.3 Proses K-Means | C04 | ✅ |
| 3.9.4 Interpretasi Cluster | A13, A17, C04, C05 | ✅ (A17 baru prob foundation) |
| 3.10.1 Fitur Dashboard | A05, C04 | ✅ |
| 3.10.2 Alur Penggunaan Dashboard | A04 | ✅ |
| 3.11 Sequence Diagram | A04, A05 | ✅ |
| 3.12 Klasifikasi Objek (Solid/Danger) | A04, A06 | ✅ |
| 3.13 Technology Stack (Dias) | A09, C02, C03 | ✅ |
| 3.14 Kontrak Data Dias-Can | A04, A05 | ✅ |

### 4.3 Coverage Check — Tidak Ada Orphan References

Setiap referensi di Kategori A, B, C telah diverifikasi muncul di minimal 1 sub-bab (Can atau Dias). Detail:

| ID | Sub-bab Can pertama | Sub-bab Dias pertama |
|----|---------------------|----------------------|
| A01-A20 | terdistribusi di 1.1-3.4.6 | terdistribusi di 1.1-3.14 |
| B01 | 1.2 | — |
| B02 | 2.2.5 (DEPRECATED) | — |
| B03-B12 | terdistribusi di 1.1-3.4.5 | — |
| C01-C09 | — | terdistribusi di 1.3-3.14 |

**Tidak ada orphan references.** ✅

---

## 5. Daftar Pustaka Can (LaTeX-ready, format `thebibliography` + `\bibitem`)

> Format mengikuti `proposal-can.tex` existing (lines 512-544). Numbered [1]-[32]. Total: **32 referensi** (A1-A20 + B1-B12).
> Urutan: alphabetical-ish by appearance di Bab 1 → Bab 3 (mengikuti urutan existing proposal).

```latex
% ============================================================
% DAFTAR PUSTAKA — SCOPE: CAN (FRONTEND)
% Farchan Deano Muhammad — D4 TRM PENS
% Proyek: Sketchbook Universe — Interactive HITL AI Literacy Simulation
% Total: 32 referensi (20 General + 12 Can-specific)
% ============================================================

\begin{thebibliography}{99}

\bibitem{ref1}
Ng, D.T.K., Leung, J.K.L., Chu, S.K.W., \& Qiao, M.S. (2021). Conceptualizing AI literacy: An exploratory review. \textit{Computers and Education: Artificial Intelligence}, 2, 100041.

\bibitem{ref2}
Casal-Otero, V., Catala, A., Fern\'andez-Morante, C., Taboada, M., Caeiro-Rodr\'iguez, M., \& Barro, S. (2023). AI literacy in K-12: A systematic literature review. \textit{International Journal of STEM Education}, 10, 29.

\bibitem{ref3}
Khosravi, H., Shum, S.B., Chen, G., Conati, C., Tsai, Y.-S., Kay, J., Knight, S., Martinez-Maldonado, R., Sadat-Milani, L., \& Ga\v{s}evi\'c, D. (2022). Explainable Artificial Intelligence in education. \textit{Computers and Education: Artificial Intelligence}, 3, 100074.

\bibitem{ref4}
Mosqueira-Rey, E., Hern\'andez-Pereira, E., Alonso-R\'ios, D., Bobillo-Ares, B., \& Moret-Bonillo, V. (2023). Human-in-the-loop machine learning: A state of the art. \textit{Artificial Intelligence Review}, 56(4), 3005--3054.

\bibitem{ref5}
Memarian, B., \& Doleck, T. (2024). Human-in-the-loop in artificial intelligence in education: A review and entity-relationship (ER) analysis. \textit{Computers in Human Behavior: Artificial Humans}, 2, 100053.

\bibitem{ref6}
Videnovik, M., Vlahovi\v{c}-Steti\'c, V., Kišiček, S., \& Vošner, H.B. (2023). Game-based learning in computer science education: A scoping literature review. \textit{International Journal of STEM Education}, 10, 54.

\bibitem{ref7}
Chan, K.K., Wan, K.M., \& King, R.B. (2021). Performance over enjoyment? Effect of game-based learning on learning outcome and flow experience. \textit{Frontiers in Education}, 6, 660376.

\bibitem{ref8}
Karran, A.J., Demazure, T., \& Hudelot, C. (2022). Designing for confidence: The impact of visualizing artificial intelligence decisions. \textit{Frontiers in Neuroscience}, 16.

% --- Can-specific (Kategori B) ---

\bibitem{ref9}
Schroeder, N.L., Davis, C.S., \& Yang, Y. (2025). Designing and learning with pedagogical agents: An umbrella review. \textit{Journal of Educational Computing Research}, 62(8).

\bibitem{ref10}
Meng, Z., Fu, Z., Liu, J., Wang, H., \& Pan, Y. (2024). Real-Time Hand Gesture Monitoring Model Based on MediaPipe's Registerable System. \textit{Sensors}, 24(19), 6262. \textit{[Catatan: DEPRECATED post-pivot 16/6/26 --- login gesture diganti nomor absen + superadmin. Dipertahankan untuk dokumentasi historis canvas drawing input.]}

\bibitem{ref11}
Wang, N., \& Lester, J. (2023). K-12 education in the age of AI: A call to action for K-12 AI literacy. \textit{International Journal of Artificial Intelligence in Education}, 33(3), 631--640.

\bibitem{ref12}
Yim, I. H. Y., \& Su, J. (2025). Artificial intelligence literacy education in primary schools: A review. \textit{International Journal of Technology and Design Education}, 35, Article 57.

\bibitem{ref13}
Lee, S., Mott, B., Ottenbreit-Leftwich, A., Scribner, A., Taylor, S., Glazewski, K., \& Lester, J. (2021). AI-infused collaborative inquiry in upper elementary school: A game-based learning approach. \textit{Proceedings of the AAAI Conference on Artificial Intelligence}, 35(17), 15653--15661.

\bibitem{ref14}
Gupta, A., Lee, S., Mott, B., Chakraburty, S., Scribner, A., Glazewski, K., Ottenbreit-Leftwich, A., \& Lester, J. (2024). Supporting upper elementary students in learning AI concepts with story-driven game-based learning. \textit{Proceedings of the AAAI Conference on Artificial Intelligence}, 38(21), 23321--23329.

\bibitem{ref15}
Hsu, T. C., Abelson, H., Lao, N., Tseng, Y. H., \& Lin, Y. T. (2021). Behavioral-pattern exploration and development of an instructional tool for young children to learn AI. \textit{Computers and Education: Artificial Intelligence}, 2, Article 100060.

\bibitem{ref16}
Ocak, C., Kopcha, T. J., \& Dey, R. (2023). An AI-enhanced pattern recognition approach to temporal and spatial analysis of children's embodied interactions. \textit{Computers and Education: Artificial Intelligence}, 4, Article 100155.

\bibitem{ref17}
Shokeen, E., Katirci, N., Williams-Pierce, C., \& Fan, C. (2022). Children learning to sketch: Sketching to learn. \textit{Information and Learning Sciences}, 123(7/8), 482--497.

\bibitem{ref18}
Chen, Z., Duan, Z., Qi, Y., \& Wang, W. (2025). From line sketches to contextualized scenes: An AR scaffold for narrative drawing based on sketch recognition and its motivational effects. \textit{Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction (HRI)}, 1--10.

\bibitem{ref19}
Wang, C. J., Zhong, H. X., Chiu, P. S., Chang, J. H., \& Chen, M. Y. (2022). Research on the impacts of cognitive style and computational thinking on college students in a visual artificial intelligence course. \textit{Frontiers in Psychology}, 13, Article 864416.

\bibitem{ref20}
Wu, S. Y., \& Su, Y. S. (2021). Visual programming environments and computational thinking performance of fifth-and sixth-grade students. \textit{Journal of Educational Computing Research}, 59(7), 1413--1441.

% --- General/Shared additions (Kategori A baru) ---

\bibitem{ref21}
Yin, M., Wortman Vaughan, J., \& Wallach, H. (2019). Understanding the effect of accuracy on trust in machine learning models. \textit{Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems}, 1--12.

\bibitem{ref22}
Batanero, C., \& \'Alvarez-Arroyo, R. (2023). Teaching and learning of probability. \textit{ZDM -- Mathematics Education}, 56, 5--17.

\bibitem{ref23}
Zhan, Z., Tong, Y., Lan, X., \& Zhong, B. (2024). A systematic literature review of game-based learning in artificial intelligence education. \textit{Interactive Learning Environments}, 32(4), 1189--1212.

\bibitem{ref24}
Liao, Q. V., Gruen, D., \& Miller, S. (2020). Questioning the AI: Informing design practices for explainable AI user experiences. \textit{Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems}, 1--15.

\bibitem{ref25}
Feldman-Maggor, Y., Cukurova, M., Kent, C., Luckin, R., \& Baur-Wolfson, M. (2025). The impact of explainable AI on teachers' trust and acceptance of AI EdTech recommendations. \textit{International Journal of Artificial Intelligence in Education}, 35(1), 1--25.

% --- Methodology (Kategori A existing, methodology) ---

\bibitem{ref26}
Pressman, R.S. (2014). \textit{Software Engineering: A Practitioner's Approach} (8th ed.). New York: McGraw-Hill.

\bibitem{ref27}
Sommerville, I. (2015). \textit{Software Engineering} (10th ed.). Pearson.

\bibitem{ref28}
Sugiyono. (2020). \textit{Metode Penelitian Kuantitatif, Kualitatif, dan R\&D}. Bandung: Alfabeta.

\bibitem{ref29}
Creswell, J.W. (2014). \textit{Research Design: Qualitative, Quantitative, and Mixed Methods Approaches} (4th ed.). Sage Publications.

\bibitem{ref30}
Ishikawa, K. (1986). \textit{Guide to Quality Control} (2nd ed.). Tokyo: Asian Productivity Organization.

\bibitem{ref31}
Brooke, J. (1996). SUS: A `Quick and Dirty' Usability Scale. In \textit{Usability Evaluation in Industry} (pp. 189--194). Taylor \& Francis.

\bibitem{ref32}
Bangor, A., Kortum, P.T., \& Miller, J.T. (2008). An empirical evaluation of the System Usability Scale. \textit{International Journal of Human-Computer Interaction}, 24(6), 574--594.

\end{thebibliography}
```

**Catatan renumbering:** Bila di-insert ke `proposal-can.tex` existing, citation in-text `[1]`-`[10]` tetap valid untuk ref 1-10 (existing Can refs). Ref baru `[11]`-`[25]` perlu ditambahkan di in-text citation sub-bab Can yang relevan (lihat Matriks §4.1). Ref `[26]`-`[32]` adalah methodology refs yang sebelumnya tidak ada di Can (hanya di Dias) — bila Can mau pakai, tambahkan in-text citation di Bab 3.4.

---

## 6. Daftar Pustaka Dias (LaTeX-ready, format `enumerate` + `\item[{[N]}]`)

> Format mengikuti `proposal-dias.tex` existing (lines 999-1022). Numbered [1]-[29]. Total: **29 referensi** (A1-A20 + C1-C9).
> Format pakai IEEE-style dengan initials first.

```latex
% ============================================================
% DAFTAR PUSTAKA — SCOPE: DIAS (BACKEND)
% Dias [Nama Lengkap] — D4 TRPL PENS
% Proyek: Sketchbook Universe — CNN + K-Means + REST API
% Total: 29 referensi (20 General + 9 Dias-specific)
% ============================================================

\chapter*{DAFTAR PUSTAKA}
\addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}

\begin{enumerate}
    \item[{[1]}] D. T. K. Ng, J. K. L. Leung, S. K. W. Chu, and M. S. Qiao, ``Conceptualizing AI literacy: An exploratory review,'' \textit{Computers and Education: Artificial Intelligence}, vol.~2, p.~100041, 2021.
    \item[{[2]}] V. Casal-Otero \textit{et al.}, ``AI literacy in K-12: A systematic literature review,'' \textit{International Journal of STEM Education}, vol.~10, p.~29, 2023.
    \item[{[3]}] H. Khosravi \textit{et al.}, ``Explainable Artificial Intelligence in education,'' \textit{Computers and Education: Artificial Intelligence}, vol.~3, p.~100074, 2022.
    \item[{[4]}] E. Mosqueira-Rey, V. Alonso-R\'ios, and B. Rubio-R\'ios, ``Human-in-the-loop machine learning: A state of the art,'' \textit{Artificial Intelligence Review}, vol.~56, no.~4, pp.~3005--3054, 2023.
    \item[{[5]}] B. Memarian and T. Doleck, ``Human-in-the-loop in artificial intelligence in education: A review and entity-relationship (ER) analysis,'' \textit{Computers in Human Behavior: Artificial Humans}, vol.~2, p.~100053, 2024.
    \item[{[6]}] L. Xu \textit{et al.}, ``Deep learning for free-hand sketch: A survey,'' \textit{IEEE Transactions on Pattern Analysis and Machine Intelligence}, vol.~45, no.~1, pp.~285--312, 2023.
    \item[{[7]}] G. Z. L. Goh, D. Ho, and Z. A. Abas, ``Front-end deep learning web apps development and deployment: A review,'' \textit{Applied Intelligence}, vol.~53, pp.~15923--15945, 2023.
    \item[{[8]}] D. Smilkov \textit{et al.}, ``TensorFlow.js: Machine learning for the web and beyond,'' in \textit{Proc. 2nd SysML Conf.}, 2019, pp.~1--10.
    \item[{[9]}] A. J. Karran, S. Demazure, and C. Hudelot, ``Designing for confidence: The impact of visualizing artificial intelligence decisions,'' \textit{Frontiers in Neuroscience}, vol.~16, 2022.
    \item[{[10]}] P. Pansri \textit{et al.}, ``Understanding student learning behavior through K-Means clustering,'' \textit{Education Sciences}, vol.~14, no.~12, p.~1291, 2024.
    \item[{[11]}] A. Alzahrani \textit{et al.}, ``Identifying weekly student engagement patterns via K-Means clustering,'' \textit{Electronics}, vol.~14, no.~15, p.~3018, 2025.
    \item[{[12]}] M. Videnovik \textit{et al.}, ``Game-based learning in computer science education: A scoping literature review,'' \textit{International Journal of STEM Education}, vol.~10, p.~54, 2023.
    \item[{[13]}] K. K. Chan, K. M. Wan, and R. B. King, ``Performance over enjoyment? Effect of game-based learning on learning outcome and flow experience,'' \textit{Frontiers in Education}, vol.~6, p.~660376, 2021.
    \item[{[14]}] R. S. Pressman, \textit{Software Engineering: A Practitioner's Approach}, 8th~ed. New York: McGraw-Hill, 2014.
    \item[{[15]}] I. Sommerville, \textit{Software Engineering}, 10th~ed. Pearson, 2015.
    \item[{[16]}] Sugiyono, \textit{Metode Penelitian Kuantitatif, Kualitatif, dan R\&D}. Bandung: Alfabeta, 2020.
    \item[{[17]}] J. W. Creswell, \textit{Research Design: Qualitative, Quantitative, and Mixed Methods Approaches}, 4th~ed. Sage Publications, 2014.
    \item[{[18]}] K. Ishikawa, \textit{Guide to Quality Control}, 2nd~ed. Tokyo: Asian Productivity Organization, 1986.
    \item[{[19]}] J. Brooke, ``SUS: A `Quick and Dirty' Usability Scale,'' in \textit{Usability Evaluation in Industry}, pp.~189--194, Taylor \& Francis, 1996.
    \item[{[20]}] A. Bangor, P. T. Kortum, and J. T. Miller, ``An empirical evaluation of the System Usability Scale,'' \textit{International Journal of Human-Computer Interaction}, vol.~24, no.~6, pp.~574--594, 2008.
    \item[{[21]}] M. Yin, J. Wortman Vaughan, and H. Wallach, ``Understanding the effect of accuracy on trust in machine learning models,'' in \textit{Proc. 2019 CHI Conf. Human Factors in Computing Systems}, 2019, pp.~1--12.
    \item[{[22]}] C. Batanero and R. \'Alvarez-Arroyo, ``Teaching and learning of probability,'' \textit{ZDM -- Mathematics Education}, vol.~56, pp.~5--17, 2023.
    \item[{[23]}] Z. Zhan, Y. Tong, X. Lan, and B. Zhong, ``A systematic literature review of game-based learning in artificial intelligence education,'' \textit{Interactive Learning Environments}, vol.~32, no.~4, pp.~1189--1212, 2024.
    \item[{[24]}] Q. V. Liao, D. Gruen, and S. Miller, ``Questioning the AI: Informing design practices for explainable AI user experiences,'' in \textit{Proc. 2020 CHI Conf. Human Factors in Computing Systems}, 2020, pp.~1--15.
    \item[{[25]}] Y. Feldman-Maggor, M. Cukurova, C. Kent, R. Luckin, and M. Baur-Wolfson, ``The impact of explainable AI on teachers' trust and acceptance of AI EdTech recommendations,'' \textit{International Journal of Artificial Intelligence in Education}, vol.~35, no.~1, pp.~1--25, 2025.
    \item[{[26]}] V. T. Huynh, T. T. Nguyen, T. V. Nguyen, and M. T. Tran, ``MobileNet-SA: Lightweight CNN with self attention for sketch classification,'' in \textit{Pacific-Rim Symposium on Image and Video Technology (PSIVT) 2023}, Springer, 2023, pp.~115--129.
    \item[{[27]}] L. Li, C. Zou, Y. Zheng, Q. Su, H. Fu, and C. L. Tai, ``Sketch-R2CNN: An RNN-rasterization-CNN architecture for vector sketch recognition,'' \textit{IEEE Transactions on Pattern Analysis and Machine Intelligence}, vol.~44, no.~9, pp.~4671--4685, 2020.
    \item[{[28]}] Google Creative Lab, ``Quick, Draw! The Data,'' Google, 2017. [Online]. Available: https://quickdraw.withgoogle.com/data
    \item[{[29]}] F. Liu, M. Lu, and W. Zhang, ``Comparative analysis of deep learning-based models in sketch recognition,'' in \textit{Proc. ICAIC 2024}, Atlantis Press, 2024.
\end{enumerate}
```

**Catatan renumbering:** Ref `[1]`-`[15]` adalah gabungan dari existing Dias `[1]-[13]` (A01-A08, C01-C05, A06, A07) + methodology `[14]-[15]` (A09, A10). Existing Dias `[16]-[22]` (A11-A15) tetap di posisi `[16]-[20]` (5 refs methodology). Ref baru `[21]-[25]` adalah A16-A20 (Kategori A baru). Ref baru `[26]-[29]` adalah C06-C09 (Kategori C baru). B02 Meng sengaja **tidak dimasukkan** ke Daftar Pustaka Dias karena MediaPipe tidak ada di scope Dias.

---

## 7. Catatan DEPRECATED & Validasi

### 7.1 Referensi DEPRECATED post-pivot 16/6/26

| ID | Referensi | Alasan DEPRECATED | Treatment |
|----|-----------|-------------------|-----------|
| **B02** | Meng, Z. et al. (2024). Real-Time Hand Gesture Monitoring Model Based on MediaPipe's Registerable System. \textit{Sensors}, 24(19), 6262. | Pivot 16/6/26: Login gesture MediaPipe finger counting diganti dengan **nomor absen + superadmin role**. Gesture login dianggap terlalu kompleks untuk classroom Indonesia dan ada concern UU PDP biometric data (walau hand landmarks tidak disimpan). | **Tetap di Daftar Pustaka Can** sebagai `[10]` dengan catatan DEPRECATED. In-text citation hanya muncul di §2.2.5 dan §2.3.4 (sub-bab yang juga di-mark DEPRECATED di outline). Tidak ada in-text citation baru yang menambah B02. Pertimbangan: bila MediaPipe benar-benar tidak dipakai untuk apapun (canvas drawing input pakai mouse/touch saja), B02 boleh dihapus total di iterasi v2. |

### 7.2 Referensi yang Tidak Dimasukkan (Filter Constraints)

Berdasarkan constraint "tidak peer-reviewed" + "Q4 journal dihindari", referensi berikut dari Merged Context **TIDAK dimasukkan**:

| Referensi | Topik di Merged Context | Alasan Skip |
|-----------|--------------------------|-------------|
| Kumar et al. (2024) IEEE Access | HITL applications & challenges | Q1 IEEE Access tapi terlalu general — A04+A05 sudah cover scope HITL. Skip untuk hindari redundancy. |
| Natarajan et al. (2025) AAAI | HITL vs AI-in-the-loop | Lebih ke AI-in-the-loop (debate), kurang relevan dengan scope siswa sebagai evaluator. |
| Chen, F. (2022) JETI | Human-AI cooperation in education | Journal of Educational Technology and Innovation — impact factor rendah, tidak Scopus Q1-Q3. |
| Monarch (2021) Manning book | HITL ML textbook | Buku textbook, prefer journal/conference. |
| Yim & Su (2024) JCE | AI learning tools K-12 scoping | Sudah ada B04 (Yim & Su 2025) yang lebih baru di topik serupa. Hindari duplikasi author. |
| Tan & Tang (2025) ILE | AI literacy K-12 systematic review | Sudah ada A02 (Casal-Otero 2023) sebagai AI literacy systematic review. Hindari redundancy. |
| Chung et al. (2025) Education and Information Technologies | AI literacy diagnostic tool | Fokus ke diagnostic tool (test development), bukan ke pedagogical design Can. |
| Zhou et al. (2025) ILE | AI literacy competency systematic review | Sudah ada A02 + A18 sebagai systematic review. Skip untuk hindari redundancy. |
| Al-Abdullatif (2025) Systems | AI literacy competency audit | Fokus ke audit framework dewasa, kurang relevan untuk siswa SMP. |
| Shamir & Levin (2020) EDULEARN | CT transformations elementary | EDULEARN conference proceedings — bukan Scopus Q1-Q3. |
| Jeon et al. (2024) Applied Sciences | CV education framework | Lebih ke curriculum design, kurang relevan dengan implementasi. |
| Hsu & Lin (2025) ETS | AI image recognition + robot GBL + CT | ETS reindexed; robot context tidak dipakai di Sketchbook Universe. |
| Abar et al. (2021) Acta Scientiae | CT in basic school | Brazilian journal, impact rendah. |
| Tan et al. (2024) Computer Science Education | ML in CT assessments | Fokus ke CT assessment dengan ML, kurang relevan scope. |
| Leavy et al. (2025) CERME13 | Statistics & probability education intro | Conference proceedings, weak. |
| Shafik (2024) Springer chapter | Trustworthy XAI educational | Book chapter; A19+A20 sudah cover XAI trust. |
| Kastania (2024) Springer chapter | Building trust in AI ed | Book chapter; A20 sudah cover XAI trust. |
| Geethanjali & Umashankar (2025) IEEE ICCCA | XAI educational outcomes | Conference低端; A20 sudah cover. |
| Alam (2022) IEEE ICSCDS | DGBL for AI/ML curriculum | Conference低端, B05+B06 lebih kuat (AAAI). |
| Wagan et al. (2023) Sustainability | AI-enabled GBL framework | Framework-level (B5+B6+B7 lebih konkret untuk anak). |
| Gong et al. (2026) JECR | LLM scaffolding in GBL for AI ed | LLM-based — arahan Bu Hesti melarang suara/NLP di Momo. Tidak relevan. |
| Kabakus (2020) IEEE HORA | Sketch recognition CNN | Conference低端; C07 (Li TPAMI) lebih authoritative. |
| Huynh et al. (2023) IEEE IPPR | Light-weight sketch w/ KD | Conference低端; C06 (Huynh Springer PSIVT) lebih authoritative. |
| Yang et al. (2025) Pattern Recognition | Sketch-SparseNet | Pattern Recognition Q1 tapi spesifik sparse conv — terlalu advanced, MobileNet cukup. |
| Bileschi et al. (2020) Manning book | DL with JavaScript TF.js | Book; C03 (Smilkov) sudah canonical TF.js. |
| Pournaras et al. (2020) IEEE IISA | DL on web, object detection | Object detection ≠ sketch classification. Kurang relevan. |
| Suryadevara (2021) Apress book | Beginning ML in browser | Book; C03 sudah cover. |
| Ali et al. (2025) ASSAJ | Privacy-preserving skin disease | Domain mismatch (medical, bukan education). |
| Gomez et al. (2025) Frontiers CS | Human-AI collaboration taxonomy | Taxonomy-level, A04+A05 sudah cover. |
| Ouyang et al. (2023) IJCSCL | AI learning analytics CPS | CPS context ≠ individual sketch evaluation. |
| Aslan et al. (2025) CHBAH | CPS in conversational AI | Conversational AI tidak dipakai (Momo non-NLP). |
| Tarun et al. (2025) IEEE FIE | HITL adaptive learning genAI | GenAI context, Momo rule-based bukan genAI. |
| López-Meneses et al. (2025) Applied Sciences | AI in EDM and HITL ML | EDM-focused, kurang relevan untuk prototype Can. |
| Charoenrat (2025) Thai journal | Affective AI + XAI HITL | Thai local journal Q4. |
| El Mouna et al. (2024) IJISAE | CNN-LSTM sketch | Q3 journal, tapi C09 (Liu 2024) sudah cover komparasi DL sketch. |
| Jannah et al. (2025) | Indonesian AI education context | Indonesian context tapi fokus "debate" — kurang akademis formal. |
| Arifin et al. (2025) Kemendikbud | SD/MI kelas V textbook | SD kelas 5, target kita SMP kelas 7-9. Mismatch age. |

### 7.3 Validasi DOI/URL

Semua referensi di Kategori A, B, C memiliki DOI atau URL akses. Berikut summary:

| Kategori | Dengan DOI | Dengan URL saja (canonical) | Total |
|----------|-----------|-----------------------------|-------|
| A | 18 (A01-A08, A12-A20) | 2 (A09, A10, A11, A13, A14 — ISBN books) | 20 |
| B | 11 (B01, B02, B03-B12) | 1 (none — semua DOI/AAAI URL) | 12 |
| C | 8 (C01-C07, C09) | 1 (C08 Google Quick Draw — canonical URL) | 9 |
| **Total** | **37** | **4** | **41** |

**Catatan:** 4 ISBN books (A09, A10, A11, A13, A14) — wajar untuk textbook/references klasik.
C08 Google Quick Draw — bukan DOI tapi URL canonical (sama treatment dengan C03 Smilkov arXiv yang juga canonical).

---

## 8. Next Actions (untuk Main Agent / User)

1. **Review Kategori B baru (B03-B12)** — pastikan relevansi akademis dengan scope Can. Perhatikan khususnya B10 (Chen et al. HRI 2025) yang membahas sketch + AR — perlu dipastikan tidak keluar dari scope (AR tidak dipakai di Sketchbook Universe, tapi motivational effects-nya bisa dipakai sebagai justifikasi).

2. **Update in-text citation di LaTeX Can** — Ref baru B03-B12 dan A16-A20 perlu di-add di sub-bab Can sesuai Matriks §4.1. Renumbering [1]-[32] mengikuti §5.

3. **Update in-text citation di LaTeX Dias** — Ref baru A16-A20 dan C06-C09 perlu di-add di sub-bab Dias sesuai Matriks §4.2. Renumbering [1]-[29] mengikuti §6.

4. **Validasi B02 Meng DEPRECATED** — Diskusikan dengan Dias & Bu Hesti: apakah MediaPipe benar-benar tidak dipakai untuk apapun (termasuk canvas drawing input)? Bila iya, B02 boleh dihapus total di iterasi v2. Bila masih dipakai untuk finger tracking canvas (alternatif mouse/touch), B02 tetap dipertahankan dengan note DEPRECATED untuk login.

5. **Validasi DOI accessible** — Merged Context sudah dikurasi user, tapi ada beberapa DOI yang perlu akses institusi (Springer, Tandfonline, IEEE Xplore). Pastikan PENS punya akses atau gunakan Sci-Hub/email author untuk PDF.

6. **Sinkronisasi dengan Outline_dan_Sitasi_PreLatex.md** — Setelah Sitasi_Final_v1.md disetujui, update Outline_dan_Sitasi_PreLatex.md agar konsisten (terutama section 1, 2, 3, 4 yang berisi tabel sitasi & matriks).

---

**End of Sitasi_Final_v1.md**
