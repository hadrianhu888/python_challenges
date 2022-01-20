TVShows = ["Continuum", "StarGate SG 1", "StarGate Atlantis", "Battle Star Galactica"]

for i in TVShows:
    print(i)

newTVShow = input("Enter another TV show: ")
newPosition = int(input("Where would you like to put this show? ")) 

TVShows.insert(newPosition,newTVShow)

print("\n\nNew TV Show List:\n\n")

for i in TVShows:
    print(i)


