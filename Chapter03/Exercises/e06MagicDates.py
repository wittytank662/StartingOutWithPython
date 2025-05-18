# if day * month = year
# magic date
# else
# not

day = int(input("Enter a day in numeric form: "))
month = int(input("Enter a month in numeric form: "))
year = int(input("Enter a 2 digit year: "))

if day * month == year:
    print("This is a magic date")
else:
    print("This is not a magic date")

'''
OUTPUT

Enter a day in numeric form: 6
Enter a month in numeric form: 10
Enter a 2 digit year: 60
This is a magic date
---------------------------------------------------------------------
Enter a day in numeric form: 1
Enter a month in numeric form: 2
Enter a 2 digit year: 49
This is not a magic date
'''