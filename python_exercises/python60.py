import random as rd
from array import *
randomNumberArray = array('i',[])
randomNum = 0
for i in range(0,5):
    randomNum = rd.randint(0,100)
    randomNumberArray.append(randomNum)
#print out the array 
print("The random number array is shown below:\n\n")
#print(randomNumberArray)
for i in randomNumberArray:
    print(i)
userSelection = 0
userSelection = int(input("Enter a number to remove from the array: "))
print("You seleected the number: " + str(userSelection))
#find the index of the chosen number 
#else display an error message 8until they select a number in the array 
while (userSelection in randomNumberArray): 
    if (userSelection in randomNumberArray): 
        userNumberIndex = randomNumberArray.index(userSelection)
        print("The index of the number " + str(userSelection) + " is at " + str(userNumberIndex+1) + ".\n\n\n")
    else:
        print("Incorrect - please try again. Enter a number in the array provided above.\n\n\n")

    