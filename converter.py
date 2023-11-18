import requests

def convert ():
        init_currency = input ("enter the currency you have: ")
        dist_currency = input ("enter the currency you want: ")
        amount = float(input("enter the amount in numbers: "))
        url = "https://api.apilayer.com/fixer/convert?to="+init_currency+"&from="+dist_currency+"&amount="+str(amount)

        payload = {}
        headers= {
        "apikey": "zF5VgnWtLBc96rb5sgGwC95PMh7MhGRk"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.json()

        converted_amount = result['result']

        print(f'{amount} {init_currency} = {converted_amount} {dist_currency}')

def get_all_currencies ():
        url = "https://api.apilayer.com/fixer/symbols"

        payload = {}
        headers= {
        "apikey": "zF5VgnWtLBc96rb5sgGwC95PMh7MhGRk"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        print(result)
        
        convert()

while True:
    start = input("Enter 'START' to start the app, 'ALL' to see the list of currencies, or 'END' to exit the app: ")

    if start.upper() == "ALL":
        get_all_currencies()
    elif start.upper() == "END":
        break  # Exit the loop and end the app
    elif start.upper() == "START":
        convert()
    else:
        print("Invalid input. Please enter 'START', 'ALL', or 'END.")
