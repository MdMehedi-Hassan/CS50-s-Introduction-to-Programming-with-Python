def main():
    # Dictionary of fruits and their calorie counts
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt the user for a fruit
    fruit = input("Fruit: ").strip().lower()

    # Output the calories if the fruit is in the dictionary
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    else:
        print("")  # Print an empty string for invalid input


main()
