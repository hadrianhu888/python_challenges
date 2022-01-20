import io

name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")

party = [name1, name2, name3]

another = input("Enter another name? [y/n]")
while (another.lower() == 'y'):
    newname = party.append(input("Enter another name: "))
    another = input("Do youw ant to add another person? [y/n]")
print("YOu have invited " + len(party) + " to the party.\n\n")

# def addGuestsToAList(): 
    
#     guestList = []
#     userGuestName = ""
#     guestCount = 0
#     userChoice = ""
#     while (userChoice.lower() != 'no'): 
#         userGuestName = input("Enter a guest name: ")
#         userChoice = input("Enter another guest? [yes/no]")
#         guestList.append(userGuestName)
#         guestCount += 1
#         if (userChoice.lower() == 'yes'):
#             addGuestsToAList()
#         elif (userChoice.lower() == 'no'): 
#             break
#         else:
#             break 
#     print(guestList)
#     print(len(guestList))

# addGuestsToAList()

