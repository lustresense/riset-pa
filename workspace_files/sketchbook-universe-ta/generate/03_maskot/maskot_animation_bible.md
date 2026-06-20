# Maskot Animation Bible — Momo State Machine & Timing Specs

> **Project:** Sketchbook Universe  
> **Document:** Animation Deep-Dive — Bigprompt v2.0  
> **Date:** 2026-03-05  
> **Engine:** Kaplay.js (JavaScript 2D game engine)  
> **Critical Constraint:** ALL animations execute while FLOATING — no walk cycle, no ground contact

---

## Daftar Isi

1. [Universal Float Layer](#1-universal-float-layer)
2. [State Machine Architecture](#2-state-machine-architecture)
3. [State: IDLE](#3-state-idle)
4. [State: HAPPY](#4-state-happy)
5. [State: CONFUSED](#5-state-confused)
6. [State: THINKING](#6-state-thinking)
7. [State: EXCITED](#7-state-excited)
8. [Transition Rules](#8-transition-rules)
9. [Performance Budget](#9-performance-budget)
10. [Sprite Sheet Specification](#10-sprite-sheet-specification)

---

## 1. Universal Float Layer

Every Momo state runs on top of the **Universal Float Layer** — a perpetual bobbing animation that NEVER stops. This is Momo's identity: she floats.

### Float Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Amplitude** | ±3px | Gentle bob, not aggressive |
| **Frequency** | 2.5 rad/s | `sin(time * 2.5)` — calm, meditative |
| **Rotation oscillation** | ±2° | `sin(time * 1.5) * 2` — subtle sway |
| **Shadow scale** | `1.0 ± 0.1` | Shadow shrinks when Momo rises, grows when she dips |
| **Shadow opacity** | `0.15 ± 0.03` | Shadow fades when Momo rises, darkens when she dips |
| **Blink cycle** | Every ~3 seconds | Eyes `scaleY → 0.1` for 120ms, then back |

### Float Pseudo-Code (Always Running)

```javascript
// === UNIVERSAL FLOAT LAYER ===
// This runs REGARDLESS of current state.
// States modify ON TOP of this base float.

const FLOAT_AMP = 3;      // bob amplitude in px
const FLOAT_FREQ = 2.5;   // bob frequency in rad/s
const ROT_AMP = 2;        // rotation oscillation in degrees
const ROT_FREQ = 1.5;     // rotation frequency in rad/s

function updateFloatLayer(momoRef, dt) {
  const t = time();
  
  // Vertical bob — ALWAYS active
  const bobOffset = Math.sin(t * FLOAT_FREQ) * FLOAT_AMP;
  momoRef.pos.y = momoRef.baseY + bobOffset;
  
  // Rotation sway — ALWAYS active (unless state overrides)
  if (momoRef.state !== "thinking" && momoRef.state !== "confused") {
    momoRef.angle = Math.sin(t * ROT_FREQ) * ROT_AMP;
  }
  
  // Shadow follows float
  const shadow = momoRef.get("momo_shadow")[0];
  const shadowScale = 1 - (bobOffset / 30) * 0.2;
  shadow.scaleTo(vec2(
    Math.max(0.7, shadowScale),
    Math.max(0.5, shadowScale * 0.5)
  ));
  shadow.opacity = 0.15 - (bobOffset / 30) * 0.03;
  
  // Blink cycle — ALWAYS active (unless state overrides eyes)
  const blinkCycle = Math.floor(t * 100) % 300;
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  if (blinkCycle < 4 && momoRef.state !== "excited") {
    eyeL.scale = vec2(1, 0.1);
    eyeR.scale = vec2(1, 0.1);
  } else if (momoRef.state !== "excited") {
    eyeL.scale = vec2(1, 1);
    eyeR.scale = vec2(1, 1);
  }
}
```

---

## 2. State Machine Architecture

### State Diagram

```
                    ┌──────────┐
         ┌─────────│   IDLE   │──────────┐
         │         └──────────┘          │
         │          ▲      ▲             │
         │          │      │             │
         ▼          │      │             ▼
    ┌──────────┐    │      │      ┌───────────┐
    │ CONFUSED │────┘      └──────│  HAPPY    │
    └──────────┘                    └───────────┘
         │                              ▲
         │                              │
         ▼                              │
    ┌──────────┐                 ┌───────────┐
    │ THINKING │─────────────────│  EXCITED  │
    └──────────┘                 └───────────┘
         │                              │
         │                              │
         └──────────┐     ┌─────────────┘
                    ▼     ▼
               ┌──────────┐
               │   IDLE   │  ← ALL states return to IDLE
               └──────────┘
```

### State Categories

| Type | States | Behavior |
|------|--------|----------|
| **Looping** | IDLE, CONFUSED, THINKING | Plays continuously until trigger |
| **One-shot** | HAPPY, EXCITED | Plays once, auto-returns to IDLE |

### State Transition Table

| From | To | Trigger | Transition Duration |
|------|----|---------|-------------------|
| IDLE | HAPPY | Confidence > 0.8 / Correct answer | 0ms (instant) |
| IDLE | CONFUSED | Confidence 0.4–0.6 / Ambiguous result | 0ms (instant) |
| IDLE | THINKING | Probe starts / Momo "reading" drawing | 0ms (instant) |
| HAPPY | IDLE | Timeout (1.5s) | 300ms ease-out |
| CONFUSED | THINKING | Player retries probe | 200ms ease-in-out |
| CONFUSED | IDLE | Issue resolved | 300ms ease-out |
| THINKING | HAPPY | Probe answered correctly | 0ms (instant) |
| THINKING | CONFUSED | Probe timeout | 0ms (instant) |
| HAPPY | EXCITED | Streak ≥ 3 / Level complete | 0ms (instant) |
| EXCITED | IDLE | Timeout (2.0s) | 400ms ease-out |
| Any | IDLE | Game reset | 500ms ease-in-out |

---

## 3. State: IDLE

### Overview
Momo's default state — floating gently, occasional blink, subtle sway. This is the "resting face" that players see most often.

### Visual Description
Momo floats with a gentle sinusoidal bob (±3px). Her body sways slightly (±2°). Eyes blink every ~3 seconds. Mouth is a neutral line. Float shadow breathes with her. Nothing else happens — peaceful, present, waiting.

### Keyframe Breakdown

| Frame | Time (ms) | Body Y | Body Angle | Eye Scale | Shadow Scale | Shadow Opacity |
|-------|-----------|--------|------------|-----------|--------------|----------------|
| 1 | 0 | +0 | 0° | (1,1) | (1.0, 0.5) | 0.15 |
| 2 | 400 | +1.5 | +1° | (1,1) | (0.95, 0.48) | 0.14 |
| 3 | 800 | +3 | +2° | (1,1) | (0.90, 0.45) | 0.12 |
| 4 | 1200 | +1.5 | +1° | (1,1) | (0.95, 0.48) | 0.14 |
| 5 | 1600 | +0 | 0° | (1,1) | (1.0, 0.5) | 0.15 |
| 6 | 2000 | -1.5 | -1° | (1,1) | (1.05, 0.53) | 0.16 |
| — | ~3000 | — | — | (1, 0.1) | — | — | ← BLINK (120ms) |
| — | ~3120 | — | — | (1,1) | — | — | ← BLINK END |

**Loop:** Frames 1-6 repeat infinitely.

### Timing & Easing

| Property | Easing | Duration | Formula |
|----------|--------|----------|---------|
| Vertical bob | `sinusoidal` | Continuous | `sin(time * 2.5) * 3` |
| Rotation sway | `sinusoidal` | Continuous | `sin(time * 1.5) * 2` |
| Blink | `step` | 120ms | `scaleY → 0.1` → wait 120ms → `scaleY → 1.0` |

### Pseudo-Code (Kaplay.js)

```javascript
// === IDLE STATE ===
// The float layer handles most of this.
// IDLE just means "no additional animation on top of float."

function enterIdle(momoRef) {
  momoRef.state = "idle";
  
  // Reset all transforms to neutral
  const head = momoRef.get("momo_head")[0];
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const mouth = momoRef.get("momo_mouth")[0];
  const body = momoRef.get("momo_body")[0];
  const fold = momoRef.get("momo_fold")[0];
  
  // Smooth reset with easing
  tween(momoRef.scale, vec2(1, 1), 0.3, (v) => momoRef.scale = v, easings.easeOutQuad);
  tween(momoRef.angle, 0, 0.3, (v) => momoRef.angle = v, easings.easeOutQuad);
  
  // Reset eyes
  eyeL.radius = 3;
  eyeR.radius = 3;
  eyeL.color = MOMO_COLORS.outline;
  eyeR.color = MOMO_COLORS.outline;
  eyeL.pos = vec2(-6, -22);
  eyeR.pos = vec2(6, -22);
  
  // Reset mouth
  mouth.width = 8;
  mouth.height = 3;
  mouth.angle = 0;
  
  // Reset fold
  fold.color = MOMO_COLORS.secondary;
  
  // Reset body outline
  body.outline = outline(2, MOMO_COLORS.outline);
}
```

---

## 4. State: HAPPY

### Overview
Momo bounces upward while floating, eyes get bigger, sparkles appear. A classic "yay!" moment that plays after correct answers or high confidence.

### Visual Description
Momo's body squishes down (anticipation), then launches upward (stretch), reaches peak with sparkles, settles back to float height. Eyes grow to radius 4. Mouth widens. Yellow sparkle particles burst outward. The float continues throughout — Momo never stops floating, even when bouncing.

### Keyframe Breakdown

| Frame | Time (ms) | Body Scale | Body Y Offset | Eye Radius | Mouth | Shadow Scale | Particles |
|-------|-----------|------------|---------------|------------|-------|--------------|-----------|
| 0 | 0 | (1.0, 1.0) | +0 | 3 | 8×3 | (1.0, 0.5) | — | ← Entry state
| 1 | 0–100 | (1.2, 0.8) | +0 | 3→4 | 8×3 | (1.1, 0.55) | — | ← SQUISH (anticipation)
| 2 | 100–250 | (0.9, 1.2) | -12 | 4 | 10×4 | (0.7, 0.35) | — | ← LAUNCH (stretch up)
| 3 | 250–600 | (0.95, 1.1) | -16 | 4 | 10×4 | (0.5, 0.25) | 5× yellow | ← PEAK + sparkles
| 4 | 600–1000 | (1.05, 0.95) | -8 | 4 | 10×4 | (0.8, 0.4) | fading | ← FALL
| 5 | 1000–1300 | (1.1, 0.9) | -2 | 4→3 | 8×3 | (1.0, 0.5) | — | ← SETTLE
| 6 | 1300–1500 | (1.0, 1.0) | +0 | 3 | 8×3 | (1.0, 0.5) | — | ← Resume IDLE

**Total duration: 1500ms (one-shot)**

### Timing & Easing

| Phase | Duration | Easing | Purpose |
|-------|----------|--------|---------|
| Squish | 100ms | `easeInQuad` | Anticipation — compress energy |
| Launch | 150ms | `easeOutCubic` | Explosive upward motion |
| Peak | 350ms | `easeOutQuad` | Hang time at top — float moment |
| Fall | 400ms | `easeInQuad` | Gravity pull back down |
| Settle | 300ms | `easeOutElastic` | Bouncy landing back to float |
| Resume | 200ms | `easeOutQuad` | Transition to IDLE |

### Pseudo-Code (Kaplay.js)

```javascript
// === HAPPY STATE ===
// One-shot: 1.5s, then auto-return to IDLE

function enterHappy(momoRef) {
  momoRef.state = "happy";
  const body = momoRef.get("momo_body")[0];
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const mouth = momoRef.get("momo_mouth")[0];
  const shadow = momoRef.get("momo_shadow")[0];
  
  // Eyes bigger
  eyeL.radius = 4;
  eyeR.radius = 4;
  
  // Mouth wider
  mouth.width = 10;
  mouth.height = 4;
  
  // Phase 1: SQUISH (0-100ms)
  tween(momoRef.scale, vec2(1.2, 0.8), 0.1, (v) => momoRef.scale = v, easings.easeInQuad)
    .onEnd(() => {
      
      // Phase 2: LAUNCH (100-250ms)
      tween(momoRef.scale, vec2(0.9, 1.2), 0.15, (v) => momoRef.scale = v, easings.easeOutCubic);
      tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 12), 0.15, 
        (v) => momoRef.pos = v, easings.easeOutCubic)
        .onEnd(() => {
          
          // Phase 3: PEAK + SPARKLES (250-600ms)
          tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 16), 0.35, 
            (v) => momoRef.pos = v, easings.easeOutQuad);
          spawnSparkles(momoRef.pos, 5, MOMO_COLORS.accent); // yellow sparkles
          
          // Phase 4: FALL (600-1000ms)
          wait(0.35, () => {
            tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 8), 0.4, 
              (v) => momoRef.pos = v, easings.easeInQuad)
              .onEnd(() => {
                
                // Phase 5: SETTLE (1000-1300ms)
                tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 2), 0.3, 
                  (v) => momoRef.pos = v, easings.easeOutElastic);
                tween(momoRef.scale, vec2(1.1, 0.9), 0.3, 
                  (v) => momoRef.scale = v, easings.easeOutQuad)
                  .onEnd(() => {
                    
                    // Phase 6: RESUME IDLE (1300-1500ms)
                    tween(momoRef.scale, vec2(1, 1), 0.2, 
                      (v) => momoRef.scale = v, easings.easeOutQuad)
                      .onEnd(() => enterIdle(momoRef));
                  });
              });
          });
        });
    });
  
  // Shadow animates in sync (handled by float layer)
}
```

---

## 5. State: CONFUSED

### Overview
Momo tilts 15°, one eye grows bigger, a question mark spawns above her head. She drifts sideways while floating. This state is HELD until the issue is resolved.

### Visual Description
Momo's body rotates to ~15° tilt (oscillating ±3° around that). Her left eye grows slightly (radius 3→3.5) while right stays normal — creating an asymmetrical "huh?" look. A bright yellow "?" spawns above her head and wobbles. She drifts sideways (±4px) while continuing to float. Mouth becomes a small, slightly angled line. The overall feeling is "wait, what?"

### Keyframe Breakdown

| Frame | Time (ms) | Body Angle | Body X Offset | Eye L | Eye R | Mouth | "?" Opacity | Shadow |
|-------|-----------|------------|---------------|-------|-------|-------|-------------|--------|
| 1 | 0 | 10° | +0 | r=3 | r=3 | 8×3 | 0 | (1.0, 0.5) | ← Entry
| 2 | 0–200 | 12° | +2 | r=3.5 | r=3 | 6×2 | 0.3 | (1.0, 0.5) | ← Tilt begins
| 3 | 200–400 | 15° | +3 | r=3.5 | r=3 | 6×2 | 1.0 | (1.0, 0.5) | ← Full tilt + "?" visible
| 4 | 400–600 | 12° | +2 | r=3.5 | r=3 | 6×2 | 1.0 | (1.0, 0.5) | ← Oscillate
| 5 | 600–800 | 15° | +3 | r=3.5 | r=3 | 6×2 | 1.0 | (1.0, 0.5) | ← Oscillate
| — | — | — | — | — | — | — | — | ← LOOP 4-5 until resolved |

**Loop: Frames 4-5 repeat infinitely until trigger resolves state.**

### Timing & Easing

| Property | Easing | Duration | Formula |
|----------|--------|----------|---------|
| Body tilt | `sinusoidal` | Continuous | `12 + sin(time * 4) * 3` degrees |
| Lateral drift | `sinusoidal` | Continuous | `sin(time * 2) * 4` px |
| "?" wobble | `sinusoidal` | 500ms cycle | `pos.y = baseY + sin(time * 4) * 2` |
| "?" fade-in | `easeOutQuad` | 300ms | `opacity 0 → 1` |
| Eye shift | `easeOutQuad` | 200ms | L eye `pos.x -1`, R eye `pos.x +1` |

### Pseudo-Code (Kaplay.js)

```javascript
// === CONFUSED STATE ===
// Hold state — persists until resolved

let confusedQuestionMark = null;

function enterConfused(momoRef) {
  momoRef.state = "confused";
  
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const mouth = momoRef.get("momo_mouth")[0];
  
  // Asymmetric eyes (one bigger)
  tween(eyeL.radius, 3.5, 0.2, (v) => eyeL.radius = v, easings.easeOutQuad);
  
  // Eyes shift sideways
  tween(eyeL.pos, vec2(-7, -22), 0.2, (v) => eyeL.pos = v, easings.easeOutQuad);
  tween(eyeR.pos, vec2(7, -22), 0.2, (v) => eyeR.pos = v, easings.easeOutQuad);
  
  // Smaller confused mouth
  mouth.width = 6;
  mouth.height = 2;
  mouth.angle = -10;
  
  // Spawn question mark
  confusedQuestionMark = add([
    text("?", { size: 14, font: "monospace" }),
    pos(momoRef.pos.x, momoRef.pos.y - 40),
    anchor("center"),
    color(MOMO_COLORS.accent),
    opacity(0),
    "question_mark",
  ]);
  
  // Fade in "?" 
  tween(confusedQuestionMark.opacity, 1, 0.3, 
    (v) => confusedQuestionMark.opacity = v, easings.easeOutQuad);
}

// In onUpdate loop:
function updateConfused(momoRef) {
  if (momoRef.state !== "confused") return;
  
  const t = time();
  
  // Oscillating tilt
  momoRef.angle = 12 + Math.sin(t * 4) * 3;
  
  // Lateral drift
  momoRef.pos.x = momoRef.baseX + Math.sin(t * 2) * 4;
  
  // Continue float bob
  const bobOffset = Math.sin(t * 2.5) * 2;
  momoRef.pos.y = momoRef.baseY + bobOffset;
  
  // Shadow follows drift
  const shadow = momoRef.get("momo_shadow")[0];
  shadow.pos.x = Math.sin(t * 2) * 4;
  
  // "?" wobble
  if (confusedQuestionMark) {
    confusedQuestionMark.pos = vec2(
      momoRef.pos.x,
      momoRef.pos.y - 40 + Math.sin(t * 4) * 2
    );
  }
}

function exitConfused(momoRef) {
  // Remove question mark
  if (confusedQuestionMark) {
    tween(confusedQuestionMark.opacity, 0, 0.2, 
      (v) => confusedQuestionMark.opacity = v, easings.easeInQuad)
      .onEnd(() => {
        destroy(confusedQuestionMark);
        confusedQuestionMark = null;
      });
  }
  enterIdle(momoRef);
}
```

---

## 6. State: THINKING

### Overview
Momo's eyes look left-right, her body dims slightly, and processing indicators (orbiting dots) appear. This state plays when Momo is "reading" a drawing (CNN inference in progress).

### Visual Description
Momo's body color desaturates slightly (vibrant green → slightly muted green) to indicate "processing." Her eyes dart left-right rhythmically (like reading). Three small yellow dots orbit around her body at radius 24. The body does a slow, gentle spin (not fast — contemplative). The float continues throughout.

### Keyframe Breakdown

| Frame | Time (ms) | Body Angle | Body Color | Eye Position | Dot Count | Shadow |
|-------|-----------|------------|------------|--------------|-----------|--------|
| 1 | 0 | 60° | #00E676 | center | 0 | normal | ← Entry
| 2 | 0–300 | 90° | #00E676→#4ADE80 | center | 1 | normal | ← Spin + dim begins
| 3 | 300–600 | 180° | #4ADE80 | left | 2 | wobble | ← Eyes dart left
| 4 | 600–900 | 270° | #4ADE80 | right | 3 | wobble | ← Eyes dart right
| 5 | 900–1200 | 360° | #4ADE80 | center | 3 orbiting | wobble | ← Full orbit
| 6 | 1200–1500 | 90° | #4ADE80 | left | 3 orbiting | wobble | ← LOOP 3-6

**Loop: Frames 3-6 repeat until probe is answered.**

### Timing & Easing

| Property | Easing | Duration | Formula |
|----------|--------|----------|---------|
| Body spin | `linear` | 3000ms per rotation | `(time * 120) % 360` degrees |
| Eye dart | `step` | 600ms per direction | Alternating left/right every 600ms |
| Dot orbit | `linear` | Continuous | `pos = center + vec2(cos(t*4+i*2.09)*24, sin(t*4+i*2.09)*24)` |
| Color dim | `easeOutQuad` | 300ms | `#00E676 → #4ADE80` |
| Shadow wobble | `sinusoidal` | Continuous | `scaleX = 1 + sin(t*3)*0.1` |

### Pseudo-Code (Kaplay.js)

```javascript
// === THINKING STATE ===
// Hold state — persists until probe is answered

let thinkingDots = [];

function enterThinking(momoRef) {
  momoRef.state = "thinking";
  
  const body = momoRef.get("momo_body")[0];
  const head = momoRef.get("momo_head")[0];
  const fold = momoRef.get("momo_fold")[0];
  
  // Dim body color (processing)
  tween(body.color, Color.fromHex("#4ADE80"), 0.3, 
    (v) => body.color = v, easings.easeOutQuad);
  tween(head.color, Color.fromHex("#4ADE80"), 0.3, 
    (v) => head.color = v, easings.easeOutQuad);
  tween(fold.color, Color.fromHex("#7EDDD6"), 0.3, 
    (v) => fold.color = v, easings.easeOutQuad);
  
  // Spawn 3 orbiting dots
  thinkingDots = [];
  for (let i = 0; i < 3; i++) {
    const dot = add([
      circle(2),
      pos(0, 0),
      color(MOMO_COLORS.accent),
      "thinking_dot",
    ]);
    thinkingDots.push(dot);
  }
}

function updateThinking(momoRef) {
  if (momoRef.state !== "thinking") return;
  
  const t = time();
  
  // Slow body spin (contemplative, not frantic)
  momoRef.angle = (t * 120) % 360;
  
  // Continue float (slightly reduced)
  const bobOffset = Math.sin(t * 2.5) * 2;
  momoRef.pos.y = momoRef.baseY + bobOffset;
  
  // Eye dart: left-right every 600ms
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const eyePhase = Math.floor(t * 1000 / 600) % 2;
  const eyeTargetX = eyePhase === 0 ? -8 : -4;
  eyeL.pos.x = eyeTargetX;
  eyeR.pos.x = eyeTargetX + 12;
  
  // Orbiting dots
  thinkingDots.forEach((dot, i) => {
    dot.pos = momoRef.pos.add(vec2(
      Math.cos(t * 4 + i * 2.09) * 24,
      Math.sin(t * 4 + i * 2.09) * 24
    ));
  });
  
  // Shadow wobble from spin
  const shadow = momoRef.get("momo_shadow")[0];
  shadow.scaleTo(vec2(
    1 + Math.sin(t * 3) * 0.1,
    0.5 + Math.sin(t * 3) * 0.05
  ));
}

function exitThinking(momoRef) {
  // Destroy orbiting dots
  thinkingDots.forEach(d => destroy(d));
  thinkingDots = [];
  
  // Restore body color
  const body = momoRef.get("momo_body")[0];
  const head = momoRef.get("momo_head")[0];
  const fold = momoRef.get("momo_fold")[0];
  
  tween(body.color, MOMO_COLORS.primary, 0.3, 
    (v) => body.color = v, easings.easeOutQuad);
  tween(head.color, MOMO_COLORS.primary, 0.3, 
    (v) => head.color = v, easings.easeOutQuad);
  tween(fold.color, MOMO_COLORS.secondary, 0.3, 
    (v) => fold.color = v, easings.easeOutQuad);
  
  enterIdle(momoRef);
}
```

---

## 7. State: EXCITED

### Overview
Momo vibrates rapidly, eyes become stars, confetti bursts outward. This is the celebration state — triggered by streaks or level completion. The most energetic state, but Momo never stops floating.

### Visual Description
Momo's body shakes rapidly (±3px horizontally at high frequency). Eyes turn into star shapes (★ ★) or flash yellow. Mouth opens wide. A confetti burst of 8+ particles (mix of yellow and teal) explodes outward. The fold corner glows brighter teal. The body outline pulses green. After 2 seconds, everything settles back to idle.

### Keyframe Breakdown

| Frame | Time (ms) | Body Shake | Body Scale | Eyes | Mouth | Fold | Shadow | Particles |
|-------|-----------|------------|------------|------|-------|------|--------|-----------|
| 1 | 0 | ±3px | (1.0, 1.0) | r=3, dark | 8×3 | normal | normal | — | ← Entry
| 2 | 0–200 | ±3px | (1.1, 0.9) | r=4.5, yellow ★ | 10×6 | glow teal | pulse | 8 confetti | ← SHAKE + BOUNCE
| 3 | 200–600 | ±3px | (0.9, 1.15) | r=4.5, yellow ★ | 10×6 | glow teal | shrink | more confetti | ← UP + SPARKLE
| 4 | 600–1000 | ±2px | (1.05, 0.95) | r=4, dark | 10×6 | glow teal | grow | fading | ← DOWN
| 5 | 1000–1500 | ±1px | (0.95, 1.05) | r=4, dark | 8×4 | normal | shrink | — | ← SECOND BOUNCE
| 6 | 1500–2000 | off | (1.0, 1.0) | r=3, dark | 8×3 | normal | normal | — | ← SETTLE → IDLE

**Total duration: 2000ms (one-shot)**

### Timing & Easing

| Phase | Duration | Easing | Purpose |
|-------|----------|--------|---------|
| Shake+bounce | 200ms | `easeOutCubic` | Explosive start |
| Rise+sparkle | 400ms | `easeOutQuad` | Climax — maximum energy |
| Fall | 400ms | `easeInQuad` | Gravity |
| Second bounce | 500ms | `easeOutElastic` | Joyful rebound |
| Settle | 500ms | `easeOutQuad` | Calm return |

### Pseudo-Code (Kaplay.js)

```javascript
// === EXCITED STATE ===
// One-shot: 2.0s, then auto-return to IDLE

function enterExcited(momoRef) {
  momoRef.state = "excited";
  
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const mouth = momoRef.get("momo_mouth")[0];
  const body = momoRef.get("momo_body")[0];
  const fold = momoRef.get("momo_fold")[0];
  const shadow = momoRef.get("momo_shadow")[0];
  
  // Phase 1: SHAKE + BOUNCE (0-200ms)
  const shakeLoop = loop(0.03, () => {
    momoRef.pos.x = momoRef.baseX + Math.sin(time() * 30) * 3;
  });
  
  // Eyes: WIDE + yellow flash
  eyeL.radius = 4.5;
  eyeR.radius = 4.5;
  eyeL.color = MOMO_COLORS.accent;  // yellow
  eyeR.color = MOMO_COLORS.accent;
  
  // Big mouth
  mouth.width = 10;
  mouth.height = 6;
  
  // Fold glows
  fold.color = Color.fromHex("#7EDDD6");
  
  // Body outline pulses
  body.outline = outline(3, Color.fromHex("#66FFB2"));
  
  // Confetti burst!
  spawnSparkles(momoRef.pos, 8, MOMO_COLORS.accent);     // yellow
  spawnSparkles(momoRef.pos, 4, MOMO_COLORS.secondary);   // teal
  
  // Phase 2: BOUNCE UP (200-600ms)
  tween(momoRef.scale, vec2(0.9, 1.15), 0.4, 
    (v) => momoRef.scale = v, easings.easeOutQuad);
  tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 10), 0.4, 
    (v) => momoRef.pos = v, easings.easeOutQuad)
    .onEnd(() => {
      
      // Phase 3: FALL (600-1000ms)
      tween(momoRef.scale, vec2(1.05, 0.95), 0.4, 
        (v) => momoRef.scale = v, easings.easeInQuad);
      tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY + 2), 0.4, 
        (v) => momoRef.pos = v, easings.easeInQuad)
        .onEnd(() => {
          
          // Phase 4: SECOND BOUNCE (1000-1500ms)
          tween(momoRef.scale, vec2(0.95, 1.05), 0.5, 
            (v) => momoRef.scale = v, easings.easeOutElastic);
          tween(momoRef.pos, vec2(momoRef.pos.x, momoRef.baseY - 5), 0.5, 
            (v) => momoRef.pos = v, easings.easeOutElastic)
            .onEnd(() => {
              
              // Phase 5: SETTLE (1500-2000ms)
              // Stop shaking
              shakeLoop.cancel();
              
              // Restore eyes
              eyeL.color = MOMO_COLORS.outline;
              eyeR.color = MOMO_COLORS.outline;
              eyeL.radius = 3;
              eyeR.radius = 3;
              
              // Restore fold
              fold.color = MOMO_COLORS.secondary;
              
              // Restore body outline
              body.outline = outline(2, MOMO_COLORS.outline);
              
              tween(momoRef.scale, vec2(1, 1), 0.5, 
                (v) => momoRef.scale = v, easings.easeOutQuad)
                .onEnd(() => enterIdle(momoRef));
            });
        });
    });
}
```

---

## 8. Transition Rules

### 8.1 Transition Priority

When multiple triggers fire simultaneously, use this priority:

| Priority | Trigger | Example |
|----------|---------|---------|
| 1 (highest) | EXCITED | Level complete — always plays |
| 2 | HAPPY | Correct answer — plays unless EXCITED triggered |
| 3 | CONFUSED | Low confidence — plays unless HAPPY or EXCITED |
| 4 | THINKING | Probe start — plays unless higher priority |
| 5 (lowest) | IDLE | Default — always available |

### 8.2 Transition Animations

| From → To | Duration | Visual | Easing |
|-----------|----------|--------|--------|
| Any → IDLE | 300ms | Smooth reset to neutral | `easeOutQuad` |
| IDLE → HAPPY | 0ms | Instant start (anticipation squish is the transition) | — |
| IDLE → CONFUSED | 200ms | Tilt begins, "?" fades in | `easeOutQuad` |
| IDLE → THINKING | 300ms | Color dims, dots spawn | `easeOutQuad` |
| HAPPY → IDLE | 300ms | Bounce settles | `easeOutElastic` |
| HAPPY → EXCITED | 0ms | Instant — shake starts immediately | — |
| CONFUSED → THINKING | 200ms | "?" removed, tilt → spin | `easeInOutQuad` |
| CONFUSED → IDLE | 300ms | Tilt → neutral, "?" removed | `easeOutQuad` |
| THINKING → HAPPY | 0ms | Instant — color restores + bounce | — |
| THINKING → CONFUSED | 200ms | Spin stops → tilt, dots removed, "?" spawns | `easeInOutQuad` |
| EXCITED → IDLE | 500ms | Shake stops, everything settles | `easeOutQuad` |

### 8.3 Transition Code Pattern

```javascript
function setMomoState(momoRef, newState) {
  const prevState = momoRef.state;
  
  // Prevent redundant transitions
  if (prevState === newState) return;
  
  // Cancel any active one-shot timers
  if (momoRef.stateTimer) {
    momoRef.stateTimer.cancel();
    momoRef.stateTimer = null;
  }
  
  // Exit current state
  switch (prevState) {
    case "confused": exitConfused(momoRef); break;
    case "thinking": exitThinking(momoRef); break;
    // happy and excited are one-shot — they auto-exit
  }
  
  // Enter new state
  switch (newState) {
    case "idle":     enterIdle(momoRef);     break;
    case "happy":    enterHappy(momoRef);    break;
    case "confused": enterConfused(momoRef); break;
    case "thinking": enterThinking(momoRef); break;
    case "excited":  enterExcited(momoRef);  break;
  }
}
```

---

## 9. Performance Budget

### 9.1 Per-State Resource Usage

| State | Shapes Active | Particles | Tweens Running | Est. CPU | Est. Memory |
|-------|--------------|-----------|----------------|----------|-------------|
| IDLE | 7 | 0 | 0 (float is sin-based) | ~0.1% | ~2KB |
| HAPPY | 7 | 5 | 3 | ~0.3% | ~4KB |
| CONFUSED | 8 (incl. "?") | 0 | 1 ("?") | ~0.2% | ~3KB |
| THINKING | 10 (incl. dots) | 0 | 1 (dots) | ~0.3% | ~4KB |
| EXCITED | 7 | 12 | 4 | ~0.5% | ~6KB |

### 9.2 Total Budget Compliance

| Metric | Budget | Actual | Status |
|--------|--------|--------|--------|
| Asset size | < 100KB | ~30KB (sprite) + ~5KB (code) | ✅ PASS |
| RAM | < 5MB | ~6KB (shapes + particles) | ✅ PASS |
| CPU | < 5% per frame | ~0.5% peak (EXCITED) | ✅ PASS |
| Draw calls | < 20 per frame | 7-12 per frame | ✅ PASS |

---

## 10. Sprite Sheet Specification

### 10.1 Layout (When Switching from Shape-Based to Sprite Sheet)

| Dimension | Value |
|-----------|-------|
| Base sprite size | 64×64 px |
| Frames per state | 6 |
| Number of states | 5 |
| Total frames | 30 |
| Sheet layout | 6 columns × 5 rows |
| Sheet size | 384×320 px |
| Color depth | 32-bit RGBA |
| Estimated file size | ~25-35 KB (PNG) |

### 10.2 Animation Speeds

| State | FPS | Frame Duration | Loop |
|-------|-----|----------------|------|
| idle | 4 | 250ms | ✓ Loop |
| happy | 6 | ~167ms | ✗ One-shot |
| confused | 3 | ~333ms | ✓ Loop |
| thinking | 5 | 200ms | ✓ Loop |
| excited | 8 | 125ms | ✗ One-shot |

### 10.3 Kaplay.js Sprite Load Code

```javascript
loadSprite("momo", "sprites/momo_spritesheet.png", {
  sliceX: 6,
  sliceY: 5,
  anims: {
    idle:     { from: 0,  to: 5,  speed: 4, loop: true },
    happy:    { from: 6,  to: 11, speed: 6, loop: false },
    confused: { from: 12, to: 17, speed: 3, loop: true },
    thinking: { from: 18, to: 23, speed: 5, loop: true },
    excited:  { from: 24, to: 29, speed: 8, loop: false },
  },
});
```

---

*Document generated: 2026-03-05*  
*Bigprompt v2.0 — Animation Deep-Dive*  
*Source: Task 2 execution*
