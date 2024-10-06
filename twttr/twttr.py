def omit_vowels(text):
    # Define vowels in both lowercase and uppercase
    vowels = "aeiouAEIOU"

    # Use list comprehension to filter out the vowels from the input text
    return ''.join([char for char in text if char not in vowels])

# Prompt the user for input
text = input("Input: ")

# Output the text without vowels
print("Output:", omit_vowels(text))
