import csv
import sys 

def AddToFile():
    file = open("Salaries.csv", "w")
    name = input("Enter a name: ")
    salary = int(input("Enter a salary: "))
    newRecord = name + ", " + str(salary) +"\n"
    file.write(str(newRecord))
    file.close() 
    Menu()

def ViewRecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()  
    Menu() 

def QuitProgram():
    sys.exit()

def Menu():
    print("(1) Add to file\n(2) View all Records\n(3) Quite the program")
    selection = int(input("Enter an option above: ")) 
    if (selection == 1):
        AddToFile()
    elif(selection == 2):
        ViewRecords()
    elif(selection == 3):
        QuitProgram()
    else:
        Menu() 

def main():
    Menu()

main()       