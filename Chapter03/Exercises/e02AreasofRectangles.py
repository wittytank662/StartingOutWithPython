# Rectangle area = len * wid

rect1len = float(input("What is the length of the first rectangle? "))
rect1wid = float(input("What is the width of the first rectangle? "))

rect2len = float(input("What is the length of the second rectangle? "))
rect2wid = float(input("What is the width of the second rectangle? "))

rect1area = rect1len * rect1wid
rect2area = rect2len * rect2wid

if rect1area > rect2area:
    print("The first rectangle has a larger area.")
elif rect2area > rect1area:
    print("The second rectangle has a larger area.")
else:
    print("The rectangles have the same area.")