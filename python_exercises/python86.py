import random as rd
import math

n0 = 5
n1 = 20
n2 = 50 

def addTwoARandomNumbers(): 
    num1 = rd.randint(n1,n2)
    num2 = rd.randint(n1,n2)
    sumExpression = str(num1) + " + " + str(num2) + " = ? "
    print(sumExpression)
    sum = num1 + num2 
    return sum

def subtractTWoRandomNumbers():
    num1 = rd.randint(n0++n1,n2)
    num2 = rd.randint(1,n0+n1)
    differenceExpression = str(num1) + " - " + str(num2) + " = ? "
    print(differenceExpression)
    difference = num1 - num2
    return difference

def checkUserSum(userSum,sum):
    correct = 1
    if (userSum == sum):
        correct += 1
    else:
        correct = correct
    return correct 

def checkUserDifference(userDiff,diff):
    correct = 1
    if (userDiff == diff):
        correct += 1
    else:
        correct = correct
    return correct 
    
def menu():
    userInput = int(input("1) Addition\n2)Subtraction\nEnter 1 or 2:"))
    if (userInput == 1):
        sum = addTwoARandomNumbers() 
        userSum = int(input("Enter the sum of the two numbers above: "))
        checkUserSum(userSum,sum)
    elif (userInput == 2):
        diff = subtractTWoRandomNumbers()
        userDiff = int(input("Enter the difference of the two number above: "))
        checkUserDifference(userDiff,diff)
    else:
        print("Sorry, not an option. \n\nReturning to main menu now")
        menu() 
    
def main():
    menu()

main() 

