import random as rd

randomNumber = rd.randint(1,5)
userGuess = 0
print(randomNumber)
while(randomNumber != userGuess): 
    userGuess = int(input("Enter a number: "))
    print("You entered: " + str(userGuess))
    if (userGuess > randomNumber):  
        print("Too High")
    elif (userGuess < randomNumber): 
        print("Too Low")
    else:
        print("Corect!\nYour guess = " + str(userGuess) + "\nThe Random Number = " + str(randomNumber))
