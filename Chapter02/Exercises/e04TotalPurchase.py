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

'''
OUTPUT

What is the price of your first item? 99.99
What is the price of your second item? 24.99
What is the price of your third item? 14.99
What is the price of your fourth item? 5.49
What is the price of your fifth item? 6.99
Your subtotal is: 152.45000000000002
Your total is: 163.12150000000003
'''