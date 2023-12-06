from utils import *

sensor_list = parse_input_file("input.txt")
beacon_list = parse_beacon_list("input.txt")
y_to_check = 2000000

combined_areas = get_combined_blocked_areas(sensor_list, y_to_check)
amount_of_blocked = 0
print(combined_areas)
for combined in combined_areas:
    if combined:
        amount_of_blocked+= (combined[1]-combined[0]+1)

checked_beacons = []
for beacon in beacon_list:
    if beacon.y == y_to_check and not beacon in checked_beacons:
        #print("beacon: " + str(beacon.x) + " : " + str(beacon.y))
        checked_beacons.append(beacon)
        amount_of_blocked-=1
print(amount_of_blocked)

beacon_bound_low = 0
beacon_bound_high = 4000000

for i in range(beacon_bound_low,beacon_bound_high):
    combined_areas = get_combined_blocked_areas(sensor_list, i)
    if len(combined_areas) > 1:
        for area in combined_areas:
            if combined_areas.index(area) < len(combined_areas)-1:
                print("on line:" + str(i)+" : "+str(combined_areas) + " with possible Location: "+str(area[1]+1)+":"+str(i))
                result = 4000000*(area[1]+1)+i
                print("Exercise 2: calculations x*4000000+y : " + str(result))
                
#1: 5147333
#2: 13734006908372

