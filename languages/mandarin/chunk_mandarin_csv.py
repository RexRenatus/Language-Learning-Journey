#!/usr/bin/env python3
"""
Script to break down Mandarin N-grams CSV into 1000-word chunks.

This script reads the Mandarin_Ngrams_with_pinyin_tones.csv file and splits it
into smaller CSV files, each containing approximately 1000 rows (excluding header).
"""

import csv
import os
from pathlib import Path

def chunk_csv_file(input_file, output_dir, chunk_size=1000):
    """
    Split a CSV file into chunks of specified size.
    
    Args:
        input_file (str): Path to the input CSV file
        output_dir (str): Directory to save the chunked files
        chunk_size (int): Number of rows per chunk (default: 1000)
    """
    input_path = Path(input_file)
    output_path = Path(output_dir)
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        chunk_num = 1
        row_count = 0
        current_chunk = []
        
        for row in reader:
            current_chunk.append(row)
            row_count += 1
            
            if row_count == chunk_size:
                output_file = output_path / f"Mandarin_Ngrams_chunk_{chunk_num:03d}.csv"
                
                with open(output_file, 'w', encoding='utf-8', newline='') as chunk_file:
                    writer = csv.writer(chunk_file)
                    writer.writerow(header)
                    writer.writerows(current_chunk)
                
                print(f"Created {output_file} with {row_count} rows")
                
                chunk_num += 1
                row_count = 0
                current_chunk = []
        
        if current_chunk:
            output_file = output_path / f"Mandarin_Ngrams_chunk_{chunk_num:03d}.csv"
            
            with open(output_file, 'w', encoding='utf-8', newline='') as chunk_file:
                writer = csv.writer(chunk_file)
                writer.writerow(header)
                writer.writerows(current_chunk)
            
            print(f"Created {output_file} with {row_count} rows")
    
    print(f"\nChunking complete! Created {chunk_num} chunk files in {output_dir}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    input_csv = script_dir / "ngrams" / "clean" / "Mandarin_Ngrams_with_pinyin_tones.csv"
    output_directory = script_dir / "ngrams" / "chunks"
    
    if not input_csv.exists():
        print(f"Error: Input file not found at {input_csv}")
        exit(1)
    
    print(f"Input file: {input_csv}")
    print(f"Output directory: {output_directory}")
    print(f"Chunk size: 1000 rows per file")
    print("-" * 50)
    
    chunk_csv_file(str(input_csv), str(output_directory), chunk_size=1000)