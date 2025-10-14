# Anki Import Instructions: Definition to Character + Pinyin (Neural Network Theme)

Complete setup guide for importing definition → character + pinyin multiple choice flashcards into Anki.

---

## 📋 Overview

**Flashcard Type**: Definition to Character + Pinyin
**Total Cards**: 1,927 characters
**Format**: Multiple choice (5 options: A-E)
**CSV Structure**: 18 columns
**Theme**: Neural Network / Brain Visualization
**Mobile Optimized**: ✅ iPhone 15 Pro tested

**Daily Practice Strategy**: 50/50/50 Stack
- 50 cards: Character → Pinyin
- 50 cards: Pinyin → Character
- 50 cards: Definition → Character + Pinyin (THIS DECK)
- **Total**: 150 cards/day across 3 decks
- **Timeline**: ~6 weeks to complete all 1,927 characters
- **Review Checkpoint**: After 1 week

---

## 📁 Required Files

1. **CSV Data File**:
   - `languages/mandarin/ngrams/flashcards/definition_to_character_mc.csv`
   - 1,927 rows × 18 columns

2. **Anki Templates** (in `.claude/anki-templates/definition-to-character-neural/`):
   - `Front_Template.html` - Definition with 5 character+pinyin choices
   - `Back_Template.html` - Correct answer with success animations

---

## 🎯 Step-by-Step Import Process

### Step 1: Create New Note Type in Anki

1. Open Anki Desktop
2. Click **Tools** → **Manage Note Types**
3. Click **Add**
4. Select **Add: Basic** as the starting template
5. Name it: `Mandarin Definition to Character (Neural)`
6. Click **OK**

### Step 2: Add All Required Fields

Click **Fields** button and add these 18 fields in exact order:

```
1.  Order Number
2.  Definition
3.  Part_of_Speech
4.  Correct_Character
5.  Correct_Pinyin
6.  Frequency
7.  Usage
8.  Choice_A_Char
9.  Choice_A_Pinyin
10. Choice_B_Char
11. Choice_B_Pinyin
12. Choice_C_Char
13. Choice_C_Pinyin
14. Choice_D_Char
15. Choice_D_Pinyin
16. Choice_E_Char
17. Choice_E_Pinyin
18. Correct_Choice
```

**Note**: Delete the default "Front" and "Back" fields that come with Basic template.

### Step 3: Set Up Card Templates

Click **Cards** button to configure front and back templates.

#### **Front Template**

Delete all existing content and paste:

```html
<!-- Mandarin Definition to Character + Pinyin - Neural Network Front Card -->
<div class="neural-frame">
  <!-- Neural background animation -->
  <div class="neural-background">
    <div class="neuron-layer"></div>
    <div class="synapse-layer"></div>
  </div>

  <!-- Rotating portal effect -->
  <div class="portal-effect"></div>

  <!-- Definition Card (Central Display) -->
  <div class="definition-card">
    <div class="card-label">📖 DEFINITION</div>
    <div class="definition-text">{{Definition}}</div>
    <div class="pos-badge">{{Part_of_Speech}}</div>
  </div>

  <!-- Multiple Choice Characters with Pinyin -->
  <div class="choice-neurons">
    <div class="choice-label">SELECT CHARACTER:</div>
    <div class="choice-option neuron-node">
      <span class="choice-letter">A)</span>
      <span class="choice-char">{{Choice_A_Char}}</span>
      <span class="choice-pinyin">({{Choice_A_Pinyin}})</span>
    </div>
    <div class="choice-option neuron-node">
      <span class="choice-letter">B)</span>
      <span class="choice-char">{{Choice_B_Char}}</span>
      <span class="choice-pinyin">({{Choice_B_Pinyin}})</span>
    </div>
    <div class="choice-option neuron-node">
      <span class="choice-letter">C)</span>
      <span class="choice-char">{{Choice_C_Char}}</span>
      <span class="choice-pinyin">({{Choice_C_Pinyin}})</span>
    </div>
    <div class="choice-option neuron-node">
      <span class="choice-letter">D)</span>
      <span class="choice-char">{{Choice_D_Char}}</span>
      <span class="choice-pinyin">({{Choice_D_Pinyin}})</span>
    </div>
    <div class="choice-option neuron-node">
      <span class="choice-letter">E)</span>
      <span class="choice-char">{{Choice_E_Char}}</span>
      <span class="choice-pinyin">({{Choice_E_Pinyin}})</span>
    </div>
  </div>

  <!-- Order Number Badge -->
  <div class="order-badge">Character #{{Order Number}}</div>
</div>

<style>
/* === ANKI MOBILE FIX === */
.card {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--neural-deep);
}

/* === ROOT VARIABLES === */
:root {
  --neural-deep: #0a0e27;
  --neural-mid: #1a1f3a;
  --neuron-cyan: #00f2fe;
  --neuron-blue: #4facfe;
  --synapse-glow: rgba(79, 172, 254, 0.6);
  --synapse-line: rgba(100, 200, 255, 0.3);
  --text-primary: #ffffff;
  --text-secondary: #e0e6ff;
  --text-tertiary: #c0d0ff;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 20px;
  --spacing-xl: 30px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 50%;
}

/* === NEURAL FRAME === */
.neural-frame {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: env(safe-area-inset-top, 20px) env(safe-area-inset-right, 20px)
           env(safe-area-inset-bottom, 20px) env(safe-area-inset-left, 20px);
  background: radial-gradient(ellipse at center, var(--neural-mid) 0%, var(--neural-deep) 100%);
  color: var(--text-primary);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-lg);
  z-index: 1;
  box-sizing: border-box;
}

/* === NEURAL BACKGROUND === */
.neural-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.neuron-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image:
    radial-gradient(circle, var(--neuron-cyan) 2px, transparent 2px),
    radial-gradient(circle, var(--neuron-blue) 1px, transparent 1px);
  background-size: 150px 150px, 200px 200px;
  background-position: 0 0, 50px 50px;
  opacity: 0.25;
  animation: neuron-drift 30s linear infinite;
}

@keyframes neuron-drift {
  from { transform: translate(0, 0); }
  to { transform: translate(50px, 50px); }
}

.synapse-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(90deg, transparent 48%, var(--synapse-line) 50%, transparent 52%),
    linear-gradient(0deg, transparent 48%, var(--synapse-line) 50%, transparent 52%);
  background-size: 100px 100px;
  opacity: 0.12;
  animation: synapse-pulse 3s ease-in-out infinite;
}

@keyframes synapse-pulse {
  0%, 100% { opacity: 0.12; }
  50% { opacity: 0.2; }
}

.portal-effect {
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, transparent 40%, rgba(79, 172, 254, 0.02) 50%, transparent 60%);
  animation: rotate-portal 30s linear infinite;
  pointer-events: none;
  z-index: 0;
}

@keyframes rotate-portal {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* === DEFINITION CARD === */
.definition-card {
  width: 100%;
  max-width: 700px;
  background: linear-gradient(135deg, rgba(30, 50, 90, 0.6), rgba(20, 40, 80, 0.7));
  border: 2px solid var(--neuron-blue);
  border-radius: var(--radius-lg);
  padding: var(--spacing-xl);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(10px);
  z-index: 2;
  box-sizing: border-box;
}

.card-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--neuron-cyan);
  margin-bottom: var(--spacing-md);
  text-align: center;
}

.definition-text {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary);
  text-align: center;
  margin: 0;
}

/* === CHOICE NEURONS === */
.choice-neurons {
  width: 100%;
  max-width: 650px;
  z-index: 2;
  box-sizing: border-box;
}

.choice-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--neuron-cyan);
  text-align: center;
  margin-bottom: var(--spacing-md);
  opacity: 0.9;
}

.choice-option.neuron-node {
  min-height: 50px;
  background: rgba(30, 50, 90, 0.5);
  border: 2px solid var(--synapse-line);
  border-radius: var(--radius-md);
  margin: var(--spacing-sm) 0;
  padding: 0 var(--spacing-lg);
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--text-tertiary);
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  box-sizing: border-box;
}

.choice-letter {
  font-weight: 700;
  color: var(--neuron-cyan);
  min-width: 28px;
}

.choice-char {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
}

.choice-pinyin {
  font-size: 0.9rem;
  color: var(--text-tertiary);
  margin-left: auto;
}

.choice-option.neuron-node:active {
  background: rgba(79, 172, 254, 0.25);
  border: 2px solid var(--neuron-cyan);
  box-shadow: 0 0 20px var(--synapse-glow);
  transform: scale(0.98);
  color: var(--text-primary);
}

/* === ORDER BADGE === */
.order-badge {
  position: absolute;
  bottom: var(--spacing-lg);
  left: var(--spacing-lg);
  padding: 6px 15px;
  background: rgba(79, 172, 254, 0.15);
  border: 1px solid var(--neuron-blue);
  border-radius: 15px;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--neuron-cyan);
  z-index: 3;
  box-sizing: border-box;
}

/* === PART OF SPEECH BADGE === */
.pos-badge {
  display: inline-block;
  padding: 6px 15px;
  background: rgba(79, 172, 254, 0.2);
  border: 1px solid var(--neuron-blue);
  border-radius: 15px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--neuron-cyan);
  margin-top: var(--spacing-md);
  box-sizing: border-box;
}

/* === MOBILE RESPONSIVE === */
@media (max-width: 600px) {
  .neural-frame {
    padding: env(safe-area-inset-top, 16px) env(safe-area-inset-right, 12px)
             env(safe-area-inset-bottom, 16px) env(safe-area-inset-left, 12px);
    gap: var(--spacing-md);
  }

  .definition-card {
    padding: var(--spacing-lg);
  }

  .definition-text {
    font-size: 0.9rem;
  }

  .choice-option.neuron-node {
    min-height: 48px;
    font-size: 1rem;
    padding: 0 var(--spacing-md);
  }

  .choice-char {
    font-size: 1.3rem;
  }

  .choice-pinyin {
    font-size: 0.85rem;
  }

  .order-badge {
    bottom: var(--spacing-md);
    left: var(--spacing-md);
    font-size: 0.6rem;
    padding: 4px 12px;
  }
}

/* === ACCESSIBILITY === */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
</style>
```

#### **Back Template**

Delete all existing content and paste:

```html
<!-- Mandarin Definition to Character + Pinyin - Neural Network Back Card -->
<div class="neural-frame neural-success">
  <!-- Neural background (success state) -->
  <div class="neural-background success-state">
    <div class="neuron-layer active"></div>
    <div class="synapse-layer glowing"></div>
  </div>

  <!-- Portal effect (success) -->
  <div class="portal-effect success"></div>

  <!-- Character + Pinyin Answer -->
  <div class="answer-neuron">
    <div class="answer-char">{{Correct_Character}}</div>
    <div class="answer-pinyin">({{Correct_Pinyin}})</div>
  </div>

  <!-- Correct Choice Indicator -->
  <div class="correct-indicator">
    <span class="checkmark">✓</span>
    <span class="correct-text">CORRECT:</span>
    <span class="correct-choice">{{Correct_Choice}}</span>
  </div>

  <!-- Usage Examples -->
  <div class="usage-card">
    <div class="usage-label">USAGE:</div>
    <div class="usage-content">{{Usage}}</div>
    <div class="pos-badge">{{Part_of_Speech}}</div>
  </div>

  <!-- Order Number Badge -->
  <div class="order-badge">Character #{{Order Number}}</div>
</div>

<style>
/* === ANKI MOBILE FIX === */
.card {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--neural-deep);
}

/* === ROOT VARIABLES === */
:root {
  --neural-deep: #0a0e27;
  --neural-mid: #1a1f3a;
  --neuron-cyan: #00f2fe;
  --neuron-blue: #4facfe;
  --synapse-glow: rgba(79, 172, 254, 0.6);
  --synapse-line: rgba(100, 200, 255, 0.3);
  --success-primary: #40ff80;
  --success-glow: rgba(64, 255, 128, 0.4);
  --success-bg: rgba(40, 200, 80, 0.12);
  --text-primary: #ffffff;
  --text-secondary: #e0e6ff;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 20px;
  --spacing-xl: 30px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 50%;
}

/* === NEURAL FRAME === */
.neural-frame {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: env(safe-area-inset-top, 20px) env(safe-area-inset-right, 20px)
           env(safe-area-inset-bottom, 20px) env(safe-area-inset-left, 20px);
  background: radial-gradient(ellipse at center, var(--neural-mid) 0%, var(--neural-deep) 100%);
  color: var(--text-primary);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-lg);
  z-index: 1;
  box-sizing: border-box;
}

/* === NEURAL BACKGROUND (Success State) === */
.neural-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.neuron-layer.active {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image:
    radial-gradient(circle, var(--success-primary) 2px, transparent 2px),
    radial-gradient(circle, var(--success-primary) 1px, transparent 1px);
  background-size: 150px 150px, 200px 200px;
  background-position: 0 0, 50px 50px;
  opacity: 0.3;
  animation: neuron-activate 2s ease-out forwards;
}

@keyframes neuron-activate {
  0% {
    opacity: 0.2;
    transform: scale(0.95);
  }
  100% {
    opacity: 0.3;
    transform: scale(1);
  }
}

.synapse-layer.glowing {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(90deg, transparent 48%, var(--success-glow) 50%, transparent 52%),
    linear-gradient(0deg, transparent 48%, var(--success-glow) 50%, transparent 52%);
  background-size: 100px 100px;
  opacity: 0.15;
  animation: synapse-success 1.5s ease-out forwards;
}

@keyframes synapse-success {
  0% { opacity: 0.1; }
  50% { opacity: 0.25; }
  100% { opacity: 0.15; }
}

.portal-effect.success {
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, transparent 40%, rgba(64, 255, 128, 0.03) 50%, transparent 60%);
  animation: portal-success 2s ease-out forwards;
  pointer-events: none;
  z-index: 0;
}

@keyframes portal-success {
  0% {
    transform: rotate(0deg) scale(0.9);
    opacity: 0;
  }
  100% {
    transform: rotate(180deg) scale(1);
    opacity: 1;
  }
}

/* === ANSWER NEURON === */
.answer-neuron {
  width: 200px;
  height: 200px;
  border-radius: var(--radius-full);
  background: radial-gradient(circle, rgba(64, 255, 128, 0.2) 0%, rgba(40, 180, 90, 0.3) 100%);
  border: 3px solid var(--success-primary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-sm);
  position: relative;
  z-index: 2;
  box-shadow: 0 0 40px var(--success-glow);
  animation: success-pulse 2s ease-in-out infinite;
}

@keyframes success-pulse {
  0%, 100% {
    box-shadow: 0 0 40px var(--success-glow);
    transform: scale(1);
  }
  50% {
    box-shadow: 0 0 60px var(--success-glow);
    transform: scale(1.02);
  }
}

.answer-char {
  font-size: 4rem;
  font-weight: 700;
  color: var(--text-primary);
  text-shadow: 0 0 20px var(--success-glow);
  line-height: 1;
}

.answer-pinyin {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--success-primary);
  text-shadow: 0 0 10px var(--success-glow);
  line-height: 1;
}

/* === CORRECT CHOICE INDICATOR === */
.correct-indicator {
  background: linear-gradient(135deg, rgba(40, 200, 80, 0.3), rgba(30, 150, 60, 0.4));
  border: 2px solid var(--success-primary);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg) var(--spacing-xl);
  box-shadow: 0 4px 30px rgba(64, 255, 128, 0.3);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-md);
  z-index: 2;
}

.checkmark {
  font-size: 1.5rem;
  color: var(--success-primary);
}

.correct-text {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.correct-choice {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: var(--radius-full);
  background: var(--success-primary);
  color: var(--neural-deep);
  font-weight: 700;
  font-size: 1.1rem;
  margin-left: var(--spacing-sm);
}

/* === USAGE CARD === */
.usage-card {
  width: 100%;
  max-width: 650px;
  background: linear-gradient(135deg, rgba(30, 50, 90, 0.6), rgba(20, 40, 80, 0.7));
  border: 1px solid rgba(64, 255, 128, 0.3);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg) var(--spacing-xl);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  z-index: 2;
  box-sizing: border-box;
}

.usage-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--success-primary);
  margin-bottom: var(--spacing-md);
}

.usage-content {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
}

/* === PART OF SPEECH BADGE (Success State) === */
.pos-badge {
  display: inline-block;
  padding: 6px 15px;
  background: rgba(64, 255, 128, 0.2);
  border: 1px solid var(--success-primary);
  border-radius: 15px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--success-primary);
  margin-top: var(--spacing-md);
  box-sizing: border-box;
}

/* === ORDER NUMBER BADGE === */
.order-badge {
  position: absolute;
  bottom: var(--spacing-lg);
  left: var(--spacing-lg);
  padding: 6px 15px;
  background: rgba(64, 255, 128, 0.15);
  border: 1px solid var(--success-primary);
  border-radius: 15px;
  font-size: 0.65rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: rgba(64, 255, 128, 0.8);
  z-index: 3;
  box-sizing: border-box;
}

/* === MOBILE RESPONSIVE === */
@media (max-width: 600px) {
  .neural-frame {
    padding: env(safe-area-inset-top, 16px) env(safe-area-inset-right, 12px)
             env(safe-area-inset-bottom, 16px) env(safe-area-inset-left, 12px);
    gap: var(--spacing-md);
  }

  .answer-neuron {
    width: 170px;
    height: 170px;
  }

  .answer-char {
    font-size: 3.5rem;
  }

  .answer-pinyin {
    font-size: 1.1rem;
  }

  .correct-indicator {
    padding: var(--spacing-md) var(--spacing-lg);
    gap: var(--spacing-sm);
  }

  .correct-text {
    font-size: 0.9rem;
  }

  .correct-choice {
    width: 32px;
    height: 32px;
    font-size: 1rem;
  }

  .usage-card {
    padding: var(--spacing-md) var(--spacing-lg);
  }

  .usage-content {
    font-size: 0.85rem;
  }

  .order-badge {
    bottom: var(--spacing-md);
    left: var(--spacing-md);
    font-size: 0.6rem;
    padding: 4px 12px;
  }
}

/* === ACCESSIBILITY === */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
</style>
```

Click **Save** to close the template editor.

### Step 4: Import CSV Data

1. From Anki main window, click **File** → **Import**
2. Navigate to: `languages/mandarin/ngrams/flashcards/definition_to_character_mc.csv`
3. Click **Open**

**Import Settings**:
- **Type**: `Mandarin Definition to Character (Neural)`
- **Deck**: Choose your target deck (or create new: "Mandarin Definition to Character")
- **Fields separated by**: `Comma`
- **Allow HTML in fields**: ✅ Checked
- **First line is field names**: ✅ Checked

**Field Mapping** (should auto-map if field names match):
```
CSV Column                 → Anki Field
─────────────────────────────────────────────
Order Number               → Order Number
Definition                 → Definition
Part_of_Speech             → Part_of_Speech
Correct_Character          → Correct_Character
Correct_Pinyin             → Correct_Pinyin
Frequency                  → Frequency
Usage                      → Usage
Choice_A_Char              → Choice_A_Char
Choice_A_Pinyin            → Choice_A_Pinyin
Choice_B_Char              → Choice_B_Char
Choice_B_Pinyin            → Choice_B_Pinyin
Choice_C_Char              → Choice_C_Char
Choice_C_Pinyin            → Choice_C_Pinyin
Choice_D_Char              → Choice_D_Char
Choice_D_Pinyin            → Choice_D_Pinyin
Choice_E_Char              → Choice_E_Char
Choice_E_Pinyin            → Choice_E_Pinyin
Correct_Choice             → Correct_Choice
```

4. Click **Import**
5. Verify: "1927 notes added" confirmation

---

## ✅ Verification Steps

### Desktop Preview

1. Click **Browse** in Anki
2. Find your "Mandarin Definition to Character" deck
3. Select any card
4. Click **Preview** button
5. Verify:
   - ✅ Definition displays in blue card
   - ✅ 5 choices show "character (pinyin)" format
   - ✅ Neural network background animations visible
   - ✅ Back card shows correct character + pinyin
   - ✅ Green success state animations on back

### Mobile Testing

1. Sync deck to AnkiMobile/AnkiDroid
2. Open deck and start studying
3. Verify:
   - ✅ Definition card fills entire screen
   - ✅ All 5 choices visible and tappable
   - ✅ Touch targets feel comfortable (48-50px)
   - ✅ Text is readable without zooming
   - ✅ Back card success animations play smoothly

---

## 📊 CSV Data Structure

**File**: `definition_to_character_mc.csv`
**Rows**: 1,927 characters
**Columns**: 18 fields

### Column Details

| Column # | Field Name | Description | Example |
|----------|------------|-------------|---------|
| 1 | Order Number | Frequency-based order (1-1927) | `1` |
| 2 | Definition | Full English definition | `Possessive particle...` |
| 3 | Part_of_Speech | Grammatical category | `particle` |
| 4 | Correct_Character | The correct character | `的` |
| 5 | Correct_Pinyin | Correct pronunciation | `de` |
| 6 | Frequency | Occurrence count in corpus | `3678` |
| 7 | Usage | Example sentences | `Used in phrases like...` |
| 8-9 | Choice_A_Char, Choice_A_Pinyin | Option A | `的`, `de` |
| 10-11 | Choice_B_Char, Choice_B_Pinyin | Option B | `地`, `di4` |
| 12-13 | Choice_C_Char, Choice_C_Pinyin | Option C | `得`, `de2` |
| 14-15 | Choice_D_Char, Choice_D_Pinyin | Option D | `底`, `di3` |
| 16-17 | Choice_E_Char, Choice_E_Pinyin | Option E | `第`, `di4` |
| 18 | Correct_Choice | Answer key (A/B/C/D/E) | `A` |

### Answer Distribution
- **A**: 384 cards (19.93%)
- **B**: 396 cards (20.55%)
- **C**: 403 cards (20.91%)
- **D**: 380 cards (19.72%)
- **E**: 364 cards (18.89%)

Well-balanced across all positions.

---

## 🎨 Design Features

### Visual Theme
- **Concept**: Walking through a networked brain
- **Colors**: Deep blue space (#0a0e27) with cyan neurons (#00f2fe)
- **Success State**: Green glow (#40ff80) when correct
- **Animations**: 60fps GPU-accelerated

### Front Card Elements
1. **Neural Background**: Animated particle grid with synaptic connections
2. **Definition Card**: Central blue gradient card with definition text
3. **Choice Neurons**: 5 options with character + pinyin in clickable nodes
4. **Part of Speech Badge**: Upper right corner label
5. **Order Badge**: Lower left frequency-based order number

### Back Card Elements
1. **Success Background**: Green activated neurons
2. **Answer Neuron**: Large pulsing circle with character + pinyin
3. **Correct Indicator**: Checkmark + correct choice letter (A-E)
4. **Usage Card**: Example sentences with part of speech
5. **Order Badge**: Maintains position from front

### Accessibility
- Reduced motion support for users with vestibular disorders
- High contrast ratios (WCAG AA compliant)
- Touch targets meet mobile accessibility standards (48-50px)

---

## 🔧 Troubleshooting

### Issue: Cards appear blank on mobile
**Solution**: Ensure you're using Anki 2.1.50+ with mobile sync enabled. Try rebuilding deck cache.

### Issue: Chinese characters display as boxes
**Solution**: Install "Noto Sans SC" font on your device, or the template will fall back to system fonts.

### Issue: Animations not playing
**Solution**: Check if "Reduced Motion" is enabled in device accessibility settings. Template respects this preference.

### Issue: Field mapping incorrect on import
**Solution**: Ensure CSV has exact field names with underscores (e.g., `Choice_A_Char` not `Choice A Char`). Delete first import attempt and re-import with corrected mapping.

### Issue: Definition text too long/overflowing
**Solution**: Template uses full definition length. If overflow occurs, text will scroll vertically within card bounds.

---

## 📈 Study Strategy

### 50/50/50 Daily Stack
**Total**: 150 cards per day across 3 decks

1. **Character → Pinyin** (50 cards)
   - Tests: Pinyin recall from character
   - Deck: `Mandarin Character to Pinyin (Neural)`

2. **Pinyin → Character** (50 cards)
   - Tests: Character recall from pinyin
   - Deck: `Mandarin Pinyin to Character (Neural)`

3. **Definition → Character + Pinyin** (50 cards - THIS DECK)
   - Tests: Semantic connection (meaning → form + sound)
   - Deck: `Mandarin Definition to Character (Neural)`

### Timeline
- **Daily**: 150 new cards + reviews
- **Weekly**: 1,050 total exposures
- **1 Week Checkpoint**: Assess if 50/50/50 is sustainable or needs adjustment
- **6 Weeks**: Complete all 1,927 characters × 3 formats = 5,781 total cards

### Benefits of Triple Exposure
- **Character Recognition**: See same character 3× daily in different contexts
- **Semantic Anchoring**: Definition cards build meaning association
- **Pronunciation Reinforcement**: Pinyin shown on all 3 card types
- **Character Discrimination**: Multiple choice builds visual differentiation skill

---

## 📝 Notes

- **Pinyin Format**: Numbered tones (de, yi1, ta1) for consistency with other decks
- **Distractor Selection**: Frequency proximity (±200 range) with prime offset randomization
- **No Visual Filtering**: Intentionally includes similar-looking characters to build discrimination
- **Full Definitions**: Complete definition text maintained for semantic depth
- **Source**: Harry Potter Mandarin corpus (21,070 n-grams)

---

## 🎯 Success Checklist

Before starting study, verify:

- [ ] All 1,927 cards imported successfully
- [ ] Front card shows definition + 5 choices with character (pinyin)
- [ ] Back card shows correct character + pinyin with green glow
- [ ] Mobile display works correctly (no blank cards)
- [ ] Touch targets feel comfortable on mobile
- [ ] Neural network animations play smoothly
- [ ] Part of speech badges display correctly
- [ ] Usage examples visible on back card

---

**Ready to Begin!** 🚀

Start with 50 cards daily and assess progress after 1 week. Adjust card count based on:
- Retention rate (aim for 80-90%)
- Time commitment (target 30-45 min/day total)
- Mental fatigue (should feel challenging but not overwhelming)

Good luck with your Mandarin learning journey! 加油! (jiā yóu - keep it up!)
