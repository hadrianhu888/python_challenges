import random as rd
import string as str

characters = list(str.ascii_letters + str.digits + "!@#$%^&*()")

pw_length = int(input("Enter the length of the password: "))

rd.shuffle(characters)

user_password = []

for i in range(pw_length): 
    user_password.append(rd.choice(characters))

for i in range(pw_length): 
    rd.shuffle(user_password)
    print ("".join(user_password))
    
