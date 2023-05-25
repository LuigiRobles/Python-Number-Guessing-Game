# Number guessing Game

import random as rand


class GuessTheNumber:
    def __init__(self):
        magicNumber = rand.randint(1, 100)
        #print(magicNumber)

        try:
            guess = int(input("Guess a number from 1 to 100: "))
        except:
            guess = int(input("Guess must be a number from 1 to 100: "))

        try:

            while guess != magicNumber:
                guess = int(input("Try again, guess number from 1 to 100: "))
                if guess < magicNumber:
                    print("Too low")
                elif guess > magicNumber:
                    print("Too high")
                else:
                    print("Correct!")
                    break
            else:
                print("First Try!")
        except:
            guess = int(input("Guess must be a number from 1 to 100: "))


GuessTheNumber()
