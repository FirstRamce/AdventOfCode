#coordinates are always in the 4-dimensions
def calculate_manhatten(coordinates_1, coordinates_2):
    distance = 0
    distance+= abs(coordinates_1.x - coordinates_2.x)
    distance+= abs(coordinates_1.y - coordinates_2.y)
    distance+= abs(coordinates_1.z - coordinates_2.z)
    distance+= abs(coordinates_1.t - coordinates_2.t)
    return distance

def import_coordinate_file(filename):
    coordinate_list = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                return coordinate_list
            else:
                c_arr = line.split(",")
                if len(c_arr) < 4:
                    return coordinate_list
                new_coords = Coordinate(int(c_arr[0]),int(c_arr[1]),int(c_arr[2]),int(c_arr[3]),)
                coordinate_list.append(new_coords)
    
def complete_list(list_1, filler_list):
    in_first = set(list_1)
    in_second = set(filler_list)
    to_add = in_second - in_first
    result = list_1 + list(to_add)
    return result


class Coordinate:
    x=0
    y=0
    z=0
    t=0

    def __init__(self, x,y,z,t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def get_coordinates_as_list(self):
        return [self.x,self.y,self.z,self.t]
    
    def __str__(self):
        return "[{},{},{},{}]".format(self.x,self.y,self.z,self.t)


class Constellation_holder:
    constellation_list = []
    
    def add_coordinate(self, coordinate):
        constellation_found = False
        for constellation in self.constellation_list:
            fits_list = False
            for coor in constellation:
                if(calculate_manhatten(coor, coordinate) <= 3):
                    fits_list=True
            if fits_list:
                if not coordinate in constellation:
                    constellation.append(coordinate)
                constellation_found=True
        if not constellation_found:
            self.constellation_list.append([coordinate])
    
    def clear_intersections(self):
        optimization_found = False
        for ch_list in self.constellation_list:
            for compare_list in self.constellation_list:
                if not (ch_list == compare_list) and (bool(set(ch_list) & set(compare_list))):
                    i = self.constellation_list.index(ch_list)
                    new_list = complete_list(ch_list, compare_list)
                    self.constellation_list.remove(compare_list)
                    self.constellation_list[i]=new_list
                    optimization_found = True
                    break
            if optimization_found:
                break
        
        if optimization_found:
            self.clear_intersections()
        else:
            return
    


    
def compare_coordinates(item1,item2):
    number_value_1 = 0
    number_value_2 = 0
    
    
    to_zero_1 = calculate_manhatten(item1, Coordinate(0,0,0,0))
    to_zero_2 = calculate_manhatten(item2, Coordinate(0,0,0,0))
    if to_zero_1 < to_zero_2:
        return -1
    elif to_zero_1 > to_zero_2:
        return 1
    else:
        return 0
    #Maybe something like this is needed: 

    if to_zero_1 > 0:
        number_value_1 = to_zero_1
    else:
        number_value_1 = 100000 - to_zero_1
    if to_zero_2 > 0:
        number_value_2 = to_zero_2
    else:
        number_value_2 = 100000 - to_zero_2
    if number_value_1 == number_value_2:
        print("They are the same...")