import string 

vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
userName = input("Enter your name: ")
userName = userName.lower()
print(userName)
count = 0
for i in userName:
    if i in vowels:
        count += 1 
    else:
        count = count 
print("Vowel count: " + str(count))
