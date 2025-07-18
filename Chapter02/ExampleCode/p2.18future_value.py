# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate.
rate = float(input('Enter the annual interest rate: '))

# Get the number of years that the money will appreciate.
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

# Display the amount needed to deposit.
print('You will need to deposit this amount:', present_value)

'''
OUTPUT

Enter the desired future value: 50000
Enter the annual interest rate: 0.06
Enter the number of years the money will grow: 15
You will need to deposit this amount: 20863.253036777027
'''