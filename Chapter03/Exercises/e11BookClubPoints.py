books = int(input('How many books have you purchased this month? '))

if books == 0:
    print('You earned 0 points.')
elif books == 2:
    print('You earned 5 points.')
elif books == 4:
    print('You earned 15 points.')
elif books == 6:
    print('You earned 30 points.')
elif books >= 8:
    print('You earned 60 points!')
    
'''
OUTPUT

How many books have you purchased this month? 10
You earned 60 points!

How many books have you purchased this month? 2
You earned 5 points.
'''