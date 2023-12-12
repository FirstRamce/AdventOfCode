import re
import copy

class Spring:
    
    def __init__(self, springConditions, controlNumbers):
        self.springConditions = machinePart
        self.controlNumbers = controlNumbers
    
    #change from left to right (recursive) and dont continue withthe paths, that contain an illegal statement (# and . that are not possible)

springList = []
with open("input") as f:
    for line in f.readlines():
        springList.append(Spring(line.split(" ")[0],line.split(" ")[1]))
        machinePart = line.split(" ")[0]
        countingPart = line.split(" ")[1]
