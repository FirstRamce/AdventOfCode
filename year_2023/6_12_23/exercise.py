import re

numberPattern = "\d+"
indexTimeDict = {}
raceDict = {}
longRaceTime = 0
longRaceDistance = 0
with open("input") as f:
    for line in f.readlines():
        if "Time" in line:
            concatedTimes = ""
            index = 0
            for match in re.findall(numberPattern,line):
                raceDict[int(match)] = 0
                indexTimeDict[index] = int(match)
                concatedTimes += match
                index+=1
            longRaceTime = int(concatedTimes)
            
        elif "Distance" in line:
            index=0
            concatedDistance = ""
            for match in re.findall(numberPattern,line):
                raceDict[indexTimeDict[index]] = int(match)
                concatedDistance+=match
                index+=1
            longRaceDistance = int(concatedDistance)

recordProduct = 1
for key, value in raceDict.items():
    possibleWins = 0
    for pressTime in range(1,key):
        if (pressTime * (key-pressTime)) > value:
            possibleWins +=1
    recordProduct *= possibleWins

print(raceDict)
print("solution 1: "+str(recordProduct))

possibleWins = 0
print("time: "+str(longRaceTime)+" distance: "+str(longRaceDistance))
for pressTime in range(1,longRaceTime):
    if (pressTime * (longRaceTime-pressTime)) > longRaceDistance:
        possibleWins +=1
print("solution 2: "+str(possibleWins))

