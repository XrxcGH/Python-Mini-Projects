# Import os for clearing the terminal
import os

# Define the fibonacci function to find the corresponding value at a given position
def fibonacci(position):
    sequenceList = [1, 1]
    posGood = True
    if position == 1 or position == 2:
        return 1
    elif position <= 0:
        return 0
    else:
        while posGood == True:
            if position != 2:
                sequenceList.append(sequenceList[-1] + sequenceList[-2])
                position -= 1
            else:
                posGood = False
        return sequenceList[-1]

# Define the runFibonacci function for easy terminal clearing and program running
def runFibonacci():
    os.system("clear")
    sequenceIndex = int(input("What position of the Fibonacci sequence would you like to find: "))
    print(fibonacci(sequenceIndex))

# Run main program
runFibonacci()
keepGoing = True
while keepGoing == True:
    goAgain = input("Would you like to continue (yes or no): ")
    if goAgain.lower() == "yes":
        runFibonacci()
    elif goAgain.lower() == "no":
        keepGoing = False
    else:
        print("Invalid input. Cancelling program.")
        keepGoing = False