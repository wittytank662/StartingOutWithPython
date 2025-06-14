# This program demonstrates an infinite loop.
# Create a variable to control the loop.
keep_going = 'y'

# Warning! Infinite loop!
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    
    # Calculatre the commission.
    commission = sales * comm_rate
    
    # Display the commission.
    print('The commission is $', \
        format(commission, ',.2f'), sep='')
    
'''
OUTPUT

Enter the amount of sales: 500
Enter the commission rate: 10
The commission is $5,000.00
Enter the amount of sales: 50000
Enter the commission rate: 1
The commission is $50,000.00
Enter the amount of sales: 20000
Enter the commission rate: 20000
The commission is $400,000,000.00
'''