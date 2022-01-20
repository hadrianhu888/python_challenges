from array import * 
NewFile = open("Names.txt", "w")
Names = ["Michael", "Samer", "Rehnuba", "Jackie", "Brittany"]
for i in range(0,len(Names)): 
    print(Names[i]) 
for i in range(0,len(Names)):
    NewFile.write(Names[i])
    NewFile.write("\n")
NewFile.close()