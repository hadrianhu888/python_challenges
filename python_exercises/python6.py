userNumber = int(input("Enter a number between 1 and 12: "))
print("The number is " + str(userNumber))
#print out the multiplication table for this number 
for i in range(0,12): 
    print(str(userNumber * (i+1)))