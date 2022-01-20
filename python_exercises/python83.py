import random as rd
import math as m 
import csv 

userName = input("Enter your name: ")
numberOne = int(rd.randint(1,100))
numberTwo = int(rd.randint(1,100))
randomSum = numberOne + numberTwo
displayQuestion = "What is the sum of " + str(numberOne) + " and " + str(numberTwo) + " ?"
print(displayQuestion)
userAnswer = int(input("Enter your answer "))
correctAnswers = 0
totalQuestionsAsked = 1
if (userAnswer == randomSum):
    correctAnswers += 1
else:
    correctAnswers = correctAnswers
totalQuestionsAsked += 1 
finalScore = round(float (correctAnswers / totalQuestionsAsked),2) 

file = open("UserQuestionsAndAnswers.csv", "a")
newData = +"\n" + userName.title() + ", " + displayQuestion + ", " + str(userAnswer) + ", " + str(correctAnswers) +", " + str(finalScore) + "\n"
file.write(str(newData))
file.close()



