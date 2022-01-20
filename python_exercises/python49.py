def userEnterAWord(): 
    userWord = input("Enter a word in all UPPER CASE: ")
    if userWord.isupper():
        print(userWord)        
    elif(userWord.islower()): 
        print("Try again")
        userEnterAWord()
    else:
        userEnterAWord()        
userEnterAWord()

