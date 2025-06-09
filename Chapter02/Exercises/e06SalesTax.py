price = float(input("What is the amount of money that you spent? (00.00) "))

# state tax is 5% (0.05)
# Country tax is 2.5% (0.025)
# Display amount of the purchase, state sales tax, country sales tax, total sales tax, total sale.

stateTax = price * 0.05
countryTax = price * 0.025

totalTax = stateTax + countryTax

totalPrice = totalTax + price

print()
print(f"The price is: ${price}, the state tax is: ${stateTax:.02f}, and the country tax is: ${countryTax:.02f}")
print()
print(f"The total amount of tax is: ${totalTax:.02f}, and your total is: ${totalPrice:.02f}.")

'''
OUTPUT

What is the amount of money that you spent? (00.00) 49.99

The price is: $49.99, the state tax is: $2.50, and the country tax is: $1.25

The total amount of tax is: $3.75, and your total is: $53.74.
'''