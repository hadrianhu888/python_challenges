compnum = 50 
number = 0
while (number != compnum): 
    number = int(input("Enter a guess value: "))
    if (number > compnum):  
        print("Too high")
    elif (number < compnum): 
        print("Too low")
    else: 
        print("Perfect")


        