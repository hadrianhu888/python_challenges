userNumber = int(input("Enter a number below 50: "))
print("You entered the number: " + str(userNumber))
if (userNumber < 50): 
    for i in range(50,userNumber,-1): 
        print(str(i))
else: 
    print("Number is out of range")