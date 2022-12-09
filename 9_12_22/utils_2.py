from enum import Enum

def parse_input_file(filename, number_of_nots, knot_to_record):
    knot_list = []
    for i in range(number_of_nots):
        knot_list.append(Position_Vector(0,0))
    pos_handler = Position_Handler(Position_Vector(0,0), knot_list, knot_to_record)
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            split_line = line.split(" ")
            dir = Direction.get_direction(split_line[0])
            moves = int(split_line[1])
            for i in range(moves):
                pos_handler.add_head_move(dir)
                pos_handler.update_knot_list()
    return pos_handler
            
class Direction(Enum):
    Right = [1,0]
    Left = [-1,0]
    Up = [0,1]
    Down = [0,-1]

    @staticmethod
    def get_direction(symbol):
        if symbol == "R":
            return Direction.Right
        elif symbol == "L":
            return Direction.Left
        elif symbol == "U":
            return Direction.Up
        elif symbol == "D":
            return Direction.Down


class Position_Handler:
    current_head=None
    current_knots_list=[]
    knot_to_record=0
    knot_position_record=[]
    def __init__(self, head, knots_list, knot_to_record) -> None:
        self.current_head=head
        self.current_knots_list = knots_list
        self.knot_to_record = knot_to_record
        self.knot_position_record=[knots_list[knot_to_record]]
    
    def add_head_move(self, direction):
        
        x = direction.value[0]
        y = direction.value[1]
        self.current_head = Position_Vector(self.current_head.x+x, self.current_head.y+y)
        #print("update head: "+ str(self.current_head.x)+" : "+ str(self.current_head.y))
        #print("tail moves from (diagonal) : "+ str(self.current_tail.x)+" : "+ str(self.current_tail.y) + " to: " + str(new_tail.x)+" : "+ str(new_tail.y))
    
    def update_knot_list(self):
        for i in range(len(self.current_knots_list)):
            self.update_knot_move(i)

    def update_knot_move(self, knot_to_update):
        
        follow_knot = self.current_head
        update_knot = self.current_knots_list[knot_to_update]
        if knot_to_update > 0:
            follow_knot = self.current_knots_list[knot_to_update-1]
        #print("update knot position : "+ str(update_knot.x)+" : "+ str(update_knot.y))
        diff_vector = self.current_knots_list[knot_to_update].diff_vector(follow_knot)
        move_vector = Position_Vector(diff_vector.x, diff_vector.y)
        if(abs(diff_vector.x) <= 1 and abs(diff_vector.y) <= 1):
            return
        else:
            if diff_vector.x == 0 or diff_vector.y == 0:
                new_update_knot = Position_Vector(update_knot.x + int(diff_vector.x/2), update_knot.y + int(diff_vector.y/2))
                self.current_knots_list[knot_to_update] = new_update_knot
                
            else:
                if abs(diff_vector.x) > 1:
                    move_vector.x = int(diff_vector.x/2)
                if abs(diff_vector.y) > 1:
                    move_vector.y = int(diff_vector.y/2)
                
                new_update_knot = Position_Vector(update_knot.x + (move_vector.x), update_knot.y + (move_vector.y))
                self.current_knots_list[knot_to_update] = new_update_knot
            
        if self.knot_to_record == knot_to_update:
            self.knot_position_record.append(self.current_knots_list[knot_to_update])


class Position_Vector:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def diff_vector(self, other_position):
        return(Position_Vector(other_position.x- self.x, other_position.y - self.y))
        
    
def contains_vector(list, vector):
    for item in list:
        if item.x == vector.x and item.y == vector.y:
            return True
    return False