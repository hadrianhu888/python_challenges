simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(simple_array)
row = 0
row = int(input("Enter a row number: "))
displayRow = simple_array[row]
print("The numbers at " + str(row) + " and " + " is " + str(displayRow)+ ".\n\n\n")
col = 0 
col = int(input("Enter a column you like to be displayed: "))
displayRowColNumber = simple_array[row][col]
print("The number to be changed is: ")
print(displayRowColNumber)
print("\n\n")
newReplacement = 0
changeValue = True 
changeValueOption = input("Would you like to change the value? [y/n]")
if (changeValueOption.lower() == 'y'):
    newReplacement = int(input("Please change the number : "))
    simple_array[row][col] = newReplacement
    #print out the new row 
    print("The new row is: ")
    print(simple_array[row])
    changeValue = True
elif (changeValueOption.lower() == 'n'):
    changeValue = False 
    print(simple_array[row])


