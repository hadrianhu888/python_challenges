#######
sum = 0
count = 0
option = ""
while (option.lower() != "n"): 
    name = (input("Enter a name to invite to the party: "))
    print(name + " has been invited to the party.")
    count = count + 1
    option = input("Do you want to continue adding people? [y/n]")
    if (option.lower() == "y"): 
        count = count + 1
        print("Total = " + str(count) + " has been invisted to the party")
        continue 
    else: 
        break