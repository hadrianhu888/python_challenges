name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")

party = [name1, name2, name3]

another = input("Enter another name? [y/n]")
while (another.lower() == 'y'):
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to add another person? [y/n]")
print("YOu have invited " + str(len(party)) + " to the party.\n\n")

for i in party: 
    print(i)

enterName = input("Enter a name on the invite list: ")
StillComeToParty = input("Do you still want to invite this person to the party? ")
if (StillComeToParty.lower() == 'n'):
    party.remove(enterName)
else:
    print("The official party invite list:")
    print(party)
