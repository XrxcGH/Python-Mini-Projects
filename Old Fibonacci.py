# Import os for clearing the terminal
import os

# Define the fibonacci function to find the corresponding value at a given position
def fibonacci(n, side):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        print("Running fibonacci with the", n, "position on the", side, "side.")
        return (fibonacci(n-1, "L") + fibonacci(n-2, "R"))

# Define the runFibonacci function for easy terminal clearing and program running
def runFibonacci():
    os.system("clear")
    sequenceIndex = int(input("What position of the Fibonacci sequence would you like to find: "))
    print(fibonacci(sequenceIndex, "Start"))

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