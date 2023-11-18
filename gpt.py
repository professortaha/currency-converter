import requests

API_KEY = "zF5VgnWtLBc96rb5sgGwC95PMh7MhGRk"

def make_api_request(url, headers, payload=None):
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()  # Raise an exception for bad responses
    return response

def convert(api_key):
    init_currency = input("Enter the currency you have: ")
    dist_currency = input("Enter the currency you want: ")
    amount = float(input("Enter the amount in numbers: "))
    url = f"https://api.apilayer.com/fixer/convert?to={dist_currency}&from={init_currency}&amount={amount}"

    headers = {"apikey": api_key}

    try:
        response = make_api_request(url, headers)
        result = response.json()
        converted_amount = result['result']
        print(f'{amount} {init_currency} = {converted_amount} {dist_currency}')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def get_all_currencies(api_key):
    url = "https://api.apilayer.com/fixer/symbols"
    headers = {"apikey": api_key}

    try:
        response = make_api_request(url, headers)
        result = response.text
        print(result)
        convert(api_key)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

while True:
    start = input("Enter 'START' to start the app, 'ALL' to see the list of currencies, or 'END' to exit the app: ")

    if start.upper() == "ALL":
        get_all_currencies(API_KEY)
    elif start.upper() == "END":
        break  # Exit the loop and end the app
    elif start.upper() == "START":
        convert(API_KEY)
    else:
        print("Invalid input. Please enter 'START', 'ALL', or 'END.")
