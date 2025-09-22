class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0, 
            'EUR': 0.92,
            'GBP': 0.82,
            'JPY': 150.25,
            'INR': 83.12,
            'CAD': 1.36,
            'AUD': 1.55,
            'AFG': 87.50
        }
    def convert(self, from_currency, to_currency, amount):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ValueError(f"Currency '{from_currency}' is not supported.")
        if to_currency not in self.rates:
            raise ValueError(f"Currency '{to_currency}' is not supported.")
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = amount_in_usd * self.rates[to_currency]
        return round(converted_amount, 2)
def main():
    converter = CurrencyConverter()
    print("Welcome to the Currency Converter!\n")
    print("Available currencies:", ', '.join(converter.rates.keys()))

    from_curr = input("Enter currency you have: ")
    to_curr = input("Enter currency you want: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Error: Amount must be a number.")
        return
    try:
        result = converter.convert(from_curr, to_curr, amount)
        print(f"\n{amount} {from_curr.upper()} = {result} {to_curr.upper()}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
    
