import csv
import math 
from array import *
import random as rd 
import sys 
import os 

nameList = [] 
file = open("NameFile.csv", "w")

def returnToMenu():
    returnYesOrNo = input("Return to main menu? [y/n]")
    if( returnYesOrNo.lower() == 'y'):
        menu()
    elif (returnToMenu.lower() == 'n'):
        exitProgram()


def menu():
    print("1) Add a name\n2) Change a name\n3) Delete a name\n4) View names\n5) Exit the program")
    choice = int(input("Enter a number, either 1, 2, 3,4 or 5 from above: "))
    if (choice == 1):
        enterNameIntoList()
    elif(choice == 2):
        changeNameInList()
    elif(choice == 3):
        deleteNameFromList()
    elif(choice == 4):
        viewNameList()
    elif(choice == 5):
        exitProgram()
    else:
        print("Sorry, this is not a valid option.\nReturning to the main menu now.\n")
        menu() 

def enterNameIntoList():
    name = input("Enter a name: ")
    print("The name you entered is: " + name)
    nameList.append(name)    
    file.write(str(name))
    returnToMenu() 
    
def changeNameInList():
    nameToChange = input("Enter name to change: ")
    if (nameToChange in nameList):
        indexToChange = nameList.index(nameToChange)
        changeName = input("What is the new name? ")
        nameList[indexToChange] = changeName 
        file.write(str(changeName))
        returnToMenu() 
    else:
        print("Sorry, the name is not on the list.")
        changeNameInList()

def deleteNameFromList():
    nameToDelete= input("Enter name to change: ")
    if (nameToDelete in nameList):
        indexToDelete= nameList.index(nameToDelete)        
        del nameList[indexToDelete]
        returnToMenu() 
    else:
        print("Sorry, the name is not on the list.")
        deleteNameFromList() 
        
def viewNameList():
    for i in nameList:
        print(nameList[i])
    returnToMenu() 

def exitProgram():
    print("The program will now exit")
    sys.exit()
    
def main(): 
    menu()
    
main() 