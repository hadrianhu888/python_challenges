import turtle as tt 

tt.color("black", "red")
tt.begin_fill()
for i in range(0,4):
    tt.forward(100)
    tt.right(90)

tt.penup()
tt.end_fill()
tt.forward(120)
tt.pendown()

tt.color("black", "green")
tt.begin_fill()
for i in range(0,4):
    tt.forward(100)
    tt.right(90)
    
tt.penup()
tt.end_fill()
tt.forward(120)
tt.pendown()

tt.color("black", "blue")
tt.begin_fill()
for i in range(0,4):
    tt.forward(100)
    tt.right(90)
    
tt.penup()
tt.end_fill()

tt.exitonclick()