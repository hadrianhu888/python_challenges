invitedGuests = int(input("How many people are invited to the party? "))
if (invitedGuests > 10):
    print("Too many people.")
elif (invitedGuests <= 10):
    for i in range(0,invitedGuests+1): 
        name = input("Enter a name for guest number " + str(i) + ": ")
        print(name + " has been invited to the party.")
else:
    print("Not a valid number. Please try again.\n\n")





