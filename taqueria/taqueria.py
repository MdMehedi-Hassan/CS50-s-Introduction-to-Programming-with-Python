def taqueria():
    # Menu dictionary
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            # Prompt user for input, handling case insensitivity
            item = input("Item: ").title()

            # If the item is on the menu, add the price to the total
            if item in menu:
                total_cost += menu[item]
                print(f"Total: ${total_cost:.2f}")
            else:
                # Ignore invalid items
                pass
        except EOFError:
            # Break the loop when Control-D is pressed
            break

# Call the function
taqueria()
