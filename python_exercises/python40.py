favouriteFoods = {}
f1 = input("Enter a favourite food: ")
favouriteFoods[1] = f1
f2 = input("Enter a favourite food: ")
favouriteFoods[2] = f2
f3 = input("Enter a favourite food: ")
favouriteFoods[3] = f3
f4 = input("Enter a favourite food: ")
favouriteFoods[4] = f4

print(favouriteFoods)

dislike = int(input("Which of these is your least favourite food? "))
del favouriteFoods[dislike]
print(sorted(favouriteFoods.values()))



