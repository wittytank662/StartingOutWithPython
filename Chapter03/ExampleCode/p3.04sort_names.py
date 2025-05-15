# This program compares strings with the < operator.
# Get two names from the user.
name1 = input("Enter a name (last name first:)")
name2 = input("Enter another name(last name first):")

# Display the names in alphabetical order.
print("Here are the names, listed alphabetically")

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
    
'''
OUTPUT

Enter a name (last name first:)Cook John  
Enter another name(last name first):Baker Fred
Here are the names, listed alphabetically
Baker Fred
Cook John

'''