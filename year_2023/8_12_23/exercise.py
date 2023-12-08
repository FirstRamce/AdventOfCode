import re

mapPattern = '([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)'
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