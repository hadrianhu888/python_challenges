NameFile = open("Names.txt", "r")
#display all of the names first 
print(NameFile.read())
NameFile.close()

NameFile = open("Names.txt", "r")
NameToMove = input("Enter a name to remove from the orignal file: ")
print("You entered: " + NameToMove)
for row in NameFile:
    if row != NameToMove:   
        NewNameFile = open("Name2.txt", "a")     
        NewNameFile.write(NameToMove)
        NewNameFile.close()
NameFile.close()




