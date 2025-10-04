import csv
import os

# Define input and output paths
input_file = 'ngrams/Mandarin_Ngrams.csv'
output_file = 'ngrams/Mandarin_Ngrams_cleaned.csv'

# Read the CSV file
rows = []
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    # Skip the header row if it exists
    header = next(reader, None)
    for row in reader:
        if row:  # Skip empty rows
            rows.append(row)

# Write the cleaned CSV file with order numbers
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    # Write the new header with Order Number column
    writer.writerow(['Order Number', 'Item', 'Frequency'])
    
    # Process each row
    for index, row in enumerate(rows, start=1):
        if len(row) >= 2:
            # Remove quotation marks from the item column
            item = row[0].strip('"')
            frequency = row[1]
            
            # Write the row with order number
            writer.writerow([index, item, frequency])

print(f"Successfully cleaned {len(rows)} rows")
print(f"Input file: {input_file}")
print(f"Output file: {output_file}")
print("\nFirst 10 rows of cleaned data:")

# Display first 10 rows to verify
with open(output_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i < 11:  # Header + first 10 data rows
            print(','.join(row))
        else:
            break