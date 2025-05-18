# Enter someones age
# Display whether the person is an infant, child, teenager, or adult.

age = int(input("Please enter someones age: "))

if age <= 1:
    print("That person is an infant.")
elif age > 1 and age < 13:
    print("That person is a child.")
elif age > 13 and age < 20:
    print("That person is a teenager.")
elif age > 20 and age < 110:
    print("That person is an adult")
else:
    print("Please enter a valid age.")

'''
OUTPUT

Please enter someones age: 1
That person is an infant.
---------------------------------------------------------------------
Please enter someones age: 16
That person is a teenager.
---------------------------------------------------------------------
Please enter someones age: 5000
Please enter a valid age.
'''