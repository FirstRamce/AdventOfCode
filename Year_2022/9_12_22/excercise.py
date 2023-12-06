from utils_2 import *

position_handler = parse_input_file("input.txt", 1, 0)
unique_positions = []

for position in position_handler.knot_position_record:
    if not contains_vector(unique_positions, position):
        unique_positions.append(position)
print("first ex: " + str(len(unique_positions)))

position_handler = parse_input_file("input.txt", 9, 8)
unique_positions = []
for position in position_handler.knot_position_record:
    if not contains_vector(unique_positions, position):
        unique_positions.append(position)
print("second ex: " + str(len(unique_positions)))

#first ex: 6314
#second ex: 2504