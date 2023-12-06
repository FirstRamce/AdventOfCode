def parse_input(filename):
    handler = Bagpack_Handler()
    bagpacks = []
    groups = []
    active_group = Group()
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            bagpack = Bagpack(line)
            bagpacks.append(bagpack)
            if not active_group.add_bagpack(bagpack):
                groups.append(active_group)
                active_group = Group()
                active_group.add_bagpack(bagpack)
    groups.append(active_group)
    handler.bagpacks = bagpacks
    handler.groups = groups
    return handler

def calculate_duplicate_priority(bagpack_list):
    value = 0
    for b in bagpack_list:
        value += get_symbol_priority_value(b.get_duplicate())
    return value

def get_symbol_priority_value(symbol):
    item_ord = ord(symbol)
    if item_ord >= 95:
        return item_ord - 96
    else:
        return item_ord - 38
        
class Bagpack:
    first_half = []
    second_half = []
    def __init__(self, items):
        self.first_half = []
        self.second_half = []
        half = int(len(items) / 2)
        for i in range(half):
            self.first_half.append(items[i])
            self.second_half.append(items[i+half])
    
    def get_duplicate(self):
        intersection = list(set(self.first_half) & set(self.second_half))
        if(len(intersection) > 1):
            print("SOMETHIGN WENT VERY WRONG")
            return None
        else:
            return intersection[0]
    
    def __str__(self) -> str:
        return str(self.first_half) + " - " + str(self.second_half)
    
class Group:
    elves_bagpacks = []
    def __init__(self) -> None:
        self.elves_bagpacks = []

    def add_bagpack(self, bagpack):
        if len(self.elves_bagpacks) < 3:
            self.elves_bagpacks.append(bagpack)
            return True
        else:
            return False

    def get_group_symbol(self):
        cross_section = set([])
        for elve in self.elves_bagpacks:
            if len(cross_section) == 0:
                cross_section = set(elve.first_half + elve.second_half)
            else:
                cross_section = cross_section & set(elve.first_half + elve.second_half)
        if len(cross_section) == 1:
            return cross_section.pop()
        else:
            raise Exception("Well that didn't work out as expected") 
        

class Bagpack_Handler:
    bagpacks = []
    groups = []
    def __init__(self) -> None:
        self.bagpacks = []
        self.groups = []

    def calculate_groups_symbol_priority(self):
        value = 0
        for group in self.groups:
            value += get_symbol_priority_value(group.get_group_symbol())
        return value