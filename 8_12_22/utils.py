import re


def parse_input_file(filename):
    forest = Forest()
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            forest.add_tree_row(line)
    return forest

def get_number_of_trees_visible(map, row, col, direction):
    seen_trees = 0
    tree_height = map[row][col]
    multiplier = 1
    while True:
        check_row = row +(direction.row_direction * multiplier)
        check_col = col + (direction.col_direction * multiplier)
        if len(map) <= check_row or check_row < 0 or len(map[check_row]) <= check_col or check_col < 0:
            return seen_trees
        if map[check_row][check_col] >=tree_height:
            seen_trees+=1
            return seen_trees
        else:
            seen_trees+=1
            multiplier+=1
        

            

class Direction:
    row_direction = 0
    col_direction = 0
    def __init__(self, row_dir, col_dir):
        self.row_direction=row_dir
        self.col_direction=col_dir

class Forest:
    tree_map = []
    def __init__(self):
        self.tree_map = []
    
    def add_tree_row(self,tree_row):
        split_row = re.findall(r"\d",tree_row)
        tree_row = list(map(int, split_row))
        self.tree_map.insert(0,tree_row)
    
    def is_tree_visible(self, row,col):
        tree_height = self.tree_map[row][col]
        row
        can_be_seen = True
        for i in range(len(self.tree_map)):
            if i == row and can_be_seen:
                return True
            elif i == row:
                can_be_seen = True
            elif not can_be_seen: 
                continue
            elif self.tree_map[i][col]>=tree_height:
                can_be_seen= False
        if can_be_seen:
            return can_be_seen

        can_be_seen = True
        for i in range(len(self.tree_map[row])):
            if i == col and can_be_seen:
                return True
            elif i == col:
                can_be_seen = True
            elif not can_be_seen: 
                continue
            elif self.tree_map[row][i]>=tree_height:
                can_be_seen= False
        
        return can_be_seen

    def get_tree_scenic_score(self, row, col):
        up = Direction(-1,0)
        down = Direction(1,0)
        left = Direction(0,-1)
        right = Direction(0,1)
        return get_number_of_trees_visible(self.tree_map,row,col,up) *get_number_of_trees_visible(self.tree_map,row,col,down)*get_number_of_trees_visible(self.tree_map,row,col,left)*get_number_of_trees_visible(self.tree_map,row,col,right)