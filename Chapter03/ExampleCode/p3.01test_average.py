# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.

high_score = 95

# Get the three test scores.

test1 = int(input("Enter the score for test 1: "))
test2 = int(input("Enter the score for test 2: "))
test3 = int(input("Enter the score for test 3: "))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average
print("The average score is", average)

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print("Congratulations!")
    print("That is a great average!")
    

'''
OUTPUT

Enter the score for test 1: 82
Enter the score for test 2: 76
Enter the score for test 3: 91
The average score is 83.0

Enter the score for test 1: 93
Enter the score for test 2: 99
Enter the score for test 3: 96
The average score is 96.0
Congratulations!
That is a great average!
'''