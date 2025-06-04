quantity = int(input("How many packages did you buy? "))
price = 99 * quantity


if quantity >= 10 and quantity <= 19:
    discount = price * 0.1
elif quantity >= 20 and quantity <= 49:
    discount = price * 0.2
elif quantity >= 50 and quantity <= 99:
    discount = price * 0.3
elif quantity >= 100:
    discount = price * 0.4
    
print(f'Your discount is: {discount}.')
print(f'The total amount of the purchase is: {price - discount}.')

'''
OUTPUT

How many packages did you buy? 10
Your discount is: 99.0.
The total amount of the purchase is: 891.0.
'''