word = input("Enter a word: ")
length = len(word)
n = 1
for i in word:
    p = length - n
    letter = word[p]
    print(letter)
    n += 1


    