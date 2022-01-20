nums = []
number = int(input("Enter a number: "))
option = input("Add another number? [y/n]")
nums.append(number)   
while (option.lower() == 'y'):        
    number = int(input("Enter a number: ")) 
    option = input("Add another number? [y/n]")     
    nums.append(number)   
print(nums)