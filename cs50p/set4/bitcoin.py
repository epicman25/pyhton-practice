import sys
import requests

def main():
    if len(sys.argv) == 2:
        try:
            num = float(sys.argv[1])
            response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
            result = response.json()
            price = result["bpi"]["USD"]["rate_float"]
            total = price * num
            print(f"${total:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except requests.RequestException:
            sys.exit("Failed to retrieve Bitcoin price data")
    else:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()
