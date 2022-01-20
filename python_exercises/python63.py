simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(simple_array)
row = 0
col = 0 
row = int(input("Enter a row number: "))
col = int(input("Enter a column number: "))
indexValue = simple_array[row] [col]
print("The number at " + str(row) + " and " + str(col) + " is " + str(indexValue)+ ".\n\n\n")
