from array import * 
import random as rd
import math 
randomArray = array('f',[])
arrayLength = 5 
while len(randomArray) < arrayLength: 
    randomNum = round(float(rd.randint(10,100)),3)
    randomArray.append(randomNum) 
#print out the array 
print("This is the randomly generated array: \n\n")
for i in randomArray:
    print(i)
tryAgain = True
number = 0
ans = array('f', [])
while (tryAgain == True): 
    number = int(input("Enter a number between 2 and 5: "))
    if (number >= 2 and number <= 5):
        tryAgain = False 
    else:
        print("Incorrect value, please try again.\n\n\n")
        tryAgain = True 
print("\n\n\nPrinting out the results: \n\n")
for i in range(0,arrayLength):
    ans = round(randomArray[i] / number,3)   
    print(ans)