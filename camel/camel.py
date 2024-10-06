# Get User input
camelCase = input("camelCase: ")

# Print "snake_case: "
print("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:
    # Check if letter is Upper Case
    if letter.isupper():
        # Print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")
    else:
        # Otherwise, print letter
        print(letter, end="")

# Print newline at the end
print()
