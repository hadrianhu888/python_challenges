import csv 

file = open("Books.csv", "r")
with file as f:
    csv_reader = csv.reader(f)
    for line in f: 
        print(line)
        
file.close()

