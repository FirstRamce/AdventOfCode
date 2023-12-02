import re
maxDict = {"red":12,"green":13,"blue":14}
cubePattern = "(\d+) (red|blue|green)"
with open("input_2") as f:
    elves = {0:0}
    elveNr = 0
    lineNr = 0
    drawDict = {}
    game = 1
    validGamesSum = 0
    for line in f.readlines():
        print(line)
        valid = True
        for draw in line.split(";"):
            print(draw)
            match = re.search(cubePattern, draw)
            for match in re.findall(cubePattern, draw):
                drawDict[match[1]]  = match[0]
                print(drawDict)
                
            drawDict.clear()
            if not valid:
                break