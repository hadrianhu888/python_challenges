import array as ar
from array import * 
import random as rd 
baseArray = array('i',[])
for i in range(0,5):
    num = int(rd.randint(1,100))
    baseArray.append(num)
print(baseArray)
userArray = array('i', [])
userInput = 0
while len(userArray) < 3: 
    userInput = int(input("Enter a number into the array: "))
    userArray.append(userInput)
#print the user array and the base array 
print("Base Array: ")
print(baseArray)
print("User Array: ")
print(userArray)
#join the two arrays 
baseArray.extend(userArray)
baseArray = sorted(baseArray)
for i in baseArray: 
    print(i)


