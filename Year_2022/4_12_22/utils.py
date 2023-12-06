import re
fetch_number_regex = r'(\d+)-(\d+),(\d+)-(\d+)'

def parse_input(filename):
    work_pairs = []
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break

            match = re.search(fetch_number_regex, line)
            #print("line with match found")
            if match:
                #print("line with match found")
                work_pairs.append(Work_Pair(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
    return work_pairs

class Work_Pair:
    first_range=[]
    def __init__(self, from_1, to_1, from_2, to_2) -> None:
        #print("create pair with: " + str(from_1)+str(to_1)+str(from_2)+str(to_2))
        self.first_range = [from_1, to_1]
        self.second_range = [from_2, to_2]
    
    def one_in_the_other(self):
        if self.first_range[0] <= self.second_range[0] and self.first_range[1] >= self.second_range[1]:
            return True
        elif self.first_range[0] >= self.second_range[0] and self.first_range[1] <= self.second_range[1]:
            return True
        return False
    
    def is_overlapping_worker_pair(self):
        if (self.first_range[0] <= self.second_range[0] and self.first_range[1] >= self.second_range[0]) or (self.first_range[0] <= self.second_range[1] and self.first_range[1] >= self.second_range[1]):
            return True
        elif (self.second_range[0] <= self.first_range[0] and self.second_range[1] >= self.first_range[0]) or (self.second_range[0] <= self.first_range[1] and self.second_range[1] >= self.first_range[1]):
            return True
        return False