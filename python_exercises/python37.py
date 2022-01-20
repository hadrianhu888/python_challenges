countries=  ("Italy", "Canada", "United States of America")
print(countries)
userCountry = input("Please enter the name of a country: ")
if (userCountry in range(0,3)):
    print(countries.index(userCountry))
else: 
    print("Sorry, not a country")
userNumber = int(input("Ënter a number between 0 and 2: "))
print(countries[userNumber])

