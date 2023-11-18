import requests

def get_available_currencies():
    api_key = "zF5VgnWtLBc96rb5sgGwC95PMh7MhGRk"
    url = f"https://api.apilayer.com/fixer/symbols"

    try:
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()

        if result.get('symbols'):
            return result['symbols']
        else:
            print(f"Error: {result.get('error', {}).get('info', 'Unknown error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

def convert_currency(init_currency, dist_currency, amount):
    api_key = "zF5VgnWtLBc96rb5sgGwC95PMh7MhGRk"
    url = f"https://api.apilayer.com/fixer/convert?to={init_currency}&from={dist_currency}&amount={amount}"

    try:
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        if result.get('result'):
            converted_amount = result['result']
            return converted_amount
        else:
            print(f"Error: {result.get('error', {}).get('info', 'Unknown error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

if __name__ == "__main__":
    available_currencies = get_available_currencies()

    if available_currencies:
        print("Available Currencies:")
        for currency, details in available_currencies.items():
            print(f"{currency}: {details['description']}")

        user_choice = input("Enter the currency you have or type 'all' to see all currencies: ").upper()

        if user_choice.upper() == 'ALL':
            for currency, details in available_currencies.items():
                print(f"{currency}: {details['description']}")
        elif user_choice in available_currencies:
            init_currency = user_choice
            dist_currency = input("Enter the currency you want: ").upper()

            try:
                amount = float(input("Enter the amount in numbers: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
                exit()

            converted_amount = convert_currency(init_currency, dist_currency, amount)

            if converted_amount is not None:
                print(f"{amount} {init_currency} = {converted_amount} {dist_currency}")
        else:
            print("Invalid currency code. Please enter a valid currency code or 'all'.")

    else:
        print("Failed to fetch available currencies. Exiting.")
