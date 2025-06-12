# This program calculates sales commissions

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print('The commission is $', \
    format(commission, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another' + \
    'commission (Enter y for yes): ')

'''
OUTPUT

Enter the amount of sales: 50000
Enter the commission rate: 5
The commission is $250,000.00
Do you want to calculate anothercommission (Enter y for yes): y
Enter the amount of sales: 100
Enter the commission rate: 0.10
The commission is $10.00
Do you want to calculate anothercommission (Enter y for yes): n
'''