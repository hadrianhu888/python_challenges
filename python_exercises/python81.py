import csv 
file = open("Books.csv", "r")
temp = [] 
file = list(csv.reader(open("Books.csv")))
temp = [] 
for r in file: 
	temp.append(r) 

x = 0
for r in temp:   
    print(x) 
    x += 1
    print(r)