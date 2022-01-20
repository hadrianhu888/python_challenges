import turtle as tt 

for i in range(0,8):
    tt.right(135)
    for j in range(0,8):
        tt.forward(50)
        for k in range(0,8): 
            tt.forward(50)
            tt.right(45)
    
tt.exitonclick()