import csv
file = open("Books.csv","a")
howMany = int(input("How many more records wouldd you like to add? "))
print("YOu want to add " + str(howMany) + " to the Books.csv record.\n\n")
for i in range(0,howMany):
    BookName = input("Enter a book title: ")
    Author = input("Enter the Author: ")
    YearPublished = input("Enter Publication Year: ")
    newRecord = + "\n" + BookName + "," + Author + "," + YearPublished + "\n"
    file.writelines(str(newRecord))
file.close()

file = open("Books.csv", "r")
with file as f:
    csv_reader = csv.reader(f)
    for line in f: 
        print(line)  
file.close()

