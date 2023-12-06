def getFirstNumber(inputString):
    index = 0
    for element in inputString:
        if(element.isdigit()):
            return (index,int(element))
        index+=1
    return (99999,0)
    
def getLastNumber(inputString):
    index = len(inputString) -1
    inputString = inputString[::-1]
    for element in inputString:
        if(element.isdigit()):
            return (index,int(element))
        index-=1
    return (-99999,0)

def getFirstStringNumber(inputString):
    leastIndex = 99999
    resultTuple = (leastIndex, 0)
    for stringNumber in getStringValues():        
        if stringNumber in inputString:
            index = inputString.index(stringNumber)
            number = getStringValues()[stringNumber]
            if leastIndex > index:
                leastIndex = index
                resultTuple = (index, number)
    return resultTuple
        
def getLastStringNumber(inputString):
    lastIndex = -99999
    resultTuple = (lastIndex, 0)
    for stringNumber in getStringValues():        
        if stringNumber in inputString:
            index = inputString.rfind(stringNumber)
            number = getStringValues()[stringNumber]
            if lastIndex < index:
                lastIndex = index
                resultTuple = (index, number)
    return resultTuple

def getStringValues():
    stringDict = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    return stringDict

with open("input_1") as f:
    sum = 0
    while True:
        line = f.readline()
        if not line:
            break
        firstTuple = getFirstNumber(line)
        lastTuple = getLastNumber(line)
        firstNumber = firstTuple[1]
        firstStringNumber = getFirstStringNumber(line)
        lastNumber = lastTuple[1]
        lastStringNumber = getLastStringNumber(line)
        if(firstTuple[0] > firstStringNumber[0]):
            firstNumber = firstStringNumber[1]
            print(firstStringNumber)
        if(lastTuple[0] < lastStringNumber[0]):
            lastNumber = lastStringNumber[1]
            print(lastStringNumber)

        result = lastNumber + 10*firstNumber
        sum += result
    print(sum)


