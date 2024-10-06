import sys

def main():
    # Collect names from the user
    names = []

    print("Enter names (press Ctrl-D to stop):")
    try:
        while True:
            name = input().strip()
            if name:  # Only add non-empty names
                names.append(name)
    except EOFError:
        pass

    # Check if any names were provided
    if not names:
        print("No names were entered.")
        sys.exit()

    # Formulate the farewell message
    if len(names) == 1:
        farewell = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

    # Print the farewell message
    print(farewell)

if __name__ == "__main__":
    main()
