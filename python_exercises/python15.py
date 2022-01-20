
######

sum = 0
count = 0
option = ""
while (option.lower() != "n"): 
    number = int(input("Enter a number: "))
    sum = sum + number
    print("Sum = " + str(sum))
    count = count + 1
    print("Count of numbers = " + str(count)) 
    option = input("Do you want to continue adding numbers? [y/n]")
    if (option.lower() == "y"): 
        print("Total = " + str(sum))
        continue 
    else: 
        break

######