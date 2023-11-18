import requests

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