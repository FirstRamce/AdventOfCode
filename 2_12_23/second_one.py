import re
maxDict = {"red":12,"green":13,"blue":14}
cubePattern = "(\d+) (red|blue|green)"
with open("input_2") as f:
    maxDrawDict = {}
    game = 1
    validGamesSum = 0
    fewestDiceSum = 0
    for line in f.readlines():
        valid = True
        for draw in line.split(";"):
            for match in re.findall(cubePattern, draw):
                if(not match[1] in maxDrawDict or maxDrawDict[match[1]] < int(match[0])):
                    maxDrawDict[match[1]]  = int(match[0])
                if maxDict[match[1]] < int(match[0]):
                    valid = False
        mult = 1    
        print(maxDrawDict)
        for key, value in maxDrawDict.items():
            mult *= value
        fewestDiceSum += mult
        maxDrawDict.clear()
        if valid:
            validGamesSum += game
        game +=1
    print(validGamesSum)
    print(fewestDiceSum)