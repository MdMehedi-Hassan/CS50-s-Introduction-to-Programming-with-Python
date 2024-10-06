def outdated():
    # List of months to handle full month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        # Prompt user for input
        date_str = input("Enter a date (MM/DD/YYYY or 'Month Day, Year'): ")

        try:
            # First, try to handle the MM/DD/YYYY format
            if "/" in date_str:
                month, day, year = date_str.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            # Handle 'Month Day, Year' format
            elif "," in date_str:
                month_str, day_year = date_str.split(" ", 1)
                day, year = day_year.split(", ")
                month = months.index(month_str) + 1  # Get the month number (1-12)
                day = int(day)
                year = int(year)
            else:
                raise ValueError("Invalid date format")

            # Format the date to YYYY-MM-DD with leading zeroes
            print(f"{year}-{month:02}-{day:02}")
            break  # Exit loop after successful conversion

        except (ValueError, IndexError):
            # If there was any error, re-prompt the user
            print("Invalid date, please try again.")

# Call the function
outdated()
