day = int(input("Choose a number 1-7: "))

if day == 1:
    print("The day is monday.")
elif day == 2:
    print("The day is tuesday.")
elif day == 3:
    print("The day is wednesday.")
elif day == 4:
    print("The day is thursday.")
elif day == 5:
    print("The day is friday.")
elif day == 6:
    print("The day is saturday.")
elif day == 7:
    print("The day is sunday.")
else:
    print("That number is not in the range of 1-7.")

'''
OUTPUT

Choose a number 1-7: 5
The day is friday.
---------------------------------------------------------------------
Choose a number 1-7: 10
That number is not in the range of 1-7.
'''