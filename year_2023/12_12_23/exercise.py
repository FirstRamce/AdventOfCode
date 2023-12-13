import re
import copy

numberPattern = "\d+"
functioningPartsPattern = "(#+)"
class Spring:
    
    
    def __init__(self, springConditions, controlNumbers):
        self.springConditions = springConditions
        self.controlNumbers = []
        self.validVariants = []
        for match in re.findall(numberPattern, controlNumbers):
            self.controlNumbers.append(int(match))
        
    def __str__(self):
        return "Spring: " + self.springConditions +" - " + str(self.controlNumbers)

    def isValidComplete(self, machineInput):
        if "?" in machineInput:
            return False
        else:
            i = 0
            for match in re.findall(functioningPartsPattern, machineInput):
                if i >= len(self.controlNumbers) or not len(match) == self.controlNumbers[i]:
                    return False
                i+=1
            if i == len(self.controlNumbers):
                return True
            return False

    def isValidUntilNext(self, machineInput):
        if not "?" in machineInput:
            return this.isValidComplete(machineInput)
        checkUntil = machineInput.index("?")
        i = 0
        for match in re.finditer(functioningPartsPattern, machineInput):
            if match.end() < checkUntil:
                if i >= len(self.controlNumbers) or not len(match.group(1)) == self.controlNumbers[i]:
                    return False
            else:
                return True
            i += 1
        return True
                

    def modifyNext(self, machineInput):
        if "?" in machineInput:
            if self.isValidUntilNext(machineInput):
                self.modifyNext(machineInput.replace("?",".",1))
                self.modifyNext(machineInput.replace("?","#",1))
        else:
            if self.isValidComplete(machineInput):
                self.validVariants.append(machineInput)

    def getValidConfigurations(self):
        self.validVariants = []
        self.modifyNext(self.springConditions)
        return self.validVariants


    
    #change from left to right (recursive) and dont continue withthe paths, that contain an illegal statement (# and . that are not possible)

springList = []
with open("input") as f:
    for line in f.readlines():
        springList.append(Spring(line.split(" ")[0],line.split(" ")[1]))
        machinePart = line.split(" ")[0]
        countingPart = line.split(" ")[1]

sumVariants = 0
for spring in springList:
    validVariants = spring.getValidConfigurations()
    sumVariants += len(validVariants)
print("solution 1: "+ str(sumVariants))