# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A corect guess will
# terminate the programm.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

# import random

# highest = 10
# answer = random.randint(1, highest)

# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())

# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

import random

highest = 10
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
while True:
    guess = int(input())

    if guess < answer:
        print("Please guess higher")
    elif guess == answer:
        print("Well done, you guessed it")
        break
    elif guess > answer:
        print("Please guess lower")
    elif guess == 0:
        print("Game over")
        break
