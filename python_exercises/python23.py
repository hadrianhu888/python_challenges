import random as rd 

def guessRandomNumber(): 
    randomNumber = rd.randint(1,10)
    userGuess = 0 
    while (randomNumber != userGuess):
        userGuess = int(input("Enter a number: "))
        if (userGuess != randomNumber):
            print("Keep guessing")
            guessRandomNumber()
        elif(userGuess == randomNumber): 
            print("You guessed it!\nThe number is " + str(randomNumber) + ".\n")

guessRandomNumber()

