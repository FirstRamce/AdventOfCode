import re

def isAdjacentToStar(numberTuple, field):
    startLine = max(numberTuple[0] -1, 0)
    endLine = min(numberTuple[0] +1, len(field) -1)
    startColumn = max(numberTuple[1] -1, 0)
    endColumn = min(numberTuple[2], len(field[0]) -1)

    found = False
    for lInt in range(startLine, endLine+1):
        for cInt in range(startColumn, endColumn+1):
            if field[lInt][cInt] == '*':
                return (lInt,cInt)
    return None

def numberAdjacent(numberTuple, field):
    startLine = max(numberTuple[0] -1, 0)
    endLine = min(numberTuple[0] +1, len(field) -1)
    startColumn = max(numberTuple[1] -1, 0)
    endColumn = min(numberTuple[2], len(field[0]) -1)

    found = False
    for lInt in range(startLine, endLine+1):
        for cInt in range(startColumn, endColumn+1):
            if field[lInt][cInt] != '.' and not field[lInt][cInt].isdigit():
                found = True
                break
        if found:
            break
    return found


numberPattern = "\d+"
gearField =  []
numbers = []
with open("input_3") as f:
    lineNr = 0
    for line in f.readlines():
        gearField.append([])
        for match in re.finditer(numberPattern, line):
            numbers.append((lineNr, match.start(),match.end(),match.group()))
        for char in line:
            if(char != "\n"):
                gearField[lineNr].append(char)
        lineNr += 1

for ar1 in gearField:
    print(ar1)
sum = 0
for tuple in numbers:
    if numberAdjacent(tuple, gearField):
        sum += int(tuple[3])
print(sum)
gearDict = {}
for tuple in numbers:
    starTuple = isAdjacentToStar(tuple, gearField)
    if starTuple != None:
        if starTuple in gearDict:
            gearDict[starTuple].append(int(tuple[3]))
        else:
            gearDict[starTuple] = [int(tuple[3])]
gearSum = 0
print(gearDict)
for key, value in gearDict.items():
    if len(value) == 2:
        gearSum += value[0] * value[1]
    else:
        print(value)
print(gearSum)