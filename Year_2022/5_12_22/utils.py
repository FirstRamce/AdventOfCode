import re
container_regex = r'[\s\[A-Z\]]{3}\s{0,1}'
number_regex = r'\d'
move_regex = r'move (\d+) from (\d) to (\d)'

def parse_input_line(line, container_status, crane_9001):
    containers = re.findall(container_regex,line)
    move_match = re.search(move_regex, line)
    if(len(containers) > 0):
        #print("containers_to_add: " + str(containers))
        container_nr = 1
        for container in containers:
            if "[" in container:
                container_status.add_container(container_nr, container[1])
            container_nr+=1
        #print("Containers: "+str(container_status.container_stacks))
    if move_match:
        
        if(not crane_9001):
            container_status.move_container(int(move_match.group(1)), int(move_match.group(2)), int(move_match.group(3)))
        else:
            #print("move_found. Before: " + str(container_status.container_stacks))
            container_status.move_container_9001(int(move_match.group(1)), int(move_match.group(2)), int(move_match.group(3)))
            #print("move_found. After: " + str(container_status.container_stacks))
    return container_status


def parse_container_input(filename):
    container_status = Container_status()
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            container_status = parse_input_line(line, container_status, False)
    return container_status
            
def parse_container_input_9001(filename):
    container_status_2 = Container_status()
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            container_status_2 = parse_input_line(line, container_status_2, True)
    return container_status_2

class Container_status:
    container_stacks = []
    def __init__(self):
        self.container_stacks = []
    def add_container(self, stack_nr, symbol):
        if(len(self.container_stacks) < (stack_nr)):
            while(len(self.container_stacks) < (stack_nr-1)):
                self.container_stacks.append([])
            self.container_stacks.append([symbol])
        else:
            self.container_stacks[stack_nr-1].insert(0,symbol)
    
    def move_container(self, amount, from_stack, to_stack):
        for i in range(amount):
            if(len(self.container_stacks[from_stack-1])>0):
                crate = self.container_stacks[from_stack-1].pop()
                self.container_stacks[to_stack-1].append(crate)
    
    def move_container_9001(self, amount, from_stack, to_stack):
        to_stack_length = len(self.container_stacks[to_stack-1])
        for i in range(amount):
            if(len(self.container_stacks[from_stack-1])>0):
                crate = self.container_stacks[from_stack-1].pop()
                self.container_stacks[to_stack-1].insert(to_stack_length, crate)
                