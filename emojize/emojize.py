# emojize.py
import emoji

def main():
    # Prompt user for a string
    user_input = input("Input: ")

    # Convert any emoji codes or aliases in the input to emoji
    emojized_str = emoji.emojize(user_input, language='alias')

    # Output the "emojized" version of the string
    print(f"Output: {emojized_str}")

if __name__ == "__main__":
    main()
