# Anki Import Instructions - Character to Pinyin Neural Network Flashcards

## Overview
This guide will walk you through importing the Mandarin Character to Pinyin flashcards with the neural network UI theme into Anki. The CSV file (`character_to_pinyin_mc.csv`) contains 1,927 flashcards with definitions, usage examples, and multiple choice options.

---

## Prerequisites

- **Anki Desktop** (version 2.1.60 or later)
- **AnkiMobile** (for iPhone testing, optional)
- **CSV File**: `character_to_pinyin_mc.csv` (1,927 cards)
- **Templates**: `Front_Template.html` and `Back_Template.html`

---

## Step 1: Create Note Type

1. **Open Anki Desktop**
2. Go to **Tools → Manage Note Types**
3. Click **Add**
4. Choose **Add: Basic** (we'll modify it)
5. Name it: `Mandarin_Character_Pinyin_Neural`
6. Click **OK**

---

## Step 2: Add Fields (13 Total)

1. Select your new note type `Mandarin_Character_Pinyin_Neural`
2. Click **Fields...**
3. Click **Add** for each field below **in this exact order**:

   1. `Order Number`
   2. `Item`
   3. `Pinyin`
   4. `Frequency`
   5. `Definition`
   6. `Usage`
   7. `Part_of_Speech`
   8. `Choice_Tone1`
   9. `Choice_Tone2`
   10. `Choice_Tone3`
   11. `Choice_Tone4`
   12. `Choice_Neutral`
   13. `Correct_Answer`

4. Click **Save**

**Note**: The order MUST match your CSV columns exactly for proper import.

---

## Step 3: Configure Card Templates

1. Still in the note type window, click **Cards...** button
2. You'll see the card template editor with 3 sections:
   - **Front Template**
   - **Back Template**
   - **Styling** (we won't use this - CSS is inline)

### Front Template

1. **Delete all existing content** in the Front Template box
2. Open `Front_Template.html` from the template folder
3. **Copy the entire contents** (Ctrl/Cmd + A, then Ctrl/Cmd + C)
4. **Paste into the Front Template box** in Anki

### Back Template

1. **Delete all existing content** in the Back Template box
2. Open `Back_Template.html` from the template folder
3. **Copy the entire contents** (Ctrl/Cmd + A, then Ctrl/Cmd + C)
4. **Paste into the Back Template box** in Anki

### Styling (Leave Empty)

- **Delete all content** in the Styling section
- Leave it completely empty (CSS is inline in the templates)

5. Click **Save**
6. Close the card template editor
7. Close the note types window

---

## Step 4: Import CSV File

1. Go to **File → Import**
2. Browse to your CSV file: `character_to_pinyin_mc.csv`
3. Select the file and click **Open**

### Import Settings

Configure the import dialog as follows:

- **Type**: `Mandarin_Character_Pinyin_Neural` (select from dropdown)
- **Deck**: Choose your target deck (e.g., `Mandarin::Characters` or create a new one)
- **Fields separated by**: **Comma**
- **Allow HTML in fields**: **✓ YES** (check this box)
- **First field is the ID**: **☐ NO** (leave unchecked)
- **Update existing notes when first field matches**: Leave unchecked (unless re-importing)

### Field Mapping

**CRITICAL**: Verify the field mapping matches exactly:

```
CSV Column 1  → Field 1:  Order Number
CSV Column 2  → Field 2:  Item
CSV Column 3  → Field 3:  Pinyin
CSV Column 4  → Field 4:  Frequency
CSV Column 5  → Field 5:  Definition
CSV Column 6  → Field 6:  Usage
CSV Column 7  → Field 7:  Part_of_Speech
CSV Column 8  → Field 8:  Choice_Tone1
CSV Column 9  → Field 9:  Choice_Tone2
CSV Column 10 → Field 10: Choice_Tone3
CSV Column 11 → Field 11: Choice_Tone4
CSV Column 12 → Field 12: Choice_Neutral
CSV Column 13 → Field 13: Correct_Answer
```

**If the mapping is incorrect**, use the dropdown menus to manually map each column to the correct field.

4. Click **Import**
5. Wait for import to complete
6. You should see: **"1,927 notes added"** (or similar confirmation)

---

## Step 5: Verify Cards

1. Go to **Browse** (Ctrl/Cmd + B)
2. In the left sidebar, find your deck (e.g., `Mandarin::Characters`)
3. Click on it to see all 1,927 cards
4. Click on any card in the list
5. Click the **Preview** button (or press P)

### Front Card Verification ✓

- ✅ Neural network background with animated neurons
- ✅ Character displayed in large central neuron (e.g., 的)
- ✅ Order number below character (e.g., "Character #1")
- ✅ Definition text in synapse connection box
- ✅ 5 multiple choice options (A-E) with pinyin
- ✅ Part of speech badge in bottom right corner
- ✅ Blue/cyan color scheme
- ✅ Pulsing glow animations on neuron

### Back Card Verification ✓

- ✅ Character with correct pinyin in parentheses (e.g., 的 (de))
- ✅ Green success state (background shifts to green tones)
- ✅ Checkmark with "CORRECT: de" highlight box
- ✅ Usage examples with bullet points
- ✅ Part of speech badge in bottom right (green border)
- ✅ Success pulse animation on central neuron

---

## Step 6: Test on Anki Desktop

1. Go to your deck
2. Click **Study Now**
3. Review a few cards:
   - Test that tapping/clicking choices doesn't break anything (Anki flips the card on tap)
   - Verify text is readable
   - Check that definitions and usage examples display correctly

---

## Step 7: Sync to AnkiMobile (iPhone 15 Pro)

### Sync from Desktop

1. In Anki Desktop, go to **Tools → Preferences → Network**
2. Ensure you're logged into your AnkiWeb account
3. Click the **Sync** button (top right, cloud icon)
4. Wait for sync to complete

### Sync to iPhone

1. Open **AnkiMobile** on your iPhone 15 Pro
2. Tap the **Sync** button (cloud icon)
3. Sign in with your AnkiWeb credentials if prompted
4. Wait for download to complete

### Test on iPhone

1. Open your deck in AnkiMobile
2. Start studying
3. Verify the following:

#### Display Checks ✓
- ✅ Card fits iPhone 15 Pro screen (6.1", 390×844 logical pixels)
- ✅ No overlap with Dynamic Island (top notch)
- ✅ Bottom elements don't overlap with home indicator
- ✅ Neural network background animates smoothly
- ✅ Character is large and readable (3.5-4rem)
- ✅ Definition text is legible (0.85-0.9rem)
- ✅ Multiple choice buttons are touch-friendly (48-50px height)
- ✅ Pinyin on back card is readable
- ✅ Usage examples don't overflow

#### Performance Checks ✓
- ✅ Animations run smoothly (60fps)
- ✅ No lag when flipping cards
- ✅ Neuron pulse and synapse glow visible
- ✅ Portal rotation effect works
- ✅ Success state transition on back card

#### Interaction Checks ✓
- ✅ Tap to flip front → back works
- ✅ Swipe gestures work (Again/Good/Easy)
- ✅ Choice buttons don't interfere with flip (they're just visual)
- ✅ Scroll works if content exceeds viewport

---

## Troubleshooting

### Issue: Cards show blank or broken layout

**Cause**: Field mapping was incorrect during import

**Solution**:
1. Go to **Browse** → Select all cards
2. **Edit → Delete Notes** (this removes the imported cards)
3. Re-import CSV with correct field mapping (see Step 4)

---

### Issue: Text is cut off or overlaps Dynamic Island

**Cause**: Safe area insets not working or old AnkiMobile version

**Solution**:
1. Update AnkiMobile to latest version (2.0.90+)
2. Restart AnkiMobile after update
3. If still issues, edit templates and increase padding values in CSS

---

### Issue: Animations don't work or look choppy

**Cause**: Device performance or reduced motion settings

**Solution**:
1. Check iPhone **Settings → Accessibility → Motion → Reduce Motion** (should be OFF)
2. Close other apps to free up memory
3. Restart AnkiMobile
4. If persistent, animations can be disabled by editing CSS (see Customization)

---

### Issue: Chinese characters show as boxes (□)

**Cause**: Font not available

**Solution**:
- AnkiMobile should have built-in Chinese font support
- If not, edit template CSS and change font-family:
  ```css
  font-family: "PingFang SC", "Noto Sans SC", sans-serif;
  ```

---

### Issue: Choice buttons too small on iPhone

**Cause**: Touch targets under 48px minimum

**Solution**: Templates already use 48-50px height, but if needed, edit CSS:
```css
.choice-option.neuron-node {
  height: 52px;  /* Increase from 50px */
  font-size: 1.1rem;  /* Increase if needed */
}
```

---

### Issue: Definition text too small to read

**Cause**: Font size too small for mobile

**Solution**: Edit CSS in Front_Template.html:
```css
.definition-text {
  font-size: 1rem;  /* Increase from 0.9rem */
}
```

---

### Issue: Usage examples overflow on back card

**Cause**: Usage text is very long for some characters

**Solution**: Template already uses `overflow-y: auto` and scrolling, but verify:
```css
.usage-synapse {
  max-height: 40vh;  /* Add this if needed */
  overflow-y: auto;
}
```

---

## Customization Guide

### Change Color Scheme

Edit the `:root` variables in both template files:

```css
:root {
  /* Neural Network Colors (Blue/Cyan) */
  --neural-deep: #0a0e27;        /* Background dark blue */
  --neural-mid: #1a1f3a;         /* Background mid blue */
  --neuron-cyan: #00f2fe;        /* Primary accent (cyan) */
  --neuron-blue: #4facfe;        /* Secondary accent (blue) */

  /* Success Colors (Green) */
  --success-primary: #40ff80;    /* Success green */
  --success-glow: rgba(64, 255, 128, 0.4);
}
```

**Example**: Purple/Pink theme
```css
:root {
  --neuron-cyan: #ba68c8;        /* Purple */
  --neuron-blue: #9c27b0;        /* Darker purple */
  --success-primary: #f48fb1;    /* Pink */
}
```

---

### Adjust Font Sizes

Modify these values in the `@media (max-width: 600px)` section:

```css
@media (max-width: 600px) {
  .character-display {
    font-size: 4rem;  /* Character size (increase for larger) */
  }

  .definition-text {
    font-size: 1rem;  /* Definition size (increase for readability) */
  }

  .choice-option.neuron-node {
    font-size: 1.2rem;  /* Choice text size */
  }

  .usage-content {
    font-size: 1rem;  /* Usage text size */
  }
}
```

---

### Disable Animations (for performance)

Add this at the end of the `<style>` section in both templates:

```css
/* Disable all animations */
* {
  animation: none !important;
  transition: none !important;
}

/* Static glow (no pulse) */
.character-neuron {
  box-shadow: 0 0 30px var(--synapse-glow) !important;
}
```

---

### Change Character Neuron Shape

Edit the `.character-neuron` class:

```css
.character-neuron {
  border-radius: 20px;  /* Square with rounded corners (instead of circle) */
  /* OR */
  border-radius: 0;  /* Perfect square */
}
```

---

### Adjust Touch Target Size

Make choice buttons taller for easier tapping:

```css
.choice-option.neuron-node {
  height: 55px;  /* Increase from 50px */
  padding: 0 20px;  /* More padding */
}
```

---

## Export as Anki Package (.apkg)

To share your deck with others or back it up:

1. Go to **File → Export**
2. **Export format**: `Anki Deck Package (*.apkg)`
3. **Include**: Select your deck
4. **Options**:
   - ✓ Include scheduling information (if you want to save progress)
   - ✓ Include media (not needed for this deck)
5. Click **Export**
6. Choose save location
7. Share the `.apkg` file

**Others can import by**: File → Import → Select your `.apkg` file

---

## Success Checklist

Before moving to study:

- ✅ 1,927 cards imported successfully
- ✅ Note type has 13 fields in correct order
- ✅ Front template displays character, definition, 5 choices
- ✅ Back template displays character+pinyin, answer, usage
- ✅ Neural network background is visible and animates
- ✅ Colors are blue/cyan (front) and green (back success state)
- ✅ Part of speech badge displays correctly
- ✅ Order numbers visible (e.g., "Character #1")
- ✅ Mobile display works on iPhone 15 Pro
- ✅ Safe areas respect Dynamic Island (no overlap)
- ✅ Touch targets are 48px+ for multiple choice
- ✅ Animations run smoothly (neurons pulse, synapses glow)
- ✅ Text is readable at all sizes
- ✅ Usage examples display without overflow

---

## Support & Additional Resources

### Anki Documentation
- Official Anki Manual: https://docs.ankiweb.net/
- AnkiMobile Guide: https://docs.ankimobile.net/

### Template Customization
- CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS
- Anki Template Variables: https://docs.ankiweb.net/templates/intro.html

### Common Anki Shortcuts
- **Ctrl/Cmd + B**: Browse cards
- **P**: Preview card (in Browse view)
- **Ctrl/Cmd + Z**: Undo last action
- **Y**: Sync to AnkiWeb
- **Spacebar**: Show answer (during study)
- **1-4**: Rate answer (Again/Hard/Good/Easy)

---

## Next Steps

1. **Start Studying**: Begin with small daily quotas (20-30 cards/day)
2. **Adjust Settings**: Go to deck options and set:
   - New cards per day: 20-30
   - Maximum reviews per day: 200
   - Graduating interval: 1 day
   - Easy interval: 4 days
3. **Track Progress**: Monitor learning stats in Anki's statistics view
4. **Optimize**: After a week, adjust settings based on retention rate (aim for 85-90%)

---

## Credits

- **Template Design**: Neural network theme with portal-inspired UI
- **Character Data**: 1,927 Mandarin characters from Harry Potter corpus
- **Definitions**: Generated via Claude Sonnet 4.5 (OpenRouter API)
- **Optimized for**: iPhone 15 Pro (6.1" display, 390×844 px)

---

**Last Updated**: October 13, 2025
**Template Version**: 1.0
**Compatible with**: Anki 2.1.60+, AnkiMobile 2.0.90+
