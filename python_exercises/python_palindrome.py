def palindrome():
    string = input("Enter the word: ")
    original_word = string
    reverse_word = string[::-1]
    if (reverse_word == original_word):
        print (string, " is a palindrome word")
    else:
        print (string, " is not a palindrome word")
        
def checkPalindrome(a):
    word = a
    condition = True
    rev_word = a[::-1]
    if (rev_word == word):
        condition = True
    else: 
        condition = False
    print(condition)
    return condition 

checkPalindrome("eye")
checkPalindrome("level")
checkPalindrome("dust")

palindrome()

def isAnagram(a,b): 
    condition = True
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b: 
        condition = False        
    else:
        if (sorted(a) == sorted(b)): 
            condition = True          
        else:
            condition = False
    print (condition)
    return condition

isAnagram("this", "hits")
isAnagram("abba", "baby")

def isAnagramPalindrome(a): 
    checkPalindrome(a)
    