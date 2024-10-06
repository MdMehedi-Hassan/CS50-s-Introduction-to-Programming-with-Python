def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Plates must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Plates must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # All characters must be alphanumeric
    if not s.isalnum():
        return False

    # Numbers cannot be in the middle (first number must be at the end)
    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == '0':  # The first number cannot be a zero
                return False
            break
        if s[i].isalpha() and any(char.isdigit() for char in s[i:]):
            return False

    return True


if __name__ == "__main__":
    main()
