from last_util import *
import functools


coordinate_list = import_coordinate_file("input")
sorted(coordinate_list, key=functools.cmp_to_key(compare_coordinates))
c_holder = Constellation_holder()

for coordinate in coordinate_list:
    c_holder.add_coordinate(coordinate)

c_holder.clear_intersections()


for list in c_holder.constellation_list:
    printStr = "["
    for coor in list:
        printStr+=str(coor)+","
    printStr = printStr[:len(printStr)-1] + "]"
    print (printStr)

print("amount of constellations: " + str(len(c_holder.constellation_list)))