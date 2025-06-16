# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)
    
'''
OUTPUT

Number  Square
--------------
1        1
2        4
3        9
4        16
5        25
6        36
7        49
8        64
9        81
10       100
'''