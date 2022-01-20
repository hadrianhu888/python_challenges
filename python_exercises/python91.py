from tkinter import *
import random as rd 
import math 
import sys 
def click(): 
    num = rd.randint(1,6)
    answer["text"] = num 

window = Tk()
window.geometry("500x200")

label1 = Label(text = "Dice Value: ")
label1.place(x = 30, y = 20)

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)

answer = Message(text = "")
answer.place(x = 150, y = 50, width = 200, height = 25)

window.mainloop() 
