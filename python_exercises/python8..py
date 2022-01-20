import math
constant = 10

userName = input("Enter your name: ")
userNumber = int(input("Enter a number: "))
if (userNumber > constant): 
    for i in range(1,4):
        print("Too High.\n")
elif (userNumber < constant): 
    for i in range(1,userNumber+1): 
        print(userName)


