#!/usr/bin/env python3
"""
Script to clean up excessive spaces in pinyin column of chunked CSV files.

This script processes all chunk files and normalizes the spacing in the pinyin column
by replacing multiple consecutive spaces with single spaces.
"""

import csv
import re
from pathlib import Path

def clean_pinyin_spaces(pinyin_text):
    """
    Clean up excessive spaces in pinyin text.
    
    Args:
        pinyin_text (str): The pinyin text with potentially excessive spaces
        
    Returns:
        str: Cleaned pinyin text with normalized spacing
    """
    return re.sub(r'\s+', ' ', pinyin_text.strip())

def process_chunk_file(file_path):
    """
    Process a single chunk file to clean pinyin spaces.
    
    Args:
        file_path (Path): Path to the chunk file to process
    """
    rows = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows.append(header)
        
        for row in reader:
            if len(row) >= 3:
                row[2] = clean_pinyin_spaces(row[2])
            rows.append(row)
    
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"Cleaned {file_path.name}")

def clean_all_chunk_files(chunks_dir):
    """
    Clean pinyin spaces in all chunk files in the specified directory.
    
    Args:
        chunks_dir (str): Path to the chunks directory
    """
    chunks_path = Path(chunks_dir)
    
    if not chunks_path.exists():
        print(f"Error: Chunks directory not found at {chunks_path}")
        return
    
    chunk_files = list(chunks_path.glob("Mandarin_Ngrams_chunk_*.csv"))
    
    if not chunk_files:
        print(f"No chunk files found in {chunks_path}")
        return
    
    print(f"Found {len(chunk_files)} chunk files to process")
    print("-" * 50)
    
    for chunk_file in sorted(chunk_files):
        process_chunk_file(chunk_file)
    
    print(f"\nCompleted cleaning {len(chunk_files)} chunk files")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    chunks_directory = script_dir / "ngrams" / "chunks"
    
    print(f"Chunks directory: {chunks_directory}")
    print("Cleaning excessive spaces in pinyin column...")
    print("-" * 50)
    
    clean_all_chunk_files(str(chunks_directory))