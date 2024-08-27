# Imports initializing
import os

# Variables initializing
playing = True

# Define the string difference identification function
def first_diff(strOne = "", strTwo = ""):

    # Convert both strings to lowercase to avoid capitalization errors
    strOne = strOne.lower()
    strTwo = strTwo.lower()

    # Return a value of -1 if the strings are the same OR run a loop until the characters in the same position are not the same and return that position
    if strOne == strTwo:
        return -1
    else:
        for i in range(len(strOne)):
            if strOne[i] != strTwo[i]:
                return i

# Run a loop to continue playing until the user decides to exit
while playing == True:
    
    # Clear the console after every use
    os.system("clear")

    # Take user input
    strInputOne = input("What is your first string: ")
    strInputTwo = input("What is your second string: ")

    # Call the string difference function with the user input
    if first_diff(strOne = strInputOne, strTwo = strInputTwo) == -1:
        print("Your strings are the same.")
    else:
        print("Your strings differ at position: " + str(first_diff(strOne = strInputOne, strTwo = strInputTwo)))
    
    # Ask user if they want to play again and update loop value correspondingly
    playAgain = input("Would you like to play again (type yes or no)? ")
    if playAgain.lower() != "yes":
        playing = False
