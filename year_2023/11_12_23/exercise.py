import re
import copy

galaxyMap = []
with open("input") as f:
    for line in f.readlines():
        row = []
        for char in line:
            if not "\n" in char:
                row.append(char)
        galaxyMap.append(row)

galaxyRowDict = {}
galaxyColDict = {}
galaxyList = []
for iRow in range(0,len(galaxyMap)):
    row = galaxyMap[iRow]
    galaxyRowDict[iRow] = 0
    for iCol in range(0, len(row)):
        if row[iCol] == "#":
            galaxyList.append((iRow, iCol))
            galaxyRowDict[iRow] = galaxyRowDict[iRow] + 1
            if not iCol in galaxyColDict:
                galaxyColDict[iCol] = 1
            else:
                galaxyColDict[iCol] = galaxyColDict[iCol] + 1
        elif not iCol in galaxyColDict:
            galaxyColDict[iCol] = 0
print(galaxyMap)
print("row dict: " + str(galaxyRowDict))
print("col dict: " + str(galaxyColDict))

def modifyGalaxyIndex(galaxyList, startPos, isRow, amount):
    modifyIndex = 0
    if not isRow:
        modifyIndex = 1
    for galaxy in galaxyList:
        if galaxy[modifyIndex] > startPos:
            if isRow:
                newPos = (galaxy[modifyIndex] + amount, galaxy[1])
            else:
                newPos = (galaxy[0], galaxy[modifyIndex] + amount)
            galaxyList[galaxyList.index(galaxy)] = newPos
        
biggerMap = galaxyMap
rowExpand = 0
modifiedGalaxyList = copy.deepcopy(galaxyList)
driftAmount = 1
for key, value in galaxyRowDict.items():
    if value == 0:
        addIndex = key + rowExpand
        modifyGalaxyIndex(modifiedGalaxyList, addIndex, True, driftAmount)
        rowExpand += driftAmount
colExpand = 0
for key, value in galaxyColDict.items():
    if value == 0:
        addIndex = key + colExpand
        modifyGalaxyIndex(modifiedGalaxyList, addIndex, False, driftAmount)
        colExpand +=driftAmount


for row in biggerMap:
    print(row)

def calculateDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

distanceSum = 0
for i in range(0,len(modifiedGalaxyList)):
    for j in range(i+1,len(modifiedGalaxyList)):
        distanceSum += calculateDistance(modifiedGalaxyList[i], modifiedGalaxyList[j])
print("solution 1: " + str(distanceSum))


modifiedGalaxyList = copy.deepcopy(galaxyList)
driftAmount = 999999
rowExpand = 0
for key, value in galaxyRowDict.items():
    if value == 0:
        addIndex = key + rowExpand
        modifyGalaxyIndex(modifiedGalaxyList, addIndex, True, driftAmount)
        rowExpand += driftAmount
colExpand = 0
for key, value in galaxyColDict.items():
    if value == 0:
        addIndex = key + colExpand
        modifyGalaxyIndex(modifiedGalaxyList, addIndex, False, driftAmount)
        colExpand +=driftAmount

distanceSum2 = 0
for i in range(0,len(galaxyList)):
    for j in range(i+1,len(modifiedGalaxyList)):
        distanceSum2 += calculateDistance(modifiedGalaxyList[i], modifiedGalaxyList[j])
print("solution 2: " + str(distanceSum2))