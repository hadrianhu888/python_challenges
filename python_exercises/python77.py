import csv
file = open("Books.csv", "a")
BookName = input("Enter a book title: ")
Author = input("Enter the Author: ")
YearPublished = input("Enter Publication Year: ")
newRecord = BookName + "," + Author + "," + YearPublished + "\n"
file.writelines(str(newRecord))
file.close() 

#display the file contents




    
