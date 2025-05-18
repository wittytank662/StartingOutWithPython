num = int(input("Choose a number between 1-10. "))

if num > 10:
    print("That is not in the range.")
else:
    if num < 1:
        print("That is not in the range.")
    elif num == 1:
        print("Your number in roman numerals is I")
    elif num == 2:
        print("Your number in roman numerals is II")
    elif num == 3:
        print("Your number in roman numerals is III")
    elif num == 4:
        print("Your number in roman numerals is IV")
    elif num == 5:
        print("Your number in roman numerals is V")
    elif num == 6:
        print("Your number in roman numerals is VI")
    elif num == 7:
        print("Your number in roman numerals is VII")
    elif num == 8:
        print("Your number in roman numerals is VIII")
    elif num == 9:
        print("Your number in roman numerals is IX")
    elif num == 10:
        print("Your number in roman numerals is X")

'''
OUTPUT

Choose a number between 1-10. 5
Your number in roman numerals is V
---------------------------------------------------------------------
Choose a number between 1-10. 50
That is not in the range.
'''