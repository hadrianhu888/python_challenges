import math

total = 0
for i in range(1,6): 
    number = int(input("Enter a number: "))
    print("number = " + str(number))
    addToTotal = input("Add to total? [y/n]")
    if (addToTotal.lower() == 'y'): 
        total = total + number
    elif (addToTotal.lower() == 'n'): 
        total = total 
    else: 
        print("Not a valid option")
        total = total

print("The total is " + str(total))





