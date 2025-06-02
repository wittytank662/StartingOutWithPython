lbs = int(input("How much does your package weigh? "))

if lbs <= 2:
    print(f"Your price is: {lbs * 1.50}")
elif lbs > 2 and lbs <= 6:
    print(f"Your price is: {lbs * 3.00}")
elif lbs > 6 and lbs <= 10:
    print(f"Your price is: {lbs * 4.00}")
elif lbs > 10:
    print(f"Your price is: {lbs * 4.75}")
    
'''
OUTPUT

How much does your package weigh? 500
Your price is: 2375.0

How much does your package weigh? 200
Your price is: 950.0
'''