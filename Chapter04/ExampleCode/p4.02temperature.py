# This program assists a technician in the process
# of checking a substance's temperature.

# Create a variable to represent the maximum
# temperature.
max_temp = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to
# adjust the thermostat.
while temperature > max_temp:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again
# in 15 minutes
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')

'''
OUTPUT

Enter the substance's Celsius temperature: 105.2
The temperature is too high.
Turn the thermostat down and wait
5 minutes. Then take the temperature
again and enter it.
Enter the new Celsius temperature: 104.1
The temperature is too high.
Turn the thermostat down and wait
5 minutes. Then take the temperature
again and enter it.
Enter the new Celsius temperature: 102.4
The temperature is acceptable.
Check it again in 15 minutes.
'''