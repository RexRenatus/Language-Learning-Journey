#!/usr/bin/env python3
"""
Create Definition → Character + Pinyin Multiple Choice Flashcards
Generates flashcards where the definition is the question, and user selects matching character + pinyin.
Part of 50/50/50 daily stack: char→pinyin, pinyin→char, def→char+pinyin
"""

import csv
import random
from pathlib import Path
from typing import List, Dict, Tuple

def load_characters(input_file: str) -> List[Dict]:
    """
    Load all characters with definitions from consolidated CSV.

    Returns:
        List of character dictionaries with all fields
    """
    characters = []

    with open(input_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            characters.append({
                'order': int(row['Order Number']),
                'character': row['Item'],
                'pinyin': row['Pinyin'],
                'frequency': int(row['Frequency']),
                'definition': row['Definition'],
                'usage': row['Usage'],
                'part_of_speech': row['Part_of_Speech']
            })

    return characters

def generate_character_distractors(
    target_idx: int,
    all_chars: List[Dict],
    count: int = 5
) -> Tuple[List[Dict], str]:
    """
    Generate 5 character choices including the correct answer.
    Uses frequency proximity + prime offset randomization.

    Args:
        target_idx: Index of target character in all_chars
        all_chars: List of all characters
        count: Number of choices to generate (default 5)

    Returns:
        Tuple of (list of 5 character dicts, correct choice letter A-E)
    """
    target = all_chars[target_idx]
    candidates = []

    # Prime offsets for mathematical randomization
    primes = [7, 11, 13, 17, 19, 23, 29, 31]

    # Start with target character
    candidates.append(target)

    # Generate 4 distractors using frequency proximity + prime offsets
    attempts = 0
    max_attempts = 100

    while len(candidates) < count and attempts < max_attempts:
        attempts += 1

        # Use prime offset to get candidate index
        prime = primes[len(candidates) % len(primes)]
        offset = (target_idx * prime) % len(all_chars)
        candidate_idx = (target_idx + offset) % len(all_chars)

        candidate = all_chars[candidate_idx]

        # Check if already in candidates (no duplicates)
        if any(c['character'] == candidate['character'] for c in candidates):
            continue

        # Check frequency proximity (within ±200 range for better variety)
        freq_diff = abs(candidate['frequency'] - target['frequency'])
        if freq_diff > 200:
            # Try adjacent characters if frequency too different
            for adj_offset in [-1, 1, -2, 2]:
                adj_idx = (candidate_idx + adj_offset) % len(all_chars)
                adj_candidate = all_chars[adj_idx]

                if not any(c['character'] == adj_candidate['character'] for c in candidates):
                    candidate = adj_candidate
                    break

        candidates.append(candidate)

    # Fallback: if still not enough candidates, use nearest characters
    while len(candidates) < count:
        for offset in range(1, len(all_chars)):
            for direction in [1, -1]:
                idx = (target_idx + (offset * direction)) % len(all_chars)
                candidate = all_chars[idx]

                if not any(c['character'] == candidate['character'] for c in candidates):
                    candidates.append(candidate)
                    break

            if len(candidates) >= count:
                break

    # Shuffle candidates to randomize correct answer position
    random.shuffle(candidates)

    # Find correct answer position (A-E)
    correct_idx = next(i for i, c in enumerate(candidates) if c['character'] == target['character'])
    correct_choice = chr(65 + correct_idx)  # 65 = 'A' in ASCII

    return candidates[:count], correct_choice

def create_definition_flashcards(input_file: str, output_file: str):
    """
    Create definition → character + pinyin multiple choice flashcards.

    Args:
        input_file: Path to consolidated_characters_with_definitions.csv
        output_file: Path to output flashcard CSV
    """
    # Load all characters
    print(f"Loading characters from {input_file}...")
    all_characters = load_characters(input_file)
    print(f"Loaded {len(all_characters):,} characters with definitions")

    # Track answer distribution
    answer_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    flashcards = []

    print("\nGenerating flashcards...")
    for idx, target_char in enumerate(all_characters):
        if (idx + 1) % 100 == 0:
            print(f"  Progress: {idx + 1}/{len(all_characters)} flashcards...")

        # Generate 5 character choices with pinyin
        choices, correct_choice = generate_character_distractors(idx, all_characters, count=5)

        # Track answer distribution
        answer_distribution[correct_choice] += 1

        # Create flashcard row
        flashcard = {
            'Order Number': target_char['order'],
            'Definition': target_char['definition'],
            'Part_of_Speech': target_char['part_of_speech'],
            'Correct_Character': target_char['character'],
            'Correct_Pinyin': target_char['pinyin'],
            'Frequency': target_char['frequency'],
            'Usage': target_char['usage'],
            'Choice_A_Char': choices[0]['character'],
            'Choice_A_Pinyin': choices[0]['pinyin'],
            'Choice_B_Char': choices[1]['character'],
            'Choice_B_Pinyin': choices[1]['pinyin'],
            'Choice_C_Char': choices[2]['character'],
            'Choice_C_Pinyin': choices[2]['pinyin'],
            'Choice_D_Char': choices[3]['character'],
            'Choice_D_Pinyin': choices[3]['pinyin'],
            'Choice_E_Char': choices[4]['character'],
            'Choice_E_Pinyin': choices[4]['pinyin'],
            'Correct_Choice': correct_choice
        }

        flashcards.append(flashcard)

    # Write output CSV
    print(f"\nWriting flashcards to {output_file}...")
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        fieldnames = [
            'Order Number', 'Definition', 'Part_of_Speech',
            'Correct_Character', 'Correct_Pinyin', 'Frequency', 'Usage',
            'Choice_A_Char', 'Choice_A_Pinyin',
            'Choice_B_Char', 'Choice_B_Pinyin',
            'Choice_C_Char', 'Choice_C_Pinyin',
            'Choice_D_Char', 'Choice_D_Pinyin',
            'Choice_E_Char', 'Choice_E_Pinyin',
            'Correct_Choice'
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flashcards)

    # Print statistics
    print("\n" + "="*60)
    print("✅ Definition → Character + Pinyin Flashcards Created!")
    print("="*60)
    print(f"\nTotal flashcards: {len(flashcards):,}")
    print(f"CSV columns: 21 (Definition + Part_of_Speech + 5 char+pinyin choices + metadata)")
    print(f"Output file: {output_file}")

    print("\n📊 Answer Distribution (should be ~20% per position):")
    total = len(flashcards)
    for letter in ['A', 'B', 'C', 'D', 'E']:
        count = answer_distribution[letter]
        percentage = (count / total) * 100
        bar = '█' * int(percentage / 2)
        print(f"  {letter}: {count:4d} ({percentage:5.2f}%) {bar}")

    print("\n💡 Daily Practice Stack (50/50/50):")
    print("  • Character → Pinyin:  50 cards/day")
    print("  • Pinyin → Character:  50 cards/day")
    print("  • Definition → Char+Pinyin: 50 cards/day")
    print("  • Total: 150 cards/day")
    print(f"  • Completion: ~{(total / 50):.0f} days (~6 weeks)")
    print("\n✅ Review checkpoint after 1 week to assess card count")

def main():
    # Set random seed for reproducibility in testing
    random.seed(42)

    # Paths
    base_dir = Path("languages/mandarin/ngrams")
    input_file = base_dir / "characters" / "consolidated_characters_with_definitions.csv"
    output_file = base_dir / "flashcards" / "definition_to_character_mc.csv"

    print("="*60)
    print("Definition → Character + Pinyin Flashcard Generator")
    print("="*60)
    print("\nPurpose: Create flashcards for 50/50/50 daily stack")
    print("  • Connects definitions to characters semantically")
    print("  • Reinforces character AND pinyin recognition")
    print("  • Triple exposure per character daily")
    print("\nStrategy:")
    print("  • Frequency-based distractor selection")
    print("  • Prime offset randomization")
    print("  • Full definition text (no truncation)")
    print("  • Visual similarity allowed (builds discrimination)")
    print("  • Pinyin format: Numbered (e.g., de, yi1, ta1)")
    print("  • Front card: Shows character + pinyin for each choice")

    # Create flashcards
    create_definition_flashcards(str(input_file), str(output_file))

    print("\n" + "="*60)
    print("Next steps:")
    print("  1. Import definition_to_character_mc.csv into Anki")
    print("  2. Use provided neural network templates")
    print("  3. Start 50/50/50 daily practice stack")
    print("  4. Review progress after 1 week")
    print("="*60)

if __name__ == "__main__":
    main()
