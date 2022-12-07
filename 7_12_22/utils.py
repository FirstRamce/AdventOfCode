


def parse_command_input(filename):
    with open(filename) as f:
        root_dir = None
        current_dir = None
        while True:
            line = f.readline().strip()
            if not line:
                break
            splitted_input = line.split(" ")
            if line.startswith("$ cd /"):
                current_dir = File_System_Item(None, 0, "/")
                root_dir = current_dir
            elif len(splitted_input) == 2 and splitted_input[0].isnumeric():
                current_dir.add_child_item(File_System_Item(current_dir, int(splitted_input[0]),splitted_input[1]))
            elif len(splitted_input) == 3 and splitted_input[1]=="cd":
                if splitted_input[2] == "..":
                    if current_dir.parent_dir == None:
                        print("dir parent was none, current dir: " + current_dir.name)
                    current_dir = current_dir.parent_dir
                    
                else:
                    if current_dir == None:
                        print("line to read: " + line)
                    new_current_dir = File_System_Item(current_dir, 0, splitted_input[2])
                    current_dir.add_child_item(new_current_dir)
                    current_dir = new_current_dir
        return root_dir

def get_folder_list_sub_size(current_folder, max_size):
    result_folders = []
    if current_folder.calculate_item_size() <= max_size:
        result_folders.append(current_folder)
    for item in current_folder.child_items:
        if item.is_dir():
            result_folders+=get_folder_list_sub_size(item, max_size)
    return result_folders

def get_folder_list_above_size(current_folder, min_size):
    result_folders = []
    if current_folder.calculate_item_size() >= min_size:
        result_folders.append(current_folder)
    for item in current_folder.child_items:
        if item.is_dir():
            result_folders+=get_folder_list_above_size(item, min_size)
    return result_folders


class File_System_Item:
    parent_dir = None
    child_items = []
    file_size = None
    name = None

    def __init__(self, parent_dir, file_size, name):
        self.parent_dir = parent_dir
        self.file_size = file_size
        self.name = name
        self.child_items = []

    def add_child_item(self, child_item):
        self.child_items.append(child_item)
    
    def is_dir(self):
        return self.file_size <= 0
    
    def print_file_tree(self, prefix):
        print(prefix + self.name)
        if len(self.child_items) > 0:
            for item in self.child_items:
                item.print_file_tree(prefix+"\t")

    def calculate_item_size(self):
        if self.is_dir():
            size = 0
            for child in self.child_items:
                size += child.calculate_item_size()
            return size
        else:
            return self.file_size