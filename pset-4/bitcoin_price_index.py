import sys
import requests

def main():
    
    try:
        decimal = float(sys.argv[1])
        
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate_float = -1
        
        if "bpi" in o:
            if "USD" in o["bpi"]:
                rate_float = float(o["bpi"]["USD"]["rate_float"])
        
        print(f"${decimal * rate_float:,.4f}")
        
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException as e:
        sys.exit(e)
    except IndexError as e:
        sys.exit("Missing command-line argument")
main()