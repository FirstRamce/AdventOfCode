with open("input_1") as f:
    elves = {0:0}
    elveNr = 0
    lineNr = 0
    while True:
        lineNr = lineNr + 1
        line = f.readline()
        if line == "\n":
            elveNr =  elveNr+1
            elves[elveNr]=0
        elif line :
            try:
                elves[elveNr] = (int(line) + elves[elveNr])
            except:
                print("Exception in input line "  + str(lineNr))
        if not line:
            break
    maxNumber=0
    sortedElves = {k: v for k, v in sorted(elves.items(), key=lambda item: item[1], reverse=True)}

    i = 0
    sum =  0
    for elve in sortedElves:
        if i == 1:
            print("first result: ")
            print(elve)
        if i == 3:
            break
        sum = sum + sortedElves[elve]
        i+=1
    print("second result: ")
    print(sum)