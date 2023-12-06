import re
from utils import *
import sys

startKey = "seed"
endKey = "location"
seedPattern="seeds:"
seedsList = []
mappers = {}
reverseMappers = {}
with open("input_5") as f:
    currentMapper = None
    for line in f.readlines():
        if line == "\n":
            continue
        if(re.match(seedPattern, line)):
            for match in re.findall("\d+", line):
                seedsList.append(int(match))
        elif(matchesMapDesignationLine(line)):
            currentMapper = Mapper(line)
            mappers[currentMapper.fromKey] = currentMapper
            reverseMappers[currentMapper.toKey] = currentMapper
        elif matchesMapAssignLine(line):
            currentMapper.extractAssignLine(line)

locations = []
for seed in seedsList:
    key = startKey
    currentNumber = seed
    while key != endKey:
        mapper = mappers[key]
        currentNumber = mapper.mapFromNumber(currentNumber)
        key = mapper.toKey
        #print("current: " + str(currentNumber) + " key: " + key + " used mapper: " + str(mapper))
    locations.append(currentNumber)
print("solution 1: " + str(min(locations)))


currentRanges = None
while key != startKey:
    mapper = reverseMappers[key]
    currentRanges = mapper.getInputRangesSorted(currentRanges)
    key = mapper.fromKey
    print("ranges: " + str(currentRanges))

seedRanges = np.asarray(seedsList).reshape(-1,2)
print("seed ranges: "+ str(seedRanges) + " seedsList: " + str(seedsList))
found = False
foundSeedRangeIntersect = None
for winRange in currentRanges:
    for seedRange in seedRanges:
        if mappers[startKey].getIntersection(winRange,seedRange):
            print("found intersection: " + str(mapper.getIntersection(winRange,seedRange)) + " between: " + str(winRange) + " " + str(seedRange))
            
            foundSeedRangeIntersect = mapper.getIntersection(winRange,seedRange)

            found = True
            break
    if found:
        break

key = startKey
currentNumber = foundSeedRangeIntersect[0]
while key != endKey:
    mapper = mappers[key]
    currentNumber = mapper.mapFromNumber(currentNumber)
    key = mapper.toKey
    #print("current: " + str(currentNumber) + " key: " + key + " used mapper: " + str(mapper))
print("solution 2 location: " + str(currentNumber))

"""
seedRanges = np.asarray(seedsList).reshape(-1,2)
lowestLocation = sys.maxsize
for seedRange in seedRanges:
    ranges = 0
    print("range " + str(ranges) + " of: " + str(len(seedRanges)))
    ranges += 1
    for seed in range(seedRange[0], seedRange[0] + seedRange[1]):
        key = startKey
        currentNumber = seed
        while key != endKey:
            mapper = mappers[key]
            currentNumber = mapper.mapFromNumber(currentNumber)
            key = mapper.toKey
            #print("current: " + str(currentNumber) + " key: " + key + " used mapper: " + str(mapper))
        if lowestLocation > currentNumber:
            lowestLocation = currentNumber
print("solution 2: " + str(lowestLocation))"""