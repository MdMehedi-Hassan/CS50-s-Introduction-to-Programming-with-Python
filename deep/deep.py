# Get user input
answer = input("What is the answer to the Great Question of Life, the University and Everything? ")

# Print Yes if the user input 42 or (case-insensitively) forty-two or forty two
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")

# Otherwise out No
else:
    print("No")
