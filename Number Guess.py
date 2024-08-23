minNum = int(input("Please put in your minumum number: "))
maxNum = int(input("Please put in your maximum number: "))
secretNum = int(input("Please put in your secret number: "))
maxGuesses = int(input("Please put in the maximum number of guesses: "))
firstGuess = int(input("Please put in your first guess: "))
newGuess = 0

if firstGuess != secretNum:
    if (firstGuess > secretNum) & (minNum <= firstGuess <= maxNum):
        print("Please guess again. Your number is too high.")
    elif (firstGuess < secretNum) & (minNum <= firstGuess <= maxNum):
        print("Please guess again. Your number is too low.")
    else:
        print("Your guess it out of bounds.")
    newGuess = int(input("New guess: "))

else:
    print("You guessed the correct number!")

for i in range(maxGuesses - 2):
    if newGuess != secretNum:
        if (newGuess > secretNum) & (minNum <= newGuess <= maxNum):
            print("Please guess again. Your number is too high.")
        elif (newGuess < secretNum) & (minNum <= newGuess <= maxNum):
            print("Please guess again. Your number is too low.")
        else:
            print("Your guess it out of bounds.")
        newGuess = int(input("New guess: "))
    else:
        exit

if newGuess == secretNum:
    print("You guessed the correct number!")
else:
    print("You ran out of guesses.")
