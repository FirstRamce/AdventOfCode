import re

nRegex = "-{0,1}\d+"
numberSequences = []
with open("input") as f:
    for line in f.readlines():
        match = re.findall(nRegex,line)
        if len(match) >0:
            numberSequences.append(match)

def allNumbersZero(layer):
    for num in layer:
        if num != 0:
            return False
    return True

allLayers = []
for sequence in numberSequences:
    layers = []
    l = []
    for nStr in sequence:
        l.append(int(nStr))
    layers.append(l)
    currentLayer = layers[0]
    while not allNumbersZero(currentLayer):
        newL = []
        for i in range(0,len(currentLayer)-1):
            newL.append( currentLayer[i+1] - currentLayer[i])
        layers.append(newL)
        currentLayer = newL
    allLayers.append(layers)

lastNumbers = []
for layers in allLayers:
    layers.reverse()
    for lIndex in range(1,len(layers)):
        pLayer = layers[lIndex-1]
        if len(pLayer) > lIndex:
            pLast = pLayer[len(pLayer)-1]
        else:
            pLast = 0
        cLayer = layers[lIndex]
        cLast = cLayer[len(cLayer)-1]
        cLayer.append(cLast + pLast)
    layers.reverse()
    lastNumbers.append(layers[0][len(layers[0])-1])
sum = 0

for lastNum in lastNumbers:
    sum+=lastNum
print("first solution: "+str(sum))


previousNumbers = []
for layers in allLayers:
    layers.reverse()
    for lIndex in range(1,len(layers)):
        pLayer = layers[lIndex-1]
        if len(pLayer) > lIndex:
            pFirst = pLayer[0]
        else:
            pFirst = 0
        cLayer = layers[lIndex]
        cFirst = cLayer[0]
        cLayer.insert(0,cFirst - pFirst)
    layers.reverse()
    previousNumbers.append(layers[0][0])

previousSum = 0
for lastNum in previousNumbers:
    previousSum+=lastNum
print("second solution: "+str(previousSum))

