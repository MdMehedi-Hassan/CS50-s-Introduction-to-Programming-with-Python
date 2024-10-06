import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the input formats
    pattern = r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Parse the two times
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Default minutes to ":00" if missing
    start_minute = start_minute if start_minute else ":00"
    end_minute = end_minute if end_minute else ":00"

    start_time_24 = to_24_hour_format(start_hour, start_minute, start_period)
    end_time_24 = to_24_hour_format(end_hour, end_minute, end_period)

    return f"{start_time_24} to {end_time_24}"

def to_24_hour_format(hour, minute, period):
    hour = int(hour)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}{minute}"

if __name__ == "__main__":
    main()
