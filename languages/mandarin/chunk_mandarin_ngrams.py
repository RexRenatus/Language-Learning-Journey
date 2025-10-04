import csv
import os

def chunk_mandarin_ngrams():
    # Input and output paths
    input_file = "languages/mandarin/ngrams/clean/Mandarin_Ngrams_with_pinyin_tones.csv"
    output_dir = "languages/mandarin/ngrams/chunks"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    chunk_size = 1000  # Number of rows per chunk
    
    print(f"Reading from: {input_file}")
    print(f"Output directory: {output_dir}")
    
    with open(input_file, 'r', encoding='utf-8-sig', newline='') as infile:
        reader = csv.reader(infile)
        
        # Read the header
        header = next(reader)
        print(f"Header: {header}")
        
        chunk_num = 1
        current_chunk = []
        total_rows = 0
        
        for row in reader:
            current_chunk.append(row)
            total_rows += 1
            
            # When we reach chunk_size, write the chunk
            if len(current_chunk) == chunk_size:
                write_chunk(current_chunk, header, chunk_num, output_dir)
                chunk_num += 1
                current_chunk = []
        
        # Write any remaining rows as the final chunk
        if current_chunk:
            write_chunk(current_chunk, header, chunk_num, output_dir)
        
        print(f"\nProcessing complete!")
        print(f"Total rows processed: {total_rows}")
        print(f"Number of chunks created: {chunk_num if current_chunk else chunk_num - 1}")

def write_chunk(chunk, header, chunk_num, output_dir):
    """Write a chunk of data to a CSV file"""
    filename = f"Mandarin_Ngrams_part_{chunk_num:04d}.csv"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8-sig', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write header
        writer.writerow(header)
        
        # Write chunk data
        writer.writerows(chunk)
    
    print(f"Created {filename} with {len(chunk)} rows")

if __name__ == "__main__":
    chunk_mandarin_ngrams()