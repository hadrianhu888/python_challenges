subjects = {"math", "physics", "chemistry", "biology", "physical education", "history"}
for s in subjects:
    print(s)
leastFavouriteSubject = input("Enter your least favourite subject: ")
if (leastFavouriteSubject in subjects): 
    subjects.remove(leastFavouriteSubject)
print("The new subject list: ")
for s in subjects:
    print(s)
