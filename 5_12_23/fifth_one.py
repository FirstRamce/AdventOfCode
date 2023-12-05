import re
from utils import *

startKey = "seed"
endKey = "location"
seedPattern="seeds:"
seedsList = []
mappers = {}
with open("input_5") as f:
    currentMapper = None
    for line in f.readlines():
        if line == "\n":
            continue
        if(re.match(seedPattern, line)):
            for match in re.findall("\d+", line):
                seedsList.append(int(match))
        if(matchesMapDesignationLine(line)):
            currentMapper = Mapper(line)
            mappers[currentMapper.fromKey] = currentMapper
        else if matchesMapAssignLine(line):
            currentMapper.extractAssignLine(line)
        

print(seedsList)