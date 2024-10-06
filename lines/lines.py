import sys
import os

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if the file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        # Count lines of code
        loc = count_lines(filename)
        print(loc)
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(filename):
    """Count the number of lines of code in a Python file, excluding comments and blank lines."""
    loc = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            # Ignore blank lines and comments
            if line and not line.startswith("#"):
                loc += 1
    return loc

if __name__ == "__main__":
    main()
