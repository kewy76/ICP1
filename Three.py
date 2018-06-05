# Kate Williams
# 6/5/2018

import random

theNumber = random.randint(0, 9)
userGuess = "10"

while int(userGuess) != int(theNumber):
    userGuess = input("Guess the digit: ")
    if int(userGuess) < int(theNumber):
        print("Your answer is lower than required")
    if int(userGuess) > int(theNumber):
        print("Your answer is higher than required")
    if int(userGuess) == int(theNumber):
        print("Your answer is perfect! Congratulations!")
