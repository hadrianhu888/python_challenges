import array as ar
from array import * 
num = 0
userArray = array('i', [])
while len(userArray) < 5:
    num = int(input("Enter a number: "))
    userArray.append(num)
#print out the numbers 
print("The original array: ")
for i in userArray:
    print (i)
#sort the array
userArray = sorted(userArray)
#print out the sorted array 
for i in userArray:
    print (i)
#let the user select a number to remove: 
newArray = array('i',[])
numToRemove = int(input("Enter a number to remove: "))
print("The number to remove: " + str(numToRemove))
if (numToRemove in userArray):
    userArray.remove(numToRemove)
    newArray = userArray 
else:
    print("The number " + str(numToRemove) + " is not in the array.\n\n")
#print out the new array
print("\n\nThe new array: \n\n")
for i in newArray:
    print(i)
