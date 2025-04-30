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