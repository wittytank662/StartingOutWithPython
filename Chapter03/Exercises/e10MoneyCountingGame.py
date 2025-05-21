reqAmt = 100

penny = 1
nickel = 5
dime = 10
quarter = 25

pennyAmt = int(input("How many pennies are required to make 1 dollar: "))
nickelAmt = int(input("How many nickles are required to make 1 dollar: "))
dimeAmt = int(input("How many dimes are required to make 1 dollar: "))
quarterAmt = int(input("How many quarters are required to make 1 dollar: "))

if pennyAmt != 100:
    print("That is wrong.")
else:
    print("Correct!")
if nickelAmt != 20:
    print("That is wrong.")
else:
    print("Correct!")
if dimeAmt != 10:
    print("That is wrong.")
else:
    print("Correct!")
if quarterAmt != 4:
    print("That is wrong.")
else:
    print("Correct!")
    
'''
OUTPUT

How many pennies are required to make 1 dollar: 100
How many nickles are required to make 1 dollar: 20
How many dimes are required to make 1 dollar: 5
How many quarters are required to make 1 dollar: 3
Correct!
Correct!
That is wrong.
That is wrong.
'''