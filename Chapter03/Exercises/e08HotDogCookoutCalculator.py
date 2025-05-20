# Hot dogs come in packages of 10
# Hot dog buns come in packages of 8

import math

peopleAttending = int(input("How many people will be attending the cookout? "))

hpp = int(input("How many hotdogs will each person have? "))

hotDogsNeeded = peopleAttending * hpp

hotDogPackages = math.ceil(hotDogsNeeded / 10)

hotDogBunsNeeded = hotDogsNeeded

hotDogBunPackages = math.ceil(hotDogBunsNeeded / 8)

leftoverDogs = (hotDogPackages * 10) - hotDogsNeeded

leftoverBuns = (hotDogBunPackages * 8) - hotDogsNeeded


print(f"The minimum number of packages of hot dogs required are: {hotDogsNeeded}")
print(f"The minimum number of packages of hot dog buns required are: {hotDogBunsNeeded}")
print(f"The amount of hot dogs left over are {leftoverDogs}")
print(f"The amount of hot dog buns leftover are {leftoverBuns}")

'''
OUTPUT

How many people will be attending the cookout? 250
How many hotdogs will each person have? 2
The minimum number of packages of hot dogs required are: 500
The minimum number of packages of hot dog buns required are: 500
The amount of hot dogs left over are 0
The amount of hot dog buns leftover are 4
'''