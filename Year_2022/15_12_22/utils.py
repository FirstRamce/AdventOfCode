import re
import functools

regex = r'Sensor at x=(-{0,1}\d+), y=(-{0,1}\d+): closest beacon is at x=(-{0,1}\d+), y=(-{0,1}\d+)'

#coordinates are always in the 4-dimensions
def calculate_manhatten(coordinates_1, coordinates_2):
    distance = 0
    distance+= abs(coordinates_1.x - coordinates_2.x)
    distance+= abs(coordinates_1.y - coordinates_2.y)
    
    return distance


def parse_beacon_list(filename):
    beacon_list=[]
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            match = re.search(regex,line)
            if match:
                beacon_list.append(Coordinate(int(match.group(3)),int(match.group(4))))
    return beacon_list


def parse_input_file(filename):
    sensor_list=[]
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            match = re.search(regex,line)
            if match:
                sensor_list.append(Sensor(int(match.group(1)),int(match.group(2)),int(match.group(3)),int(match.group(4))))
    return sensor_list



def get_combined_blocked_areas(sensor_list, y_to_check):
    areas = []
    for sensor in sensor_list:
        perpendicular_manhatten = calculate_manhatten(Coordinate(sensor.x,sensor.y),Coordinate(sensor.x,y_to_check))
        if perpendicular_manhatten > sensor.manhatten:
            continue
        diff = sensor.manhatten-perpendicular_manhatten
        areas.append([sensor.x-diff,sensor.x+diff])
        
    areas = sorted(areas, key=functools.cmp_to_key(lambda i1,i2:i1[0]-i2[0]))

    combined_areas = []
    current_area = None
    for area in areas:
        if not current_area:
            current_area = area
            continue
        if area[0] <= current_area[1]+1 and current_area[1] < area[1]:
            current_area[1]=area[1]
        elif area[0] > current_area[1]:
            combined_areas.append(current_area)
            current_area = area
    combined_areas.append(current_area)
    return combined_areas


class Sensor:
    x=0
    y=0
    closest_x=0
    closest_y=0
    manhatten=0
    def __init__(self, x, y, closest_x, closest_y) -> None:
        self.x = x
        self.y = y
        self.closest_x = closest_x
        self.closest_y = closest_y
        own = Coordinate(self.x,self.y)
        beacon=Coordinate(closest_x,closest_y)
        self.manhatten = calculate_manhatten(own,beacon)

    def beacon_not_possible(self, x,y):

        own = Coordinate(self.x,self.y)
        check=Coordinate(x,y)
        return calculate_manhatten(own,check) <= self.manhatten

class Coordinate:
    x=0
    y=0
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __eq__(self, __o: object) -> bool:
        if self.x==__o.x and self.y==__o.y:
            return True
        return False


def in_sensor_list(sensor_list, coordinate):
    for sensor in sensor_list:
        check_coord = Coordinate(sensor.x, sensor.y)
        if check_coord == coordinate:
            return True
    return False

def in_sensor_reach(sensor_list, coordinate):
    pass



def print_map(from_coordinate, to_coordinate, sensor_list, beacon_list):
    for i in range(to_coordinate.y - from_coordinate.y):
        for j in range(to_coordinate.x - from_coordinate.x):
            pass