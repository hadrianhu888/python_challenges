low = 10
high = 20
number = 0
while ((number > low) or (number < high)): 
    number = int(input("Enter a number: "))
    if (number > high):  
        print("Too high")
        continue
    elif (number < low): 
        print("Too low")
        continue
    else: 
        print("Thank you")
        break




