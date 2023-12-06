import re

regex  = r'[\[\]]|\d+'

def parse_input_file(filename):
    pair_list = []
    with open(filename) as f:
        first_container = None
        second_container = None
        current_container=None
        while True:
            line = f.readline()
            if not line:
                pair_list.append(Pair(first_container, second_container))
                break
            if line == "\n":
                pair_list.append(Pair(first_container, second_container))
                first_container = None
                second_container = None

            current_container=None
            matches = re.findall(regex,line)
            for match in matches:
                if match == "[":
                    current_container = Container(current_container)
                elif re.search(r'\d', match):
                    current_container.add_value(int(match))
                elif match == "]":
                    add_container = current_container
                    if current_container.parent:
                        current_container = add_container.parent
                        current_container.add_value(add_container)
                    else:
                        #print("root container: " + str(current_container))
                        lsdjkflksdjf=1
                    continue
            if first_container:
                second_container = current_container
            else:
                first_container = current_container
    return pair_list


class Container:
    container = None
    parent = None
    def __init__(self, parent_container) -> None:
        self.container = []
        self.parent = parent_container
        
    def add_value(self, value):
        self.container.append(value)

    def __str__(self) -> str:
        return str(self.container)

    def get_string(self):
        return_string = "["
        item_number = 0
        for item in self.container:
            if item_number > 0:
                return_string+=","
            if type(item) == int:
                return_string+=str(item)
            else:
                return_string+=item.get_string()
            item_number+=1
        return return_string+"]"

        
    
def compare_two_containers(first_container, second_container):
    i=0
    for item in first_container.container:
        current_second_value = None
        if len(second_container.container) <= i:
            #print("here 1")
            return -1
        else:
            current_second_value = second_container.container[i]
        i+=1
        if type(item) == int and type(current_second_value) == int:
            if current_second_value == item:
                continue
            elif current_second_value > item:
                #print("here 4")
                return 1
            else:
                #print("here 2 : numbers: " + str(item) + " : " + str(current_second_value))
                return -1
        else:
            container_one = item
            container_two = current_second_value
            if type(item) == int:
                container_one = Container(None)
                container_one.add_value(item)
            if type(current_second_value) == int:
                container_two = Container(None)
                container_two.add_value(current_second_value)
            cmp = compare_two_containers(container_one, container_two)
            if cmp != 0:
                return cmp    
                
        
    if len(first_container.container) < len(second_container.container):
        #print("here 5 : " + str(first_container.get_string() + " : " + str(second_container.get_string())))
        return 1
    elif len(first_container.container) > len(second_container.container):
        #print("here 6")
        return -1
    return 0



class Pair:
    first_container = None
    second_container = None
    def __init__(self, first_container, second_container) -> None:
        self.first_container = first_container
        self.second_container = second_container

    def compare_containers(self):
        #print("compare: |" + str(self.first_container.container) + "| to: |" + str(self.first_container.container))
        return compare_two_containers(self.first_container, self.second_container)
        #returns 1 if container 2 is "bigger" then 1 (correct order) -1 if it is opposit, and 0 if they are the same
        
