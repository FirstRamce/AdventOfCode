from utils import *
import copy

first_cave = parse_input_file("input.txt")
second_cave = copy.deepcopy(first_cave)
print(first_cave.cave_map)
drop_point = Vector(0,500)
number_of_sand = 0
while first_cave.drop_sand(drop_point,1000):
    number_of_sand+=1
print("Exercise 1: " + str(number_of_sand) + " cave number: " + str(first_cave.stuck_sand))

lowest_row = 0
current = 0
while True:
    if current in second_cave.cave_map:
        lowest_row = current
    elif current -lowest_row > 100:
        break
    current+=1

print("absolut ground: " + str(lowest_row))

second_cave.set_ground_zero(lowest_row+2)
number_of_sand = 0
while second_cave.drop_sand_with_ground(drop_point,0):
    number_of_sand+=1
print("Exercise 2: " + str(number_of_sand) + " cave number: " + str(second_cave.stuck_sand))


for i in range(164):
    for j in range(330, 620):
        if i in second_cave.cave_map and j in second_cave.cave_map[i]:
            print(second_cave.cave_map[i][j], end="")
        else:
            print(".", end="")
    print("")