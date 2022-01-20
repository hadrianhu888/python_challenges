start = 10
howMany = 0
while (start >= 0):
    print("There are " + str(start) + " green bottles hanging on the wall, and if 1 grene bottle should accidentally fall, how many green bottles are on the wall?")
    howMany = int(input("Enter how many green bottles are left hanging on the wall: "))
    start = start - 1
    if (howMany == start): 
        print("There will be " + str(start - 1) + " bottles hanging on the wall")
        continue 
    else: 
        print("Sorry, try again")
        continue 



