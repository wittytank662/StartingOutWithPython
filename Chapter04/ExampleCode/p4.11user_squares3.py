# This program uses a loop to display a
# table of numbers and their squares.

# Get the starting value.
print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))

# Get the ending limit.
end = int(input('How high should I go?'))

# Print the table headings.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(start, end+1):
    square = number**2
    print(number, '\t', square)

'''
OUTPUT

This program displays a list of numbers
and their squares.
Enter the starting number: 5
How high should I go?10

Number  Square
--------------
5        25
6        36
7        49
8        64
9        81
10       100
'''