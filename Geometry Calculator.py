# Import initializing
import math
import os

# Variable initiailzing
continueProgram = True
goodGuess = False

# Function initializing
def circle(circleRadius):
    circleCircumference = math.pi * (2 * circleRadius)
    circleArea = math.pi * (circleRadius * circleRadius)

    return circleCircumference, circleArea

def square(squareWidth):
    squarePerimeter = (2 * squareWidth) + (2 * squareWidth)
    squareArea = squareWidth * squareWidth

    return squarePerimeter, squareArea

def rectangle(rectangleWidth, rectangleLength):
    rectanglePerimeter = (2 * rectangleWidth) + (2 * rectangleLength)
    rectangleArea = rectangleWidth * rectangleLength

    return rectanglePerimeter, rectangleArea



# Run main program
while continueProgram == True:

    os.system("clear")

    whatToLearn =  input("What do you want to learn about (circles, squares, or rectangles): ")

    if whatToLearn.lower() == "circles":
        circleRadius = float(input("What is your radius: "))
        circleResult = circle(circleRadius)

        print("Your radius is: " + str(circleRadius))
        print("Your circumference is: " + str(circleResult[0]))
        print("Your area is: " + str(circleResult[1]))
    
    elif whatToLearn.lower() == "squares":
        squareWidth = float(input("What is your width: "))
        squareResult = square(squareWidth)

        print("Your width is: " + str(squareWidth))
        print("Your perimeter is: " + str(squareResult[0]))
        print("Your area is: " + str(squareResult[1]))

    elif whatToLearn.lower() == "rectangles":
        rectangleWidth = float(input("What is your width: "))
        rectangleLength = float(input("What is your length: "))
        rectangleResult = rectangle(rectangleWidth, rectangleLength)
        
        print("Your width is: " + str(rectangleWidth))
        print("Your length is: " + str(rectangleLength))
        print("Your perimeter is: " + str(rectangleResult[0]))
        print("Your area is: " + str(rectangleResult[1]))
    
    else:
        
        while goodGuess == False:
            
            newWhatToLearn = input("That input is not valid. What do you want to learn about (circles, squares, or rectangles): ")
            
            if newWhatToLearn.lower() == "circles":
                circleRadius = float(input("What is your radius: "))
                circleResult = circle(circleRadius)

                print("Your radius is: " + str(circleRadius))
                print("Your circumference is: " + str(circleResult[0]))
                print("Your area is: " + str(circleResult[1]))

                goodGuess = True

            elif newWhatToLearn.lower() == "squares":
                squareWidth = float(input("What is your width: "))
                squareResult = square(squareWidth)

                print("Your width is: " + str(squareWidth))
                print("Your perimeter is: " + str(squareResult[0]))
                print("Your area is: " + str(squareResult[1]))

                goodGuess = True

            elif newWhatToLearn.lower() == "rectangles":
                rectangleWidth = float(input("What is your width: "))
                rectangleLength = float(input("What is your length: "))
                rectangleResult = rectangle(rectangleWidth, rectangleLength)
                
                print("Your width is: " + str(rectangleWidth))
                print("Your length is: " + str(rectangleLength))
                print("Your perimeter is: " + str(rectangleResult[0]))
                print("Your area is: " + str(rectangleResult[1]))

                goodGuess = True
        
        goodGuess = False
    
    runAgain = input("Do you want to run the program again (yes or no): ")
    
    if runAgain.lower() == "yes":
        continueProgram = True
    
    elif runAgain.lower() == "no":
        continueProgram = False
    
    else:
        print("Invalid response. Ending program.")
        continueProgram = False
