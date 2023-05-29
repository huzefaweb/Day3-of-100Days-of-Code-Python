"""
100 days of Python course
DAY 3
"""

# this program allows for users to have multiple choices
# regarding size and toppings using logical if / elif / else flow
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# running pylint, bill is detected as a constant variable and should be
# in uppercase: we will learn about this in a future lesson - leave as
# is because the program still executes without errors
bill = 0

# learning that instead of e.g. bill = bill + 15 use shorter notation
# note that errors will occur if user does not input capital letters
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

# use f-string to show result: note that no decimal numbers generated
print(f"Your final bill is: ${bill}.")
