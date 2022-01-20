from tkinter import *
import csv

def save_list(): 
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newRecord = name + "," + age +"\n"
    file.write(str(newRecord))
    file.close()
    name_box.delete(0,END)
    age_box.delete(0,END)
    name_box.focus()

def read_list():
    name_list.delete(0,END)
    file = list(csv.reader(open("ages.csv")))
    temp =[]
    for row in temp: 
        temp.append(row)
    x = 0
    for i in temp: 
        data = temp[x]
        name_list.insert(END,data)
        x += 1    

def show_file():
    file = open("ages.csv", "r")
    file = list(csv.reader(open("ages.csv")))
    temp =[]
    for row in temp: 
        temp.append(row)
    x = 0
    for i in temp: 
        data = temp[x]
        print(x)
        x += 1   

window = Tk()
window.title("Peoples List")
window.geometry("400x200")

label1 = Label(text = "Enter a name:")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry()
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text = "Enter their age: ")
label2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry()
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"
age_box.focus()

button1 = Button(text = "Add to File", command = save_list)
button1.place(x = 250, y = 20, width = 100, height = 25)

button2 = Button(text = "Read List", command = read_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

button3 = Button(text = 'Show CSV file', command = show_file)
button3.place(x = 250, y = 80, width = 100, height = 25)

label3 = Label(text = "Saved Names: ")
label3.place(x = 120, y = 80, width = 100, height = 25)

name_list = Listbox()
name_list.place(x  = 120, y = 80, width = 120, height = 100)
name_list.focus() 

window.mainloop() 



