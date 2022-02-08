#To Get your API GO TO  "https://currencylayer.com/"
import json
import requests

response = requests.get("get_your_api_url")
data = response.json()
print(json.dumps(data, indent=2))
for currency, values in data['quotes'].items():
    print(currency, values)

# Save data to dictionary
usd_rates = dict()
for currency, values in data['quotes'].items():
    usd_rates[currency] = values

print(usd_rates)
print(usd_rates['USDINR'])

# Convert USD to EUR
print(50*float(usd_rates['USDEUR']))

# Convert USD to INR
print(50*float(usd_rates['USDINR']))