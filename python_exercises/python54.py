from array import *
userArray = array('i', [])
for i in range(0,5):
    integer = int(input("Enter a number: "))
    userArray.append(integer)
userArray = sorted(userArray)
print(userArray)
userArray.reverse()
print(userArray)

    