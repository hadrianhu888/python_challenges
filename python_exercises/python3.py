firstName = input("Ënter your first name: ")
getFirstNameLength = len(firstName)
print("Your first name is : " + firstName + " " + " and the string length is: " + str(getFirstNameLength))

lastName = input("Enter your surname: ")
getLastNameLength = len(lastName)
fullName = firstName + " " + lastName
totalStringLength = getFirstNameLength + getLastNameLength
print("Your full name is: " + fullName + " with total string length of " + str(totalStringLength))

NurseryRhyme = input("Enter the first line of a nursery rhyme: ")
NurseryRhymeLength = len(NurseryRhyme)
startNumber = int(input("Enter the starting number: "))
endNumber = int(input("Enter the ending number: "))
printNurseryRhymeAndLength = NurseryRhyme + " has a length of " + str(NurseryRhymeLength)
printRhymeFromStartToEnd = NurseryRhyme[startNumber:endNumber]
print(printNurseryRhymeAndLength)
print(printRhymeFromStartToEnd)

userWord = input("Enter any word of your choice: ")
userWordToUpper = userWord.upper()
print("The word in upper case is: " + userWordToUpper)

firstName = input("Enter you first name: ")
firstNameLength = len(firstName)
if (firstNameLength < 5): 
    lastName = input("Enter your last name: ")
    fullNameUpperCase = firstName.upper() + lastName.upper()
    print(fullNameUpperCase)
elif (firstName > 5): 
    print(firstName.lower())

def changeWordToPigLatin(word): 
    vowels = ['a', 'e', 'i', 'o', 'u']
    startWithConsonants = "way"
    startWithVowels = "ay"
    word = input("Enter a word: ")
    if (word[0] in vowels): 
        newWord = word[1:]+ word[0] + startWithVowels
        print(newWord)
    elif (word[0] not in vowels): 
        newWord = word + startWithConsonants
        print(newWord)

changeWordToPigLatin()


    

