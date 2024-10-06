# game.py
import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # If input is not an integer, prompt again.

def main():
    # Get the level (upper bound)
    level = get_positive_integer("Level: ")

    # Randomly generate the number between 1 and level
    secret_number = random.randint(1, level)

    # Prompt the user to guess the number
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop once the correct number is guessed

if __name__ == "__main__":
    main()
