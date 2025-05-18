# weight = mass * 9.8

mass = float(input("Enter the mass of your object in kilograms: "))

weight = mass * 9.8

if weight > 500:
    print("Your object is too heavy.")
elif weight < 100:
    print("Your object is too light")
else:
    print("Your object is a good weight.")

'''
OUTPUT

Enter the mass of your object in kilograms: 40
Your object is a good weight.
---------------------------------------------------------------------
Enter the mass of your object in kilograms: 62 
Your object is too heavy.
---------------------------------------------------------------------
Enter the mass of your object in kilograms: 10
Your object is too light
'''