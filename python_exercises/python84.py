def enterNum():
    num = int(input("Enter a number: "))
    print("The number you entered is: " + str(num))
    return num
    
def countUp(num): 
    for i in range(0,num):
        print(str(i+1))


num = enterNum()
countUp(num)
