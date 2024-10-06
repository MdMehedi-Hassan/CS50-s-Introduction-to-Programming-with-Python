import sys
import csv
import os

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.exists(input_file):
        sys.exit(f"Error: {input_file} does not exist")

    try:
        # Open the input CSV file
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)

            # Prepare to write to the output CSV file
            with open(output_file, 'w', newline='') as outfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                # Write header
                writer.writeheader()

                # Process each row
                for row in reader:
                    last, first = row['name'].split(', ')
                    writer.writerow({'first': first, 'last': last, 'house': row['house']})

    except Exception as e:
        sys.exit(f"Error processing the file: {e}")

if __name__ == "__main__":
    main()
