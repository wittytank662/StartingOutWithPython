males = int(input("How many males are in a class? "))
females = int(input("How many females are in a class? "))

students = males + females

malePercent = males / students
femalePercent = females / students

print(f"The percentage of males in your class are: {malePercent:.2%}, and the percentage of females is: {femalePercent:.2%}")

'''
OUTPUT

How many males are in a class? 12
How many females are in a class? 8
The percentage of males in your class are: 60.00%, and the percentage of females is: 40.00%
'''