"""
100 days of Python course
DAY 3
"""

year = int(input("Which year do you want to check? "))

# Refer to the flow chart here: https://bit.ly/36BjS2D
# the logic seems complicated, but using nested if / else
# statements and thinking like a computer it then makes sense
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
