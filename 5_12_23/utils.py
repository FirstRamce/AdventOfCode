import re
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
    fromKey = ""
    toKey = ""
    mappings = []

    def __init__(self, line):
        self.extractFromTo(line)

    def extractFromTo(self, line):
        match = re.match(mapDesignationPattern,line)
        if match:
            self.fromKey = match.group(1)
            self.toKey = match.group(2)
        
    def extractAssignLine(self,line):
        match = re.match(mapAssignPattern,line)
        if match:
            self.mappings.append((match.group(1),match.group(2),match.group(3)))
    
    def mapFromNumber(self,fromNumber):
        destinationNumber = fromNumber
        for mapping in self.mappings:
            if fromNumber in range(mapping[1],mapping[1]+maping[2]):
                destinationNumber = fromNumber + (mapping[0] - mapping[1])
                break
        return destinationNumber