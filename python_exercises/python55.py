from array import *
import random as rd 
userArray = array('i', [])
for i in range(0,5):
    integer = int(rd.randint(1,100))
    userArray.append(integer)
userArray = sorted(userArray)
print(userArray)
userArray.reverse()
print(userArray)
for i in range(0,5):
    print(userArray[i])

