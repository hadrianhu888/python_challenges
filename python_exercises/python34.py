import turtle as tt 
import random as rd

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
randomColor = rd.choice(colors)

for i in range(0,8):
    tt.color(rd.choice(colors))
    tt.forward(100)
    tt.right(45)

tt.exitonclick()

