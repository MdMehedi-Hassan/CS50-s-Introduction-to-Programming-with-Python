import random

def main():
    level = get_level()  # Get the level without printing "Level: "
    score = 0

    # Generate 10 problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # Give user 3 attempts to answer the problem
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Print only the score at the end
    print(score)

def get_level():
    """Prompts for a valid level (1, 2, or 3)."""
    while True:
        try:
            level = int(input())  # No "Level: " text prompt
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Ignore invalid input and reprompt

def generate_integer(level):
    """Generates a random integer based on the level."""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
