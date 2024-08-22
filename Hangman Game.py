# Import initializing
import os

# Variable initializing
secretWord = input("Enter secret word: ")
numGuesses = int(input("Enter number of guesses: "))
indexPos = 0
wordArray = []
posArray = []
posString = ""
tempString = ""
newGuess = ""

# Clear the terminal after taking user input to keep the secret word hidden
os.system("clear")

# Get word length by modifying array length
for i in range(len(secretWord)):
    wordArray.append("_")

# Display word length as a string instead of an array
tempString = "".join(wordArray)
print("Your word is " + str(len(secretWord)) + " letters long. You have " + str(numGuesses) + " guesses. Current word: " + tempString)

# While loop continues until the number of guesses reaches 0 or the secret word is guessed
while numGuesses > 0:
    newGuess = input("Please enter your letter to guess: ")

    # Get letter positions storeded in an array to track current word progress
    # Get letter postition indexes stored in an array to output to player
    for i in range(len(secretWord)):
        if secretWord[indexPos] == newGuess:
            wordArray[i] = newGuess
            posArray.append(str(i + 1))
        indexPos += 1
    posString = ", ".join(posArray)
    tempString = "".join(wordArray)

    # Displayable outputs based on correct letter guesses
    if newGuess in secretWord:

        # Exit while loop if all letters in the secret word have been guessed
        if tempString == secretWord:
            print("Your letter is in position(s): " + posString + ". Current word: " + tempString)
            numGuesses = 0
        
        # Continue while loop if not all letters in the secret word have been guessed
        else:
            print("Your letter is in position(s): " + posString + ". Current word: " + tempString)
            print("Guesses left: " + str(numGuesses))
    
    # Displayable outputs based on incorrect letter guesses
    else:
        print("That letter in not in the secret word.")
        numGuesses -= 1
        if numGuesses != 0:
            print("Guesses left: " + str(numGuesses))
    indexPos = 0
    posArray.clear()

# Final displayable outputs based on if the secret word was guessed or if the number of guesses reached 0
if tempString == secretWord:
    print("You have guessed the secret word! It was: " + secretWord)
else:
    print("You ran out of guesses. The secret word was: " + secretWord)