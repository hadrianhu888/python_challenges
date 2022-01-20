def SchoolSubjectList(): 

    subjects = []
    options = {"1) Create a new File", "2) Display the File", "3) Add a new item to the files."}
    for i in options: 
        print(i)
    print("Make a selection 1, 2 or 3")
    userInput = int(input("Your choice: ")) 
    if (userInput == 1): 
        File = open("Subjects.txt", "w")
        schoolSubject = input("Enter a school subject: ")
        print("Subject: " + schoolSubject)
        subjects.append(schoolSubject)
        File.write(schoolSubject)
        File.write("\n")
        File.close()
    elif (userInput == 2): 
        File = open("Subjects.txt", "r")
        print("The file contents are: ")
        print(File.read())
        File.close()
    elif (userInput == 3): 
        File = open("Subjects", "a")
        anotherSchoolSubject = input("Enter another school subject: ")
        subjects.append(anotherSchoolSubject)
        print("You entered: " + anotherSchoolSubject)
        File.close()
    else:
        print("Sorry, please select 1, 2 or 3\n\n")   
        SchoolSubjectList() 

SchoolSubjectList()
