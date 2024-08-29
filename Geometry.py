# Import initializing
import math
import os

# Variable initiailzing
continueProgram = True
goodGuess = False

# Function initializing
def circle():
    circleRadius = float(input("What is your radius: "))
    circleCircumference = math.pi * (2 * circleRadius)
    circleArea = math.pi * (circleRadius * circleRadius)
    
    print("Your radius is: " + str(circleRadius))
    print("Your circumference is: " + str(circleCircumference))
    print("Your area is: " + str(circleArea))

def square():
    squareWidth = float(input("What is your width: "))
    squarePerimeter = (2 * squareWidth) + (2 * squareWidth)
    squareArea = squareWidth * squareWidth
    
    print("Your width is: " + str(squareWidth))
    print("Your perimeter is: " + str(squarePerimeter))
    print("Your area is: " + str(squareArea))

def rectangle():
    rectangleWidth = float(input("What is your width: "))
    rectangleLength = float(input("What is your length: "))
    rectanglePerimeter = (2 * rectangleWidth) + (2 * rectangleLength)
    rectangleArea = rectangleWidth * rectangleLength
    
    print("Your width is: " + str(rectangleWidth))
    print("Your length is: " + str(rectangleLength))
    print("Your perimeter is: " + str(rectanglePerimeter))
    print("Your area is: " + str(rectangleArea))


# Run main program
while continueProgram == True:

    os.system("clear")

    whatToLearn =  input("What do you want to learn about (circles, squares, or rectangles): ")

    if whatToLearn.lower() == "circles":
        circle()
    elif whatToLearn.lower() == "squares":
        square()
    elif whatToLearn.lower() == "rectangles":
        rectangle()
    else:
        while goodGuess == False:
            newWhatToLearn = input("That input is not valid. What do you want to learn about (circles, squares, or rectangles): ")
            if newWhatToLearn.lower() == "circles":
                circle()
                goodGuess = True
            elif newWhatToLearn.lower() == "squares":
                square()
                goodGuess = True
            elif newWhatToLearn.lower() == "rectangles":
                rectangle()
                goodGuess = True
        goodGuess = False
    
    runAgain = input("Do you want to run the program again (yes or no): ")
    if runAgain.lower() == "yes":
        continueProgram = True
    elif runAgain.lower() == "no":
        continueProgram = False
    else:
        print("Invalid response. Ending program.")