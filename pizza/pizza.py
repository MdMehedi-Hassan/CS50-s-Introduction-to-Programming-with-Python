import sys
import os
import csv
from tabulate import tabulate

def main():
    # Ensure exactly one command-line argument is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")

    # Extract the filename from command-line arguments
    filename = sys.argv[1]

    # Check if the file ends with .csv
    if not filename.endswith('.csv'):
        sys.exit("Error: File must be a CSV")

    # Check if the file exists
    if not os.path.exists(filename):
        sys.exit(f"Error: {filename} does not exist")

    # Try reading the CSV file
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # First row contains headers
            data = [row for row in reader]  # Remaining rows contain data
    except Exception as e:
        sys.exit(f"Error reading the CSV file: {e}")

    # Format and print the table using tabulate
    table = tabulate(data, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
