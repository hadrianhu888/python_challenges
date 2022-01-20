firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

def CompareNumbers(first, second):
    print("The number is: ")
    if (first > second):        
        print(str(second) + " " + str(first))
    else:        
        print(str(first)+ " " + str(second))

CompareNumbers(firstNumber, secondNumber)

NumberLessThanTwenty = int(input("Enter a number less than 20: "))

def compareTwenty(number): 
    if(number >= 20): 
        print("Too high")
    else: 
        print("Thank you")

compareTwenty(NumberLessThanTwenty)

NumberBetweenTenTwenty = int(input("Enter a number between 10 and 20, inclusive: "))

def checkBetweenTenTwenty(number): 
    if(number >= 10 and number <= 20): 
        print("Thank you")
    else: 
        print("Incorrect Answer")
    
checkBetweenTenTwenty(NumberBetweenTenTwenty)

userFavouriteColor = input(print("Enter your favourite color: "))

def checkUserColor(color): 
    if(color == 'red' or 'Red' or 'RED'): 
        print("I like red too.")
    else: 
        print("I don't like " + color + ", I prefer red.")
        
checkUserColor(userFavouriteColor)

def checkWeatherCondition(): 
    Raining = input(print("Is it raining? Enter yes or no"))
    Windy = input(print("Is it also windy? Enter yes or not"))
    if (Raining.lower() == 'yes' and Windy.lower() == 'yes'): 
        print("It is too windy for an umbrella.")
    elif(Raining.lower() == 'yes' and Windy.lower() == 'no'): 
        print("Take an umbrella.")
    elif(Raining.lower() == 'no' and Windy.lower() == 'no'):   
        print("Enjoy your day.")
    else: 
        print("Invalid input. Enter yes or no")
        checkWeatherCondition()

checkWeatherCondition()

def checkAge(): 
    Age = int(input("Enter your age: "))
    if (Age >= 18): 
        print("You can vote.")
    elif(Age >= 17):
        print("You can learn to drive.")
    elif(Age >= 16):
        print("You can buy a lottery ticket.")
    else:
        print("You can go Trick-or-Treating.")
    
checkAge()

def NumbersBetweenTenAndTwenty(): 
    number = int(input("Enter a number between ten and twenty: "))
    if(number > 20): 
        print("Too high.")
    elif (number > 10): 
        print("Correct.")
    else: 
        print("Too low.")
    
NumbersBetweenTenAndTwenty()

def UserNumbers(): 
    userNumber = int(input("Enter either 1, 2, or 3: "))
    if(userNumber == 1): 
        print("Thank you.")
    elif (userNumber == 2): 
        print("Well done.")
    elif (userNumber == 3):
        print("Correct.")
    else:
        print("Error message.")

UserNumbers()





