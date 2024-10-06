import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regex pattern for a valid IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Match the IP against the pattern
    if not re.match(pattern, ip):
        return False

    # Split the IP into its four parts and check if each is within the valid range (0-255)
    parts = ip.split(".")
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True

if __name__ == "__main__":
    main()
