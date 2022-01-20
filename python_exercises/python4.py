import math

userNumber = float(input("Enter a very long number with lots of decimals"))
newNumber = userNumber * 2
print("The new number is " + str(newNumber))
print("The new number is " + str(round(newNumber,2)))

userInteger = int(input("Enter a number over 500: "))
if (userInteger > 500): 
    squareRootUserInteger =  round(math.sqrt(userInteger),2)
    print("The square root of the number " + userInteger + "  is " + squareRootUserInteger + ".\n\n")
else: 
    print("The number is " + str(userInteger))

print(round(math.pi,5))

radius = float(input("Enter the radius of a circle: "))

def circleArea (radius): 
    return pow(radius,2) * math.pi

AreaOfACircle = circleArea(radius)
print("The area of a circle with radius " + str(radius) + " is " + str(AreaOfACircle) + ".\n\n")

cylinderHeight = float(input("Enter the height of the cylinder: "))

def CylinerVolume(radius, height): 
    return round(circleArea(radius) * height,3)

VolumeOfACylinder = CylinerVolume(radius, cylinderHeight)
print("The volume of a cylinder with radius " + str(radius) + " and height " + str(cylinderHeight) + " is " + str(VolumeOfACylinder) + ".\n\n")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
quotient = first // second
remainder = first % second
print("The division of " + str(first) + " and " + str(second) + " has a quotient of " + str(quotient) + " and a remainder of " + str(remainder) + ".\n\n")

def SquareOrTriangle(): 
    SelectOperation = "1) Square\n2) Triangle"
    print(SelectOperation)
    choice = int(input("Enter 1 or 2 above: "))
    if (choice == 1):
        side = float(input("Enter side length: "))
        SquareArea = pow(side,2)
        print("Area = " + str(SquareArea) + ".\n\n")
    elif (choice == 2): 
        base = float(input("Enter base length: "))
        height = float(input("Enter height length: "))
        TriangleArea = 0.5 * base * height
        print("Area of the Triangle = " + str(TriangleArea) + ".\n\n")
    else: 
        print("\nNot a valid option. Please select either 1 or 2.\n\n")
        SquareOrTriangle()

SquareOrTriangle()



