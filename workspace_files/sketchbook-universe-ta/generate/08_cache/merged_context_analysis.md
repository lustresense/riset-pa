# Merged Context Analysis — *Escape the Sketchbook*

> Project: Interactive Human-in-the-Loop AI Playground  
> Author: Farchan Deano Muhammad (Can) — D4 TRM, PENS  
> Document purpose: Consolidated reference from 7 AI conversation backups  
> Generated: 2026-03-04

---

## Per-Backup Summary

### 1. Backup001 — Claude (Lines 1–10256)

**Topic:** Initial concept formation, proposal drafting, and pitch deck creation.

**Key Insights:**
- Defined the core HITL system: student draws → AI classifies (CNN, TF.js client-side) → Top-3 + confidence → Accept/Override → game consequence → log interaction
- Established 3 object categories: **Solid** (platform), **Danger** (reset), **Decorative** (no physics)
- Original target: **SD Kelas 5** (later changed to SMP)
- Created comprehensive context-transfer document (KDKO-style) for handoff to other AI sessions
- Identified key constraints: no pre/post-test, no backend AI, no model retraining, client-side only inference

**Relevance:** ✅ Core system architecture still valid. ❌ SD Kelas 5 target is deprecated (now SMP 7–9). ❌ Title proposals referencing "SD" need updating.

---

### 2. Backup002 — Gemini (Lines 10257–22419)

**Topic:** Scope definition, user flow design, team division, and technical sparring.

**Key Insights:**
- **Target user shift to SMP Kelas 7–9** — prompted by Bu Hesti's feedback that SD students can't grasp probabilistic thinking
- Defined **3 pillars**: Interaksi, Edukasi, Gameplay/Narasi
- Introduced **maskot Momo** as floating AI companion / pedagogical agent / game master
- Established team split: **Can** = Frontend/UX/Game, **Dias** = Backend/AI/Model/Data
- Created V2 User Flow with three decision types: Accept, Correcting, Override
- Discussed logging schema: `top_1_conf`, `chosen_label`, `is_override`, `time_to_decide`
- Identified overlap zone: TF.js integration (model runs in browser = frontend territory but model built by Dias)
- Recommended `modelHelper.js` pattern: Dias exports a `predictImage()` function, Can imports it
- Discussed campus server trade-offs (LAMP stack vs Node.js/Firebase fallback)

**Relevance:** ✅ 3 pillars, Momo concept, team split, and user flow are all current. ✅ SMP target is final. ⚠️ Game engine discussion was still Kaboom vs Phaser at this point (later resolved to Kaplay).

---

### 3. Backup003 — Meta AI #1 (Lines 22420–24233)

**Topic:** Technical research — game engine comparison and QuickDraw architecture analysis.

**Key Insights:**
- **QuickDraw uses RNN (Sketch-RNN)**, not just CNN — processes stroke sequence (vector format), not just pixel images
- Recommendation: **Stick with CNN (MobileNet)** for pixel-based classification — simpler, defensible, and sufficient for PA scope
- Exhaustive comparison of **Kaboom.js → Kaplay.js vs Phaser.js**:
  - Kaplay: ~130KB, component-based, fast dev, low device requirements, less documentation
  - Phaser: ~900KB+, class-based, industry standard, heavy boilerplate, better debugging
- **Final recommendation: Kaplay.js** — faster development, lower bundle size for student devices, component-based architecture ideal for dynamic Accept/Override behavior mapping
- Provided defense arguments for sidang: "Kaplay dipilih karena efisiensi memori (130KB) untuk perangkat target siswa dan fleksibilitas arsitektur component-based"
- Discussed privacy: no NISN, use session ID only; awareness of UU PDP

**Relevance:** ✅ Kaplay.js decision is final. ✅ CNN over RNN is final. ✅ Privacy stance is current. ⚠️ Kaplay's maturity risk acknowledged but accepted.

---

### 4. Backup004 — DeepSeek #1 (Lines 24234–39589)

**Topic:** Concept consolidation, advisor feedback integration, and priority planning.

**Key Insights:**
- Shadow Advisor mode established with strict rules: no BS, data-driven, casual Indo, zero bias
- Consolidated all prior AI conversations into unified project status
- **Identified critical issues from bimbingan:**
  - Can accidentally said "RNN" during meeting with Pak TB → must fix to CNN in proposal
  - Diagram flow too small/cluttered → must split into 3 parts (global, onboarding, core loop)
  - Justification for "Sketchbook" theme still weak
  - K-Means clustering variables need sync with Dias: decision latency, override ratio, danger acceptance
- **Priority task list:**
  1. Fix RNN→CNN in proposal (30 min, high impact)
  2. Detailed user flow (foundation for everything)
  3. Split diagram flow into 3 parts
  4. Interaction design spec / wireframe
  5. Write Sketchbook theme justification (1 paragraph)
  6. Use case diagram
  7. Sync with Dias on K-Means
- Separated scope: Can-only tasks vs shared tasks vs Dias-only tasks
- Emphasized Pak TB's concern: **"your presentation looks like two separate projects"** — sync is critical
- Discussed Docker, GHCR, and deployment architecture (carried forward to Backup005)

**Relevance:** ✅ All bimbingan feedback is still actionable. ✅ Priority order still valid. ✅ Sync concern remains the #1 organizational risk.

---

### 5. Backup005 — DeepSeek #2 (Lines 39590–52662)

**Topic:** DevOps, server setup, Docker, Tailscale, and infrastructure planning.

**Key Insights:**
- **VM Setup (Proxmox):**
  - VM ID 111, Ubuntu 24.04.2, 12GB RAM, 2 cores, 64GB disk
  - Three accounts: `can` (admin), `deano` (developer Can), `dayes` (developer Dias)
  - Workspace: `/srv/team-projects/` with isolated per-developer and shared folders
- **Docker best practices:** non-root containers, `--read-only`, `--cap-drop=ALL`, `USER 1000` in Dockerfile
- **Tailscale Funnel** for remote access without VPN/port-forwarding
  - Can share single machine access with Dias via email invite
  - Tailscale adds ~10-15ms latency via DERP relay (negligible for REST API)
- **Reverse proxy (Caddy/Nginx)** routes `/api/*` to backend container, `/ws/*` to WebSocket
- **GHCR over Docker Hub:** no pull rate limits, better GitHub integration
- Discussed personal branding / TikTok content strategy (off-topic but noted)
- Created 3 project naming options: "Escape the Sketchbook", "Momo's Sketchbook", "The Momo Project"
- Started drafting **Latar Belakang** structure for proposal (automation bias → HITL → MIT probabilistic thinking → MediaPipe)

**Relevance:** ✅ VM spec and account structure are current. ✅ GHCR decision is final. ✅ Tailscale architecture is valid. ⚠️ Account naming changed (originally `deano` was admin, later `can` became admin).

---

### 6. Backup006 — GPT (Lines 52663–64427)

**Topic:** Presentation deck design, slide structure, wireframe planning, and proposal drafting.

**Key Insights:**
- Established FigJam as the single workspace for bimbingan presentations (no switching between slides and jam board)
- **Recommended slide structure:**
  - Slide 6: Global User Flow
  - Slide 7: Use Case Diagram (after flow, not before)
  - Slide 8: Core Loop & HITL Detail ("jantung PA")
  - Slide 9: Wireframe — Onboarding & First-Time Check
  - Slide 10: Wireframe — Probe UI & Decision Moment
  - Slide 11–13: Level 1–3 Flows (Trust → Doubt → Critical Override)
  - Slide 14: System Architecture
  - Slide 15–17: References, Progress, Thank You
- **Key design principle:** "Game sebagai ruang konsekuensi" — not just entertainment
- Use Case should highlight only one: **"Mengevaluasi Prediksi AI / HITL"**
- Slide 12 "Satu Sistem, Dua Fokus" directly addresses Pak TB's concern about looking like two separate projects
- MVP scoping: Wajib Jadi / Boleh Menyusul / Tidak Dikerjakan / Risiko Utama
- Drafted full **BAB 1 and BAB 2** proposal content (Latar Belakang, Kajian Pustaka, Deskripsi Sistem)
- Confirmed all system constraints in formal academic language

**Relevance:** ✅ Slide structure is the current plan. ✅ Proposal draft is the working version. ✅ Wireframe priorities are current. ⚠️ Some slide numbers may have shifted during iteration.

---

### 7. Backup007 — Meta AI #2 (Lines 64428–71368)

**Topic:** Literature review verification and final presentation slide content.

**Key Insights:**
- **Literature Review with anti-hallucination verification:**
  - Category A (Shared/General): 12 journals — AI literacy, HITL-ML, XAI-ED, productive failure, probabilistic reinforcement learning, automation bias, GBL
  - Category B (Can/Frontend): 8 journals — MediaPipe hand gesture, pedagogical agents, gamification flow, failure learning, child-computer interaction, Kaplay.js game engine
  - Category C (Dias/AI): 7 journals — sketch recognition, CNN/RNN comparison, TF.js, QuickDraw dataset, K-Means clustering
  - Several entries marked ⚠️ for author name verification
- **Final presentation content (Slides 15–24):**
  - Level flows with mermaid diagrams (Trust → Ambiguity → Critical Override)
  - System architecture diagram (client-side pipeline: MediaPipe → Canvas → TF.js → Probe UI → Kaplay → Log)
  - Design system: Input–Process–Output mapping
  - AI pipeline: Canvas → Resize 28×28 → Grayscale → Normalize → Tensor → CNN → Softmax → Top-3
  - Log & Analysis flow: Frontend event → JSON → POST API → SQLite → K-Means → Dashboard
  - Progress & Next Steps slide
- Confirmed Momo is **not LLM/NLP/Generative AI** — simple condition-based pedagogical agent

**Relevance:** ✅ Literature review is the current reference list. ✅ Final slide content is the working version. ⚠️ Some DOI/author entries still need manual verification.

---

## Cross-Conversation Themes

### 1. Human-in-the-Loop as Core Identity
Every conversation centers on HITL as the defining feature. The system is not "a game with AI" — it's "a HITL learning system delivered through a game." Override/Accept/Correct is the mechanism; game consequences are the feedback; log data is the research output.

### 2. Three Pillars (Repeated Consistently)
- **Interaksi** — MediaPipe gesture drawing, Probe UI, Momo as companion
- **Edukasi** — AI literacy, probabilistic thinking, automation bias mitigation
- **Gameplay/Narasi** — Escape the Sketchbook theme, Stickman, consequence-driven mechanics

### 3. Client-Side Architecture as Hard Constraint
No backend AI inference. No model retraining. TF.js runs in browser. Server is a data sink for logs only. This was stated in Backup001 and never deviated.

### 4. Scope Creep Resistance
Repeated warnings across all conversations: don't add real-time training, don't add pre/post-test, don't over-engineer the game engine, don't make Momo an LLM chatbot. The "No" list is as important as the "Yes" list.

### 5. Dual-Project Risk
Pak TB's concern — "this looks like two separate projects" — appears in Backups 004, 005, and 006. Mitigation strategies: shared user flow, "Satu Sistem, Dua Fokus" slide, HITL moment as the meeting point, synchronized proposal language.

### 6. Defensive Academic Positioning
Every conversation includes strategies for sidang defense: why Kaplay not Phaser, why CNN not RNN, why override is not retraining, why no pre/post-test, why Momo is not LLM. The project is designed to be **defensible**, not just functional.

---

## Evolution Timeline

| Phase | Backup | What Changed |
|-------|--------|-------------|
| **Concept birth** | 001-Claude | SD Kelas 5 target, CNN + TF.js, game 2D, HITL override |
| **Target shift** | 002-Gemini | SD → SMP 7–9 (Bu Hesti feedback), Momo introduced, 3 pillars defined |
| **Tech validation** | 003-Meta | CNN confirmed over RNN, Kaplay chosen over Phaser, privacy stance |
| **Consolidation** | 004-DeepSeek | Bimbingan feedback integrated, priorities set, sync concerns raised |
| **Infrastructure** | 005-DeepSeek | VM/Docker/Tailscale/GHCR planned, account structure defined |
| **Formalization** | 006-GPT | Proposal drafted (BAB 1–3), presentation deck structured, wireframes planned |
| **Verification** | 007-Meta | Literature review verified, final slide content produced, system diagrams finalized |

---

## Deprecated vs Still-Relevant Decisions

### ❌ Deprecated
| Decision | Origin | Reason |
|----------|--------|--------|
| Target SD Kelas 5 | 001-Claude | Changed to SMP 7–9 per Bu Hesti |
| Title referencing "SD" | 001-Claude | Must use "SMP" in all formal documents |
| Kaboom.js as game engine | 002-Gemini | Replaced by Kaplay.js (successor/fork) |
| RNN terminology in proposal | 004-DeepSeek | Must be CNN — was a slip during bimbingan |
| "Feedback loop" retraining concept | 001-Claude | Removed; override is NOT retraining |
| Guru as active system user | 001-Claude | Guru is not an actor in the system |
| `deano` as admin account | 005-DeepSeek | Later changed to `can` as admin |

### ✅ Still Relevant
| Decision | Status | Source |
|----------|--------|--------|
| HITL as core mechanism | Active | All backups |
| CNN MobileNet + TF.js client-side | Active | All backups |
| Top-3 + confidence score display | Active | All backups |
| Accept / Correct / Override | Active | 002–007 |
| Solid / Danger / Decorative mapping | Active | All backups |
| Kaplay.js as game engine | Active | 003–007 |
| Momo as pedagogical agent (not LLM) | Active | 002–007 |
| SMP 7–9 target | Active | 002–007 |
| No pre/post-test; log-based evaluation | Active | All backups |
| GHCR for container registry | Active | 005 |
| Tailscale for remote access | Active | 005 |
| Session ID (no NISN) for privacy | Active | 003, 004 |
| K-Means clustering for analysis | Active | 004, 007 |
| 3 levels: Trust → Doubt → Critical Override | Active | 004, 006, 007 |
| Escape the Sketchbook as project name | Active | 004–007 |
| SQLite for database | Active | 005, 007 |

---

## Open Items & Risks

1. **Literature review verification** — Some DOI/author entries need manual check (marked ⚠️)
2. **Can–Dias sync** — Still the #1 organizational risk; proposal must read as one project
3. **Kaplay.js maturity** — Accepted risk; smaller community means harder debugging
4. **MediaPipe drawing quality** — Messy air-drawings could make AI predictions unreliable (acknowledged as feature, not bug)
5. **Pak Doto as potential examiner** — Concern about comparison with more complex VA projects; mitigate with Momo-as-PA framing
6. **Model accuracy threshold** — CNN MobileNet must be tested with QuickDraw subset before integration; no baseline established yet
