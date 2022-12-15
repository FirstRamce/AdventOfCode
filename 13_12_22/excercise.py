from utils import *
import functools

def compare_containers(item1, item2):
    if not item1:
        return -1
    elif not item2:
        return 1
    #print("item1: " + str(item1) + " type: " + str(type(item1)))
    #print("item2: " + str(item2) + " type: " + str(type(item2)))
    return compare_two_containers(item1, item2)*-1
 
pairs = parse_input_file("input.txt")

index = 1
sum=0
container_list = []
for pair in pairs:
    if pair.compare_containers() > 0:
        #print("index: " +str(index) + "")
        #print("container_1: " + pair.first_container.get_string())
        #print("container_2: " + pair.second_container.get_string())
        sum +=index    
    container_list.append(pair.first_container)
    container_list.append(pair.second_container)
    if not pair.first_container:
        print("Added an empty container 1 ")
    if not pair.second_container:
        print("Added an empty container 2")
    index+=1

print("EX 1: " + str(sum))
divider_packet_1 = Container(None)
divider_packet_2 = Container(None)
c_2 = Container(divider_packet_1)
c_6 = Container(divider_packet_2)
c_2.add_value(2)
c_6.add_value(6)
divider_packet_1.add_value(c_2)
divider_packet_2.add_value(c_6)
container_list.append(divider_packet_1)
container_list.append(divider_packet_2)
sorted_list = sorted(container_list, key=functools.cmp_to_key(compare_containers))

print("Ex 2: " +str((sorted_list.index(divider_packet_1)+1) * (sorted_list.index(divider_packet_2)+1)))