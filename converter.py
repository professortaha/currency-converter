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
    
start = input ("enter the START to start the app or enter ALL (in uppercase) to see list of currencies or enter END (in uppercase) to exit the app: ")

if start.upper() == "ALL":
    convert = get_all_currencies()
elif start.upper() == "END":
    exit()
else:
    convert = convert()