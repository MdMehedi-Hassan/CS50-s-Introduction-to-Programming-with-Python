import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Regular expression to match the word "um", case-insensitive, as a whole word
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)
if __name__ == "__main__":
    main()
