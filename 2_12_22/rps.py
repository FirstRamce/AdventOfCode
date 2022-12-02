import re
from enum import Enum

def parse_file_win_indication(filename):
    round_list = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            m = re.search(r'([ABC]) ([YXZ])', line)
            p1 = Move.get_move(m.group(1))
            p2 = Move.get_corresponding_move(p1, m.group(2))
            round_list.append(Round(p1,p2))
    return round_list

def parse_file_move_indication(filename):
    round_list = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            m = re.search(r'([ABC]) ([YXZ])', line)
            p1 = Move.get_move(m.group(1))
            p2 = Move.get_move(m.group(2))
            round_list.append(Round(p1,p2))
    return round_list

class Move(Enum):
    Invalid=0
    Rock = 1
    Paper = 2
    Scissor = 3

    @staticmethod
    def get_move(symbol):
        if symbol == "A" or symbol == "X":
            return Move.Rock
        elif symbol == "B" or symbol == "Y":
            return Move.Paper
        elif symbol == "C" or symbol == "Z":
            return Move.Scissor
        else:
            return Move.Invalid

    @staticmethod
    def get_move_by_value(value):
        if value == 1:
            return Move.Rock
        elif value == 2:
            return Move.Paper
        elif value == 3:
            return Move.Scissor

    @staticmethod
    def get_corresponding_move(p1, symbol):
        if symbol == "Y":
            return p1
        elif symbol == "X":
            if (p1.value - 1) > 0:
                return Move.get_move_by_value(p1.value - 1)
            else:
                return Move.get_move_by_value(3)
        elif symbol == "Z":
            if (p1.value + 1) <= 3:
                return Move.get_move_by_value(p1.value + 1)
            else:
                return Move.get_move_by_value(1)

    
    

class Round:
    player1 = None
    player2 = None

    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
    
    def calc_points(self, player):
        me = self.player1
        opponent = self.player2
        if(player == 2):
            me=self.player2
            opponent=self.player1
        result_points = 0
        if (me.value - opponent.value) == 1 or (me.value - opponent.value) == -2:
            result_points = 6
        elif (me.value-opponent.value) == 0:
            result_points = 3
        return result_points + me.value

    def __str__(self):
        return "<"+str(self.player1)+"/"+str(self.player2)+">"

    
