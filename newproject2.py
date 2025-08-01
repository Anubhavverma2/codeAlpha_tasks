# -*- coding: utf-8 -*-
"""newproject2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12k-x-6OSZ4OML_BsQDaXjIiV1oRHadeo
"""

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📊 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Type 'done' when you finish entering stocks.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"✅ Added {quantity} shares of {stock}.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

# Calculate total investment
print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")