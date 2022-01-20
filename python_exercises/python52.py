newPassWord = input("Enter your password: ")
repeatPassWord = input("Enter your password again: ")
if (repeatPassWord == newPassWord): 
    print("Thank you")
elif (repeatPassWord.lower() != newPassWord.lower()):
    print("They must be in the same case")
else:
    print("Incorrect")
