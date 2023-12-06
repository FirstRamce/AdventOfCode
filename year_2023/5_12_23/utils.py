import re
import numpy as np
import sys

mapDesignationPattern="(\w+)-to-(\w+)"
mapAssignPattern="(\d+) (\d+) (\d+)"




def matchesMapDesignationLine(line):
    if(re.match(mapDesignationPattern,line)):
        return True
    return False

def matchesMapAssignLine(line):
    if(re.match(mapAssignPattern,line)):
        return True
    return False

class Mapper:

    def __init__(self, line):
        self.mappings = []
        self.extractFromTo(line)

    def extractFromTo(self, line):
        match = re.match(mapDesignationPattern,line)
        if match:
            self.fromKey = match.group(1)
            self.toKey = match.group(2)
        
    def extractAssignLine(self,line):
        match = re.match(mapAssignPattern,line)
        if match:
            self.mappings.append((int(match.group(1)),int(match.group(2)),int(match.group(3))))
    
    def mapFromNumber(self,fromNumber):
        destinationNumber = fromNumber
        for mapping in self.mappings:
            if fromNumber in range(mapping[1],mapping[1]+mapping[2]):
                destinationNumber = fromNumber + (mapping[0] - mapping[1])
                break
        return destinationNumber
    
    def smallestSource(self, mappings):
        smallest = sys.maxsize
        for range in mappings:
            if range[1] < smallest:
                smallest=range[1]
        return smallest
    
    def getIntersection(self, range1, range2):
        start = max(range1[0],range2[0])
        end = min(range1[0] + range1[1] -1, range2[0] + range2[1] -1)
        if start >= 0 and end >= 0 and start <= end:
            return (start, (end-start)+1)
        else:
            return None

    def getFilledMappings(self):
        sortedMappings = self.mappings
        sortedMappings.sort(key=lambda x: x[1])
        newMappings = []
        currentNumber = 0
        for mapping in sortedMappings:
            if mapping[1] > currentNumber:
                newMappings.append((currentNumber, currentNumber, mapping[1]-currentNumber))
            newMappings.append(mapping)
            currentNumber = mapping[1] + mapping[2]
        last = sortedMappings[len(sortedMappings)-1]
        newMappings.append((last[1]+last[2],last[1]+last[2],sys.maxsize - (last[1] +last[2])))
        print("new mappings: "+str(newMappings))
        return newMappings
        
    
    def getInputRangesSorted(self, nextRanges):
        previousRanges = []
        if nextRanges == None:
            sortedMappings = self.getFilledMappings()
            sortedMappings.sort()
            #previousRanges.append((sortedMappings[0][1],sortedMappings[0][2]))
            for mapping in sortedMappings:
                previousRanges.append((mapping[1],mapping[2]))
        else:
            sortedMappings = self.getFilledMappings()
            sortedMappings.sort()
            for range in nextRanges:
                for mapping in sortedMappings:
                    intersect  = self.getIntersection(range, (mapping[0],mapping[2]))
                    if intersect:
                        previousIntersect = (intersect[0] -(mapping[0] - mapping[1]), intersect[1])
                        if not previousIntersect in previousRanges:
                            previousRanges.append(previousIntersect)
        return previousRanges

    def __str__(self):
        return self.fromKey + " " + self.toKey + " mappings: " + str(self.mappings)
    
