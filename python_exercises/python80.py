import csv 
file = open("Books.csv", "r")
startYear = int(input("Enter a starting year: "))
endYear = int(input("Enter an End Year: "))
temp = [] 

file = list(csv.reader(open("Books.csv")))
temp = [] 
for r in file: 
	temp.append(r) 

x = 0
for r in temp:
    if (int(temp[x][2]) >= startYear and int(temp[x][2]) <= endYear):
        print(temp[x])
    x = x + 1

