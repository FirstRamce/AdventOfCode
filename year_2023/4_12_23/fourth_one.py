import re

numberPattern = "\d+"
with open("input_4") as f:
    cardSum = 0
    cardsDict = {}
    lineNr = 1
    for line in f.readlines():
        numberLine = line[line.index(":")+1:]
        winningNumbers = numberLine.split("|")[0]
        ownNumbers = numberLine.split("|")[1]
        winningList = []
        for match in re.findall(numberPattern, winningNumbers):
            winningList.append(int(match))
        ownList = []
        for match in re.findall(numberPattern, ownNumbers):
            ownList.append(int(match))
        appearences = 0
        for number in ownList:
            if number in winningList:
                appearences+=1
        cardsDict[lineNr] = appearences
        if appearences != 0:
            cardSum += 2**(appearences-1)
        
        lineNr+=1
print(cardSum)
copyDict = {}
for key in cardsDict:
    copyDict[key] = 1

for key, value in cardsDict.items():
    amountOfCards = copyDict[key]
    for copyKey in range(key+1, key + value +1):
        if copyKey in copyDict:
            copyDict[copyKey] = copyDict[copyKey] + amountOfCards

scratchCards = 0
for key, value in copyDict.items():
    scratchCards += value
print(cardsDict)
print(copyDict)
print(scratchCards)


    
