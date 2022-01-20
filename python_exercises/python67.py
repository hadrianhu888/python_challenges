PersonAgeShoesData = {}
name = ""
age = 0
shoeSize = 0
for i in range(0,4): 
    name = input("Enter a name: ")
    age = int(input("Enter an age: ")) 
    shoeSize = int(input("Enter a shoe size: "))
    PersonAgeShoesData[name] = {"Age:",age, "Shoe Size: ", shoeSize}
    print(PersonAgeShoesData[name])
