sugar = 1.5 # Cups
butter = 1.0 # Cups
flour = 2.75 # Cups

cookieAmt = int(input("How many cookies do you want to make? "))

amt = cookieAmt / 48

sugar = sugar * amt
butter = butter * amt
flour = flour * amt

print(f"You will need {sugar:.02f}, cups of sugar, {butter:.02f}, cups of butter, and {flour:.02f}, cups of flour")