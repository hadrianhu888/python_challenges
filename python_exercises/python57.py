import array as ar
from array import * 
userArray = array('i',[1,1,2,3,4])
count = 0
for i in userArray:
    print(i)
userInput = int(input("Enter a number from the array: "))
if (userInput in userArray):
    for i in userArray:
        if userArray[i] == userInput: 
            count += 1 
else:
    print("The number entered is not in the array\n")

print("The user entered the number: " + str(userInput) +  " which occurred " + str(count) +  " times in the array\n\n")

