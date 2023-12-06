from utils import *
import sys

file_system_space = 70000000

root_dir = parse_command_input("input.txt")
needed_space = 30000000 - (70000000-root_dir.calculate_item_size())
folders_sub_max = get_folder_list_sub_size(root_dir, 100000)
final_size = 0
for folder in folders_sub_max:
    final_size+= folder.calculate_item_size()
print("ex_1: " + str(final_size))

folders_above_min = get_folder_list_above_size(root_dir, needed_space)

smallest = sys.maxsize
for folder in folders_above_min:
    f_value = folder.calculate_item_size()
    if smallest > f_value:
        smallest = f_value

print("ex_2: " + str(smallest))

#first answer: 1243729
#second answer: 4443914