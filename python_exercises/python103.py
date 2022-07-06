from tkinter import *

def convert1():
    km = textbox1.get()
    km = int(km)
    message = km / 0.6214
    textbox1.delete(0,END)
    textbox1.insert(END, str(message))
    textbox1.insert(END, " miles")

def convert2():
    miles = textbox2.get()
    miles = int(miles)
    message1 = miles * 0.6214
    textbox2.delete(0,END)
    textbox2.insert(END, str(message1))
    textbox2.insert(END, " km")
    
window = Tk()
window.title("Distance Conversion Calculator")
window.geometry("260x200")

label1 = Label(text = "Enter the value you want to convert")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 30, y = 50, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

textbox2 = Entry(text = "")
textbox2.place(x = 30, y = 70, width = 200, height = 25)
textbox2["justify"] = "center"
textbox2.focus()

convert1_btn = Button(text = "Convert miles to km", command = convert1)
convert1_btn.place(x = 30, y = 100, width = 200, height = 25)

convert2_btn = Button(text = "Convert km to miles", command = convert2)
convert2_btn.place(x = 30, y = 120, width = 200, height = 25)

window.mainloop()

