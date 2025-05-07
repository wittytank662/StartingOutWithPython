# This program compares two strings.
# Get a password from the user.
password = input("Enter the password: ")

# Determine whether the correct password
# was entered.
if password == "prospero":
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
    
'''
OUTPUT

Enter the password: 123password!
Sorry, that is the wrong password.

Enter the password: prospero
Password accepted.
'''