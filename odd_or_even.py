"""
100 days of Python course
DAY 3
"""

number = int(input("Which number do you want to check? "))

# using the modulo function to see that after dividing, remainder is 0
# this means that the number is divisible
if number % 2 == 0:
    print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
    print("This is an odd number.")
