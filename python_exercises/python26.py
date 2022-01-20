import random as rd

colours = ["red", "green", "blue", "yellow", "orange"]

q = 0
randomColor = rd.choice(colours)
userColor = ""
while(userColor != randomColor):
    userColor = input("Enter a colour: ")
    if (userColor == randomColor): 
        print("Well done. The colour is " + str(userColor) + " and the computer chose " + str(randomColor) + ".\n")
    elif (userColor != randomColor): 
        print("You must be feeling " + str(randomColor) + " today.\n\n")
    else:
        print("Not a valid colour\n\n")

