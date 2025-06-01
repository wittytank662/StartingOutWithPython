weight = int(input("Enter your weight in lbs: "))
height = int(input("Enter your height in inches: "))

BMI = weight * (703/(height ** 2))

if BMI < 18.5:
    print("You are underweight.")
if BMI >= 18.5 and BMI <= 25:
    print("You have the optimal weight.")
elif BMI > 25:
    print("You are overweight.")
    
'''
OUTPUT

Enter your weight in lbs: 100
Enter your height in inches: 64
You are underweight.

'''