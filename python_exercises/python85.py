import random as rd
import math

def generateANumberBetweenTwoNumbers():
    low = int(input("Enter a low value: "))
    high = int(input("Enter a high vale: "))
    comp_num = rd.randint(low, high)
    return comp_num 

comp_num = generateANumberBetweenTwoNumbers() 

def NumberGuessingGame():
    randomNumber = int(input("I am thinking of a number...What is this number?"))
    return randomNumber 
    
randNum = NumberGuessingGame()

def printOutGuessAndRandomNumber(comp_num, randNum): 
    print("Your guess: " + str(randNum)) 
    print("The actual random number: " + str(comp_num))

def checkGuessAndGeneratedRandomNumber(comp_num, randNum):
    correct = True 
    if randNum == comp_num: 
        print("You guessed correctly")
        printOutGuessAndRandomNumber(comp_num,randNum)
        correct = True 
    else:
        print("This is the incorrect guess")
        printOutGuessAndRandomNumber(comp_num,randNum)
        correct = False 
    return correct 

checkGuessAndGeneratedRandomNumber(comp_num, randNum) 

