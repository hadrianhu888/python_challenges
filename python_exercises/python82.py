import csv 
file = open("Books.csv", "r")
temp = [] 
file = list(csv.reader(open("Books.csv")))
temp = [] 
for r in file:
    temp.append(r)

x = 0
for r in temp:
    display = x,temp[x]
    print(display)
    x += 1
removeData = int(input("Enter the row number to delete: "))
del temp[removeData]

x = 0 
for r in temp:
    display = x, temp[x]
    print(display)
    x += 1
alter = int(input("Enter a row to alter: "))
for r in temp:
    display = x, temp[x]
    print(display)
    x += 1
part = int(input("Which part do you want to change? "))
newData = input("Enter new data: ")
temp[alter][part] = newData
print(temp[alter])

file = open("Books.csv", "w")
x = 0
for r in temp:
    newRecord = temp[x][0] + ", " + temp[x][1] + ", " + temp[x][2] + "\n"
    x += 1
file.close() 



    