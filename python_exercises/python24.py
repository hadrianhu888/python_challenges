import random as rd 
import io

def guessRandomNumber(): 
    randomNumber = rd.randint(1,10)
    userGuess = 0 
    while (randomNumber != userGuess):
        userGuess = int(input("Enter a number: "))
        if (userGuess > randomNumber):
            print("Keep guessing. Too High.")
            guessRandomNumber()
        elif (userGuess < randomNumber):
            print("Keep guessing. Too Low.")
            guessRandomNumber()
        elif(userGuess == randomNumber): 
            print("You guessed it!\nThe number is " + str(randomNumber) + ".\n")
            io.exit(0)

guessRandomNumber()
