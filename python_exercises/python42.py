numberList = [123, 321, 345, 543]
print(numberList)
userNumber = int(input("Enter a number: "))
if (userNumber in numberList):
    print("Position: " + str(numberList.index(userNumber)))
else: 
    print(str(userNumber) + " is not in the list\n\n")
