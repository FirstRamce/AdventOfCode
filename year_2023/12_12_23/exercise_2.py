import re
from itertools import combinations

numberPattern = "\d+"
functioningPartsPattern = "(#+)"
class Spring:
    
    def __init__(self, springConditions, controlNumbers):
        self.springConditions = springConditions
        self.controlNumbers = []
        self.validVariants = []
        self.numValidVariants = 0
        for match in re.findall(numberPattern, controlNumbers):
            self.controlNumbers.append(int(match))
        
    def __str__(self):
        return "Spring: " + self.springConditions +" - " + str(self.controlNumbers)

    def validStartPositionForGroup(self, startPosition, groupIndex):
        fieldsAmount = self.controlNumbers[groupIndex]
        for i in range(startPosition, startPosition + fieldsAmount):
            if not self.springConditions[i] == "#" and not self.springConditions[i] == "?":
                return False
        if len(self.springConditions) <= startPosition + fieldsAmount or self.springConditions[startPosition + fieldsAmount] == "." or self.springConditions[startPosition + fieldsAmount] == "?":
            return True
        return False
                
    
    def getAmountOfVariants(self):
        emptySlots = len(self.springConditions) - sum(self.controlNumbers) -len(self.controlNumbers) + 1
        options = combinations(range(len(self.controlNumbers) + emptySlots), len(self.controlNumbers))
        validOptions = 0
        for possibility in options:
            addIndex = 0
            groupIndex = 0
            impossible = False
            for pos in possibility:
                if not self.validStartPositionForGroup(pos + addIndex,groupIndex):
                    impossible = True
                    break
                addIndex += (self.controlNumbers[groupIndex])
                groupIndex += 1
            print(possibility)
            if not impossible:
                print("valid option: " + str(possibility))
                validOptions += 1
        return validOptions


    #change from left to right (recursive) and dont continue withthe paths, that contain an illegal statement (# and . that are not possible)
    #Nonogram solution: https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4

springListFoldUp = []
foldUpAmount = 1
with open("input") as f:
    for line in f.readlines():
        machinePart = line.split(" ")[0]
        countingPart = line.split(" ")[1]
        countingPart = countingPart.replace("\n","")
        countingPart += ","
        foldUpCountingPart = ""
        foldUpMachinePart = ""
        for i in range(0,foldUpAmount):
            foldUpMachinePart += (machinePart + "?")
            foldUpCountingPart += (countingPart)
        foldUpMachinePart = foldUpMachinePart[:-1]
        springListFoldUp.append(Spring(foldUpMachinePart, foldUpCountingPart))

sumVariants = 0
for spring in springListFoldUp:
    validVariants = spring.getAmountOfVariants()
    sumVariants += validVariants
print("solution 2: "+ str(sumVariants))
