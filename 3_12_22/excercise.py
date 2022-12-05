from utils import *

handler = parse_input("input.txt")
print("Excercise 1: ")
v = calculate_duplicate_priority(handler.bagpacks)
print(v)
#7553
print("Excercise 2: ")
v = handler.calculate_groups_symbol_priority()
print(v)