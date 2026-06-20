# MASKOT README — Momo Design Documentation Hub

> **Project:** Sketchbook Universe  
> **Document:** Documentation Index — Bigprompt v2.0  
> **Date:** 2026-03-05  
> **Status:** Bigprompt v2.0 COMPLETE — 4 design options documented, compared, and analyzed

---

## Quick Reference

```
┌─────────────────────────────────────────────────────┐
│              MOMO — Quick Reference (v2.0)          │
├─────────────────────────────────────────────────────┤
│ Name:       MOMO (working title — suggest "SKETI")  │
│ Species:    Sketchbook Creature (concept-dependent)  │
│ Movement:   FLOATING — no legs, no wings            │
│ Comms:      Text bubble ONLY — no voice, no NLP     │
│ Style:      8-bit geometric, rect-based             │
│ Base Size:  64×64 px                                │
│ Max Shapes: 5                                       │
│ States:     idle | happy | confused | thinking |    │
│             excited                                  │
│ Engine:     Kaplay.js                               │
│ Target:     Siswa SMP Kelas 7-9 (13-15 tahun)      │
│ Role:       Game Master, Confidence Display,        │
│             Probe Trigger, Narrative Guide           │
│                                                     │
│ KEY RULES:  NO LEGS · NO WINGS · FLOAT ONLY        │
│             Text bubble only · IP SAFE from day 1   │
└─────────────────────────────────────────────────────┘
```

---

## Document Index

| # | File | Content | Status |
|---|------|---------|--------|
| 1 | [`maskot_research_clawd_analysis.md`](./maskot_research_clawd_analysis.md) | Clawd success analysis + Among Us, Fall Guys, Pac-Man references + ADOPT/ADAPT/AVOID strategy | ✅ Complete |
| 2 | [`maskot_options_comparison.md`](./maskot_options_comparison.md) | 4 design options with ASCII art, hex colors, animation specs + weighted scoring + TOP 2 recommendations | ✅ Complete |
| 3 | [`maskot_animation_bible.md`](./maskot_animation_bible.md) | State machine + 5 expression states with keyframes, timing, easing, pseudo-code | ✅ Complete |
| 4 | [`maskot_ip_safety_report.md`](./maskot_ip_safety_report.md) | IP analysis per option + silhouette test + color test + name safety + Clawd distance | ✅ Complete |
| — | [`maskot_concept.md`](./maskot_concept.md) | OLD version (v1) — DO NOT OVERWRITE — kept as historical reference | 📦 Archived |

---

## Design Options Summary

### OPSI A: "Sticky Note" — 🏆 RECOMMENDED #1
- Yellow rounded rectangle, dog-ear fold, cream paper feel
- Score: 4.35/5.00 (highest)
- Strengths: Best Kaplay.js compat, easiest animation, 8-bit pure
- Risk: Yellow color association (Pikachu), "office supply" feel

### OPSI B: "Ink Blob"
- Dark navy irregular blob, animated drips, white dot eyes
- Score: 3.95/5.00
- Strengths: Most unique color palette, best IP safety for shape
- Risk: Blob reads as generic circle at 16×16, dark palette may feel heavy

### OPSI C: "Sketch Ghost" — 🏆 RECOMMENDED #2
- Cream dome with wavy bottom, pencil-outline texture, paper fill
- Score: 3.95/5.00
- Strengths: Best theme fit, strongest narrative, ghost float is natural
- Risk: Ghost silhouette = Pac-Man association, weakest IP safety

### OPSI D: "Origami Monster"
- Cream diamond/rhombus, 3D fold illusion, cel-shaded
- Score: 3.45/5.00
- Strengths: Best IP safety (most unique shape), best silhouette
- Risk: Hardest to implement in Kaplay.js, angular shape = awkward UI integration

---

## Key Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Top recommendation** | OPSI A (Sticky Note) | Highest weighted score, best technical feasibility |
| **Second recommendation** | OPSI C (Sketch Ghost) | Best theme fit, strongest emotional resonance |
| **Hybrid direction** | "Sketch Note Ghost" (A+C hybrid) | Combines rect base + pencil aesthetic + float — matches existing v2.0 concept |
| **Name suggestion** | "SKETI" or "MOMO the Sketch" | "MOMO" alone has too many collisions |
| **Float layer** | Universal, always-on | Float is identity, not just animation |
| **Clawd distance** | Moderate for A and D, High for B and C | Mitigations specified for A (fold + shadow + pencil outline) |

---

## Next Steps

| # | Action | Owner | Priority |
|---|--------|-------|----------|
| 1 | Create pixel art sprite for recommended option (64×64) | Designer | HIGH |
| 2 | Prototype shape-based Momo in Kaplay.js | Developer | HIGH |
| 3 | User test with siswa SMP (name + design feedback) | Researcher | MEDIUM |
| 4 | Iterate based on feedback | Designer + Dev | MEDIUM |
| 5 | Finalize sprite sheet for production | Designer | LOW (after step 4) |
| 6 | Write narrative script for all 3 levels | Writer | LOW (after step 4) |
| 7 | Consult IP attorney for trademark filing | Legal | LOW (after step 4) |

---

## Constraint Checklist

| Constraint | Status | Notes |
|------------|--------|-------|
| NO LEGS | ✅ | All 4 options: floating creatures, zero leg elements |
| NO WINGS | ✅ | All 4 options: float without wings (sketchbook logic) |
| Text bubble only | ✅ | No voice, no NLP, no speech synthesis |
| 8-bit geometric style | ✅ | Rect-based, limited palette, pixel aesthetic |
| Original / IP safe | ✅ | All options analyzed; mitigations specified |
| Kaplay.js compatible | ✅ | All options use rect/circle/ellipse/polygon |
| < 100KB total assets | ✅ | Shape-based: ~35KB; Sprite sheet: ~30KB |
| < 5MB RAM | ✅ | ~6KB runtime memory |
| Target: 13-15 year olds | ✅ | Design considerations for teen appeal documented |

---

## Color Palette Reference (Per Option)

| Option | Primary | Secondary | Accent | Outline |
|--------|---------|-----------|--------|---------|
| A: Sticky Note | `#FFE066` | `#4ECDC4` | `#FF6B6B` | `#2D3436` |
| B: Ink Blob | `#1A1A2E` | `#16213E` | `#E94560` | `#0F0F23` |
| C: Sketch Ghost | `#F5F0E8` | `#2D3436` | `#FF6B6B` | `#3D3D3D` |
| D: Origami Monster | `#F5E6CA` | `#D4C4A8` | `#E74C3C` | `#2D3436` |
| **Hybrid (existing v2.0)** | **`#00E676`** | **`#4ECDC4`** | **`#FFE66D`** | **`#2D3436`** |

---

*Document generated: 2026-03-05*  
*Bigprompt v2.0 — Documentation Hub*  
*Source: Task 2 execution*
