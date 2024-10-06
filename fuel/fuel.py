def main():
    # Get user input
    fraction = input("Fraction (X/Y): ")

    # Convert the fraction to a percentage
    try:
        percentage = convert(fraction)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return

    # Display the gauge result
    print(gauge(percentage))


def convert(fraction):
    try:
        # Split the input into X and Y
        X, Y = fraction.split('/')

        # Convert X and Y to integers
        X = int(X)
        Y = int(Y)

        # Raise ValueError if X > Y
        if X > Y:
            raise ValueError("X cannot be greater than Y.")

        # Raise ZeroDivisionError if Y is zero
        if Y == 0:
            raise ZeroDivisionError("Y cannot be zero.")

        # Return percentage rounded to nearest integer
        percentage = (X / Y) * 100
        return round(percentage)

    except ValueError:
        raise ValueError("Invalid input. X and Y must be integers.")


def gauge(percentage):
    # Return "E" if percentage is less than or equal to 1
    if percentage <= 1:
        return "E"

    # Return "F" if percentage is greater than or equal to 99
    elif percentage >= 99:
        return "F"

    # Otherwise, return "Z%" where Z is the percentage
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
 