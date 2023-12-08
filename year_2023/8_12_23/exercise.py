import re
import math

mapPattern = '([A-Z\d]{3}) = \(([A-Z\d]{3}), ([A-Z\d]{3})\)'
directionsPattern = '\w+'
directions = None
mapDict = {}
with open("input") as f:
    for line in f.readlines():
        mapMatch = re.match(mapPattern,line)
        if line == "\n":
            continue
        if mapMatch:
            mapDict[mapMatch.group(1)] = (mapMatch.group(2),mapMatch.group(3))
            continue
        if not mapMatch and ("R" in line or "L" in line):
            directions = re.match(directionsPattern, line)[0]
print(directions)
print(mapDict)

currentLocation = "AAA"
steps = 0
while not "ZZZ" in currentLocation:
    stepIndex = steps % len(directions)
    lr = 0
    if directions[stepIndex] == "R":
        lr = 1
    currentLocation = mapDict[currentLocation][lr]
    steps+=1
print(steps)

#Second exercise
beginningValues = []
for key in mapDict.keys():
    if str.endswith(key,"A"):
        beginningValues.append(key)

stepsList = []
for value in beginningValues:
    current = value
    steps = 0
    while not str.endswith(current, "Z"):
        stepIndex = steps % len(directions)
        lr = 0
        if directions[stepIndex] == "R":
            lr = 1
        current = mapDict[current][lr]
        steps+=1
    stepsList.append(steps)

lcm = 1
for stepAmount in stepsList:
    lcm = math.lcm(lcm, stepAmount)
print("second result: " +str(lcm))