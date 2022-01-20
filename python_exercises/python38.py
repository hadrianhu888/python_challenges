sports = {"basketball", "football"}
for s in sports: 
    print(s)
favouriteSport = input("What is your favourite sport?")
print("You aaid " + favouriteSport)
if (favouriteSport not in sports): 
    sports.add(favouriteSport)
for i in sports:
    print(i)