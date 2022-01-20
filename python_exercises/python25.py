import random as rd

sum = 0
correctAnswers = 0
count = 0
q = 0
userAnswer = 0
while (q < 5):
    randNum_1 = rd.randint(1,5)
    randNum_2 = rd.randint(1,5)
    print("What is the sum of " + str(randNum_1) + " + " + str(randNum_2) + " = ?")
    sum = randNum_1 + randNum_2
    userAnswer = int(input("Enter your answer: "))
    print("Your answer = " + str(userAnswer))
    if (userAnswer == sum): 
        count = count + 1
    else: 
        count = count
    q = q + 1

correctAnswers = count
print("Total corect answers out of five(5) = " + str(correctAnswers) + ".\n\n")
