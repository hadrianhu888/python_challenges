#python while loop exercise 

# Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program.

#
num = 0
while (num <= 5): 
    num = int(input("Enter a number: "))
    print(str(num))
    if (num > 5): 
        print("The last number you entered was " + str(num))
        break
    else: 
        continue


