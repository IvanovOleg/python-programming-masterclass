# Write a small programm to ask for a name and age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a polite message refusing them entry.

name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 < age < 31:
    print("Welcome to the party")
else:
    print("Sorry, {}, our party has an age limit.".format(name))
