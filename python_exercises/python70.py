import random as rd 
NewFile = open("Numbers.txt","w")
num = 0
for i in range(0,5):
    num = (rd.randint(1,100))
    NewFile.write(str(num))
    NewFile.write(", ")
NewFile.close()