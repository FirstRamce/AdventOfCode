import re

directionsDict = {"|":((-1,0),(1,0)),"-":((0,-1),(0,1)), "L":((-1,0),(0,1)),"J":((-1,0),(0,-1)),"7":((0,-1),(1,0)),"F":((1,0),(0,1))}
directions = [(1,0),(-1,0),(0,1),(0,-1)]
pipeMap = []

with open("input") as f:
    for line in f.readlines():
        row = []
        for char in line:
            if not "\n" in char:
                row.append(char)
        pipeMap.append(row)

def addPositions(pos, add):
    return (pos[0]+add[0], pos[1]+add[1])

def isInRange(pos, rows, cols):
    if pos[0] < 0 or pos[0] >= rows:
        return False
    if pos[1] < 0 or pos[1] >= cols:
        return False
    return True

def getResolvedFromTo(position, connector):
    return ((position[0]+connector[0][0],position[1]+connector[0][1]),(position[0]+connector[1][0],position[1]+connector[1][1]))

def getConnectorNextPosition(startPosition, connectorFromTo):
    if connectorFromTo == None:
        return None
    if connectorFromTo[0][0] == startPosition[0] and connectorFromTo[0][1] == startPosition[1]:
        return connectorFromTo[1]
    elif connectorFromTo[1][0] == startPosition[0] and connectorFromTo[1][1] == startPosition[1]:
        return connectorFromTo[0]
    return None


rows = len(pipeMap)
cols = len(pipeMap[0])
for r in range(0,rows):
    for c in range(0,cols):
        if pipeMap[r][c] == "S":
            startPos = (r,c)
steps=[startPos]

for direction in directions:
    nPos = addPositions(startPos, direction)
    if isInRange(nPos, rows, cols) and pipeMap[nPos[0]][nPos[1]] in directionsDict.keys() and getConnectorNextPosition(startPos, getResolvedFromTo(nPos,directionsDict[pipeMap[nPos[0]][nPos[1]]])) != None:
        nextStep = nPos
        break

currentStep = startPos
while not nextStep == startPos:
    newStep = getConnectorNextPosition(currentStep, getResolvedFromTo(nextStep,directionsDict[pipeMap[nextStep[0]][nextStep[1]]]))
    currentStep = nextStep
    nextStep = newStep
    steps.append(currentStep)
print("solution 1: "+ str((len(steps)/2)))