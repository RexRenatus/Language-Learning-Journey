import csv
from pypinyin import lazy_pinyin, Style

# Define input and output paths
input_file = 'ngrams/Mandarin_Ngrams_cleaned.csv'
output_file = 'ngrams/Mandarin_Ngrams_with_pinyin_tones.csv'

# Read the CSV file
rows = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader, None)  # Read header
    for row in reader:
        if row:  # Skip empty rows
            rows.append(row)

# Write the CSV file with pinyin column
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    # Write the new header with Pinyin column before Frequency
    writer.writerow(['Order Number', 'Item', 'Pinyin', 'Frequency'])
    
    # Process each row
    for row in rows:
        if len(row) >= 3:
            order_num = row[0]
            item = row[1]
            frequency = row[2]
            
            # Convert Chinese characters to pinyin with tone numbers
            # Use lazy_pinyin with Style.TONE3 to include numeric tone markers (1-4)
            pinyin_list = lazy_pinyin(item, style=Style.TONE3)
            # Join with space to match the original format
            pinyin = ' '.join(pinyin_list)
            
            # Write the row with pinyin
            writer.writerow([order_num, item, pinyin, frequency])

print(f"Successfully processed {len(rows)} rows")
print(f"Input file: {input_file}")
print(f"Output file: {output_file}")
print("\nFirst 10 rows with pinyin:")

# Display first 10 rows to verify
with open(output_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i < 11:  # Header + first 10 data rows
            print(','.join(row))
        else:
            break