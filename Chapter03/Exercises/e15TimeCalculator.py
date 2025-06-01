totalSeconds = int(input("Enter a number of seconds: "))

days = 0
hours = 0
minutes = 0
seconds = 0

if totalSeconds >= 86400:
    days = totalSeconds // 86400
    totalSeconds = totalSeconds % 86400

if totalSeconds >= 3600:
    hours = totalSeconds // 3600
    totalSeconds = totalSeconds % 3600

if totalSeconds >= 60:
    minutes = totalSeconds // 60
    totalSeconds = totalSeconds % 60

seconds = totalSeconds

print(f'{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).')

'''
OUTPUT

Enter a number of seconds: 100000
1 day(s), 3 hour(s), 46 minute(s), 40 second(s).
'''
