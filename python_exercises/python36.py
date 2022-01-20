import random as rd 
import turtle as tt 

for i in range(rd.randint(1,100)):
    tt.forward(rd.randint(1,100))
    tt.right(rd.randint(0,360))

tt.exitonclick()