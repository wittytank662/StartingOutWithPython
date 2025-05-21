# On a roulette wheel, the pockest are numbered from 0 to 36.
# The colors of the pockets are as follows:
'''
Pocket 0 is green
For pockets 1 through 10, the odd numbered pockets are red and the even numbered pockets are black.
For pockets 11 through 18, the odd numbered pockets are black and the even numbered pockets are red.
For pockets 19 through 28, the odd numbered pockets are red and the even numbered pockets are black.
For pockets 29 through 36, the odd numbered pockets are black and the even numbered pockets are red.
'''
# Write a program that asks the user to enter a pocket number
# and displays whether the pocket is green, red, or black.
# The program should display an error message if the user 
# enters a number that is outside the range of 0 through 36

num = int(input("Choose a number 0-36: "))

if num == 0:
    print("This pocket is green")

if num > 0 and num <= 10:
    if num == 1:
        print("This pocket is red")
    elif num == 2:
        print("This pocket is black")
    elif num == 3:
        print("This pocket is red")
    elif num == 4:
        print("This pocket is black")
    elif num == 5:
        print("This pocket is red")
    elif num == 6:
        print("This pocket is black")
    elif num == 7:
        print("This pocket is red")
    elif num == 8:
        print("This pocket is black")
    elif num == 9:
        print("This pocket is red")
    elif num == 10:
        print("This pocket is black")
        
elif num > 10 and num <= 18:
    if num == 11:
        print("This pocket is black")
    elif num == 12:
        print("This pocket is red")
    elif num == 13:
        print("This pocket is black")
    elif num == 14:
        print("This pocket is red")
    elif num == 15:
        print("This pocket is black")
    elif num == 16:
        print("This pocket is red")
    elif num == 17:
        print("This pocket is black")
    elif num == 18:
        print("This pocket is red")
        
elif num > 18 and num <= 28:
    if num == 19:
        print("This pocket is red")
    elif num == 20:
        print("This pocket is black")
    elif num == 21:
        print("This pocket is red")
    elif num == 22:
        print("This pocket is black")
    elif num == 23:
        print("This pocket is red")
    elif num == 24:
        print("This pocket is black")
    elif num == 25:
        print("This pocket is red")
    elif num == 26:
        print("This pocket is black")
    elif num == 27:
        print("This pocket is red")
    elif num == 28:
        print("This pocket is black")
        
elif num > 28 and num <= 36:
    if num == 29:
        print("This pocket is black")
    elif num == 30:
        print("This pocket is red")
    elif num == 31:
        print("This pocket is black")
    elif num == 32:
        print("This pocket is red")
    elif num == 33:
        print("This pocket is black")
    elif num == 34:
        print("This pocket is red")
    elif num == 35:
        print("This pocket is black")
    elif num == 36:
        print("This pocket is red")
        
elif num < 0 or num > 36:
    print("That is not in the range please try again.")
        
'''
OUTPUT:

Choose a number 0-36: 0
This pocket is green

Choose a number 0-36: 15
This pocket is black

Choose a number 0-36: 200
That is not in the range please try again.
'''