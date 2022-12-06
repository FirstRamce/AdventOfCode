from utils import *

input = parse_input("input.txt")

begin_unique = get_first_x_different(4,input)
print("first after code: " + str(begin_unique+4))

new_unique = get_first_x_different(14,input)
print("first aftere message: " + str(new_unique+14))

#first after code: 1640
#new Unique: 3599