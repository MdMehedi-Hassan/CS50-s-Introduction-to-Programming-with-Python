# coke.py

def main():
    amount_due = 50  # Total amount to be paid
    accepted_coins = [25, 10, 5]  # Valid coin denominations

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))  # Get coin input from user

        if coin in accepted_coins:  # Check if the inserted coin is valid
            amount_due -= coin  # Reduce the amount due by the coin value

    # Once the loop breaks (amount_due <= 0), calculate and display any change owed
    change_owed = abs(amount_due)  # If amount_due is negative, it means change is owed
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
