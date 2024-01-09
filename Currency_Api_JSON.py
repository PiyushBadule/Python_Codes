import requests

class CurrencyConverter:
    def __init__(self, api_url):
        """
        Initializes the CurrencyConverter with the given API URL.

        Parameters:
        api_url (str): The URL to fetch currency data from.
        """
        self.api_url = api_url
        self.usd_rates = self.fetch_currency_rates()

    def fetch_currency_rates(self):
        """
        Fetches and returns currency rates from the API URL.

        Returns:
        dict: A dictionary with currency rates keyed by currency codes.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            return {currency: values for currency, values in data['quotes'].items()}
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return {}

    def convert_currency(self, amount, target_currency):
        """
        Converts an amount from USD to the target currency.

        Parameters:
        amount (float): The amount in USD.
        target_currency (str): The target currency code.

        Returns:
        float: The converted amount in the target currency.
        """
        rate = self.usd_rates.get(target_currency)
        if rate:
            return amount * rate
        else:
            print(f"Conversion rate for {target_currency} not found.")
            return 0

def main():
    # Replace 'your_api_url' with your actual API URL
    api_url = "your_api_url"
    converter = CurrencyConverter(api_url)

    # Check and print specific currency rates
    print("USD to INR:", converter.convert_currency(50, 'USDINR'))
    print("USD to EUR:", converter.convert_currency(50, 'USDEUR'))

if __name__ == "__main__":
    main()
