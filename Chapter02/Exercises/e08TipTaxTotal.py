initCharge = float(input("What is the charge for your food? "))

tip = initCharge * 0.18
salesTax = initCharge * 0.07

totalCharge = initCharge + tip + salesTax

print(f"The initial charge is: {initCharge}")
print()
print(f"Assuming you are tipping 18% the tip will be: {tip:.02f}")
print()
print(f"Assuming the sales tax is 7% the tax would be: {salesTax:.02f}")
print()
print(f"The total charge will be: {totalCharge:.02f}")

'''
OUTPUT

What is the charge for your food? 12.49
The initial charge is: 12.49

Assuming you are tipping 18% the tip will be: 2.25

Assuming the sales tax is 7% the tax would be: 0.87

The total charge will be: 15.61
'''