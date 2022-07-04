from tkinter import *
import random 

def click(): 
    num = random.randint(1,6)
    answer["text"] = num
    
window = Tk()
window.title("Roll a Dice")
window.geometry("100x200")

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 50, width = 50, height = 25)

answer = Message(text = "")
answer.place(x = 40, y = 70, width = 25, height = 25)

window.mainloop()

