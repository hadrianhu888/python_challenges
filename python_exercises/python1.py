firstName = input("Enter your first name: ")
print("Hello " + firstName) 

lastName = input("Enter your last name: ")
print("Hello " + firstName + " " + lastName)

Joke = "What do you call a bear iwth no teeth? "
Answer = "A gummy bear!"
print(Joke + " " + Answer)

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
Total = firstNumber + secondNumber
print("Total is " + str(Total))

a = int(input("Enter the first number: "))
b = int(input("Ënter the second number: "))
c = int(input("Enter the third number: "))
answer = (a + b) * c
print("The Answer is : " + str(answer))

startingSlices = int(input("How many pizza slices did you start with? "))
slicesAte = int(input("How many slices of pizza did you eat so far? "))
remainingSlices = startingSlices - slicesAte
remainingSlicesMessage = print("There are " + 
                               str(remainingSlices) + " of pizza left.\n\n\n")

fullName = input("Ënter your full name: ")
Age = int(input("Enter your current age: "))
nextYear = Age + 1
printNextYearAge = print("You will be " + str(nextYear) + " years old next year.\n\n")

totalPriceOfBill = float(input("What is the total cost of the bill? "))
totalDiners = int(input("How many dinners are there? "))
averagePayment = float (totalPriceOfBill / totalDiners)
averagePaymentPerDinerMessage = print("The Average each diner pays is " + 
                                      str(averagePayment))

Lb2Kg = 2204

hoursPerDay = 24
minutesPerHour = 60
secondsPerMinute = 60
days = int(input("Enter how many days: "))
totalHours = days * hoursPerDay
totalMinutes = totalHours * minutesPerHour
totalSeconds = totalMinutes * secondsPerMinute
totalHoursMessage = print("There are " + str(totalHours) + " hours")
totalMinutesMessage = print("There are " + str(totalMinutes) + " minutes")
totalSecondsMessage = print("There are " + str(totalSeconds) + " seconds")

def convertPoundToKilogram(weight): 
    return weight * Lb2Kg

getWeight = float(input("Enter the weight in lbs: "))
putWeightFromLb2Kg = print("The weight in kilograms is: " + 
                           str(convertPoundToKilogram(getWeight)) + " kilograms.\n\n")

getNumberOverHundred = int(input("Enter a number greater than one hundred: ")) 
if (getNumberOverHundred < 100): 
    print("Please enter a number greater than one hundred.")
else: 
    getNumberLessThanTen = int(input("Enter a number less than ten: "))
    if (getNumberLessThanTen > 10): 
        print("Please enter a number less than ten.")
    else: 
        getQuotient = getNumberOverHundred / getNumberLessThanTen
        getQuotientMessage = print(
            "The number " + str(getNumberLessThanTen) +" can go into " + 
                                   str(getNumberOverHundred) + " " + str(getQuotient) + " times.\n\n" 
                                   )


