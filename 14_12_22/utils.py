import re

number_regex = r'(\d+),(\d+)'


def parse_input_file(filename):
    cave = Cave()
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            previous_point = None
            matches = re.findall(number_regex,line)
            for match in matches:
                point = Vector(int(match[1]), int(match[0]))
                if previous_point:
                    cave.add_rock_row(previous_point, point)
                previous_point=point

    return cave

class Cave:
    cave_map = None
    stuck_sand = 0
    
    def __init__(self) -> None:
        self.cave_map = {}
        self.stuck_sand=0
        pass

    def add_rock_row(self, rock_from, rock_to):
        difference = rock_to.x - rock_from.x
        if difference == 0:
            difference = rock_to.y - rock_from.y
        for i in range(abs(difference)+1):
            add = i
            if difference < 0:
                add = i*-1
            if rock_to.x == rock_from.x:
                self.add_rock(rock_from.x, (rock_from.y+add))
            else:
                self.add_rock(rock_from.x+add, rock_from.y)
        return

    def add_rock(self, x, y):
        if not (x in self.cave_map):
            self.cave_map[x] = {y:"#"}
        else:
            self.cave_map[x][y] = "#"

    def add_sand(self, x, y):
        if not (x in self.cave_map):
            self.cave_map[x] = {y:"O"}
        else:
            self.cave_map[x][y] = "O"
    
    def set_ground_zero(self, ground_zero_level):
        for i in range(10000):
            self.add_rock(ground_zero_level, i)
    
    def drop_sand(self, sand_drop_point, threshhold):
        sand_point = Vector(sand_drop_point.x, sand_drop_point.y)
        runs = 0
        while True:
            if not((sand_point.x+1) in self.cave_map) or not(sand_point.y in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
            elif not(sand_point.y-1 in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
                sand_point.y = sand_point.y-1
            elif not(sand_point.y+1 in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
                sand_point.y = sand_point.y+1
            else:
                self.add_sand(sand_point.x, sand_point.y)
                self.stuck_sand+=1
                return True
            if runs < threshhold:
                runs+=1
            else:
                return False
    
    def drop_sand_with_ground(self, sand_drop_point, ground_level):
        sand_point = Vector(sand_drop_point.x, sand_drop_point.y)
        runs = 0
        while True:
            if sand_drop_point.x in self.cave_map and sand_drop_point.y in self.cave_map[sand_drop_point.x]:
                return False
            if not((sand_point.x+1) in self.cave_map) or not(sand_point.y in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
            elif not(sand_point.y-1 in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
                sand_point.y = sand_point.y-1
            elif not(sand_point.y+1 in self.cave_map[sand_point.x+1]):
                sand_point.x=sand_point.x+1
                sand_point.y = sand_point.y+1
            else:
                self.add_sand(sand_point.x, sand_point.y)
                self.stuck_sand+=1
                return True
            
            
    
class Vector:
    x: 0
    y: 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        pass