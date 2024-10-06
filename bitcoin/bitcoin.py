import sys
import requests

def main():
    # Check if the user provided the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number of bitcoins>")

    # Get the number of Bitcoins the user wants to buy
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid number of Bitcoins. Please enter a valid float.")

    # Fetch the current Bitcoin price from CoinDesk API
    try:
        price = get_bitcoin_price()
    except requests.RequestException:
        sys.exit("Error: Unable to retrieve Bitcoin price.")

    # Calculate the cost of the specified number of Bitcoins
    cost = num_bitcoins * price

    # Print the cost formatted with commas and four decimal places
    print(f"${cost:,.4f}")

def get_bitcoin_price():
    """Fetch the current Bitcoin price in USD from the CoinDesk API."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response and extract the current price of Bitcoin in USD
    data = response.json()
    return float(data["bpi"]["USD"]["rate"].replace(",", ""))

if __name__ == "__main__":
    main()
