import re

directionsDict = {"|":((-1,0),(1,0)),"-":((0,-1),(0,1)), "L":((1,0),(0,1)),"J":((1,0),(0,-1)),"7":((0,-1),(1,0)),"F":((0,1),(-1,0))}
pipeMap = []

with open("input") as f:
    for line in f.readlines():
        row = []
        for char in line:
            if not "\n" in char:
                row.append(char)
        pipeMap.append(row)
print(pipeMap)

def isConnectable(startPosition, connector):
    if connector in directionsDict.keys():
        fromTo = directionsDict[connector]
        if fromTo[0][0] == startPosition[0] and fromTo[0][1] == startPosition[1]:
            return True
        if fromTo[1][0] == startPosition[0] and fromTo[1][1] == startPosition[1]:
            return True
    return False

