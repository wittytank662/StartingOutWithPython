priceOfItem1 = float(input("What is the price of your first item? "))
priceOfItem2 = float(input("What is the price of your second item? "))
priceOfItem3 = float(input("What is the price of your third item? "))
priceOfItem4 = float(input("What is the price of your fourth item? "))
priceOfItem5 = float(input("What is the price of your fifth item? "))



subTotal = priceOfItem1 + priceOfItem2 + priceOfItem3 + priceOfItem4 + priceOfItem5

salesTax = subTotal * 0.07

total = subTotal + salesTax

print("Your subtotal is:", subTotal)
print("Your total is:", total)