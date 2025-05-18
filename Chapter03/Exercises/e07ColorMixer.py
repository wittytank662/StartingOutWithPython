color1 = input("Enter the name of a primary color (red, blue, yellow): ")

if color1.lower() not in ["red", "blue", "yellow"]:
    print("That is not a valid primary color.")
    exit()
else:
    color2 = input("Enter another primary color: ")
    if color2.lower() not in ["red", "blue", "yellow"]:
        print("That is not a valid primary color.")
        exit()

if color1 == "red":
    if color2 == "yellow":
        print("You get orange")
    else:
        print("You get blue")
else:
    if color2 == "yellow":
        print("You get green")

'''
OUTPUT

Enter the name of a primary color (red, blue, yellow): red
Enter another primary color: yellow
You get orange
---------------------------------------------------------------------
Enter the name of a primary color (red, blue, yellow): green
That is not a valid primary color.
'''