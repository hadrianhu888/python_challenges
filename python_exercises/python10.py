def UserUpDownFunction(): 
    userDirection = input("Enter a direction: [up] or [down]: ")
    if (userDirection.lower() == "up"): 
        userNumber = int(input("Enter a number less than 20: "))
        if (userNumber > 20): 
            print("Sorry, too high")
        else: 
            for i in range(1,userNumber): 
                print(i)
    elif (userDirection.lower() == "down"): 
        userNumber = int(input("Enter a number less than 20: "))
        if (userNumber > 20): 
            print("Sorry, too high")
        else: 
            for i in range(20, userNumber, -1): 
                print(i)
    else: 
        print("Sorry, I don't understand " + userDirection + " command.\n\n")

UserUpDownFunction()


