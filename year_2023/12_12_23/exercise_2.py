import re
from itertools import combinations
from functools import cache

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


    #change from left to right (recursive) and dont continue withthe paths, that contain an illegal statement (# and . that are not possible)
    #Nonogram solution: https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4
methodCalls = [0]
@cache
def countVariants(pattern, splits):
    size=len(pattern)
    methodCalls[0] +=1
    if len(splits) == 0:
        if all(c in ".?" for c in pattern):
            return 1
        return 0
    
    cSplit = splits[0]
    rest = splits[1:]
    minAfter = sum(rest) + len(rest)-1
    count = 0

    for before in range(size - minAfter - cSplit):
        cPattern = "." * before + "#"*cSplit + "."
        if (all(c0 == c1 or c0 == "?" for c0,c1 in zip(pattern, cPattern))):
            count += countVariants(pattern[len(cPattern):], rest)
    return count



springListFoldUp = []
foldUpAmount = 5
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
    validVariants = countVariants(spring.springConditions, tuple(spring.controlNumbers))
    sumVariants += validVariants
print("solution 2: "+ str(sumVariants))
print(methodCalls)