from datetime import date, datetime
import inflect
import sys

# Initialize inflect engine for converting numbers to words
p = inflect.engine()

def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Validate date format and check if it's a valid date
    if not validate_date_format(dob):
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        sys.exit(1)  # Exit with code 1 for invalid input

    birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    minutes = calculate_minutes(birth_date)
    print(f"{p.number_to_words(minutes, andword='').capitalize()} minutes")

def validate_date_format(dob):
    """Validate the date format and check if it's a valid date."""
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_minutes(birth_date):
    """Calculate the number of minutes from the birth date to today."""
    today = date.today()
    delta = today - birth_date
    return round(delta.total_seconds() / 60)

if __name__ == "__main__":
    main()
