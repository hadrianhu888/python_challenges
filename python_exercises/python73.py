OpenFile = open("Names.txt","r")
print(OpenFile.read())
OpenFile.close()

OpenFile = open("Names.txt","a")
newName = input("Enter a new name: ")
print("You entered: " + newName)
OpenFile.write(newName)
OpenFile.write("\n")
OpenFile.close()

OpenFile = open("Names.txt", "r")
print(OpenFile.read())
OpenFile.close()