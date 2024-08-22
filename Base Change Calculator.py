firstNum = input("Number to convert (no commas): ")
firstBase = int(input("Base of the first number: "))
newBase = int(input("Base of the new number: "))

firstIndex = 0
calcIndex = int(len(firstNum)) - 1
secondIndex = -1
tempNum = 0
tempNumList = []
secondNum = 0
secondNumList = []

for i in range(len(firstNum)):
    firstNumIndex = int(firstNum[firstIndex])
    tempNum += firstNumIndex * (firstBase ** calcIndex)
    firstIndex += 1
    calcIndex -= 1

while (tempNum / newBase) !=0:
    tempNumList.append(str(tempNum % newBase))
    tempNum = tempNum // newBase

for i in range(len(tempNumList)):
    secondNumList.append(tempNumList[secondIndex])
    secondIndex -= 1

secondNum = int("".join(secondNumList))

print("New number in base " + str(newBase) + ": " + str(secondNum))