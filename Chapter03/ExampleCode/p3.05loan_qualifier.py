# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0 # The minimum annual salary
min_years = 2        # The minimum years on the job

# Get the customer's annual salary.
salary = float(input("Enter your annual salary:"))

# Get the number of years on the current job.
years_on_job = int(input("Enter the number of" + "years employed:"))

if salary >= min_salary:
    if years_on_job >= min_years:
        print("You qualify for the loan")
    else:
        print("You must have been employed", \
            "for at least", min_years, \
                "years to qualify.")
else:
    print("You must earn at least $", \
        format(min_salary, ",.2f"), \
            " per year to qualify.", sep="")

'''
OUTPUT

Enter your annual salary:29000
Enter the number ofyears employed:5 
You must earn at least $30,000.00 per year to qualify.
---------------------------------------------------------------------
Enter your annual salary:35000
Enter the number ofyears employed:2
You qualify for the loan
---------------------------------------------------------------------
Enter your annual salary:35000
Enter the number ofyears employed:1
You must have been employed for at least 2 years to qualify.
'''