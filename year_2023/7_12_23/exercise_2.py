import re
import functools

cardValuesOrdered = "AKQT98765432J"
numberPattern = "\d+"
handPattern = "([AKQT98765432J]{5}) (\d+)"
handBidList = []
with open("input") as f:
    for line in f.readlines():
        match = re.match(handPattern, line)
        handBidList.append((match.group(1),int(match.group(2))))
"""
def isJokerFullhouse(numberOfJokers, occurenceDict):
    if numberOfJokers == 0:
        return False
    if numberOfJokers == 3:
        return True
    if numberOfJokers == 2:
        return True
    if list(occurenceDict.values()).count(2) == 2:
        return True
    """

def getTypeValue(hand):
    occurenceDict = {}
    numberOfJokers = 0
    occurenceDict["J"] = 0
    for card in hand:
        if card == "J":
            numberOfJokers +=1
        else:
            if not card in occurenceDict:
                occurenceDict[card] = 0
            occurenceDict[card] += 1
    hType = 6
    if (5-numberOfJokers) in occurenceDict.values():
        hType= 0
    elif (4-numberOfJokers) in occurenceDict.values():
        hType = 1
    elif (3 in occurenceDict.values() and 2 in occurenceDict.values()) or (list(occurenceDict.values()).count(2) == 2 and numberOfJokers > 0):
        hType = 2
    elif (3-numberOfJokers) in occurenceDict.values():
        hType = 3
    elif list(occurenceDict.values()).count(2) == 2:
        hType = 4
    elif (2-numberOfJokers) in occurenceDict.values():
        hType = 5
    return hType

def compareHands(handBid1,handBid2):
    hand1 = handBid1[0]
    hand2 = handBid2[0]
    type1 = getTypeValue(hand1)
    type2 = getTypeValue(hand2)
    if type1 < type2:
        return -1
    elif type2 < type1:
        return 1
    else:
        for pos in range(0,len(hand1)):
            if cardValuesOrdered.index(hand1[pos]) < cardValuesOrdered.index(hand2[pos]):
                return -1
            elif cardValuesOrdered.index(hand2[pos]) < cardValuesOrdered.index(hand1[pos]):
                return 1
    return 0

sortedHandBidList = sorted(handBidList, key=functools.cmp_to_key(compareHands))
sortedHandBidList.reverse()
rank = 1
sum = 0
for play in sortedHandBidList:
    value = (rank * play[1])
    sum += value
    rank += 1
print(sum)