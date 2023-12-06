from utils import *
from datetime import datetime


input = parse_input("input.txt")

begin_unique = alternative(4,input)
print("EX 1: " + str(begin_unique+4))

new_unique = alternative(14,input)
print("EX 2: " + str(new_unique+14))

#first after code: 1640
#new Unique: 3599