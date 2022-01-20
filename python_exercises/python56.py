import array as ar
from array import * 
userArray = array('i',[])
while len(userArray) < 5:
    userNum = int(input("Enter a value: "))
    if (userNum >= 10 and userNum <= 20):
        userArray.append(userNum)
    else:
        print("Outside of range")
for i in userArray:
    print(i)


