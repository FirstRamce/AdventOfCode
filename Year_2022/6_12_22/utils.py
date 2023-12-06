

def parse_input(filename):
    with open(filename) as f:
        input = f.readlines()
        if len(input) > 0:
            return input[0]

def get_first_x_different(different_length, input):
    for i in range(len(input)):
        if i <= len(input)-different_length:
            characters = set([])
            for c in range(different_length):
                characters.add(input[i+c])
            if len(characters) == different_length:
                return i

def alternative(different_length, input):
    check_range = []
    for i in range(len(input)):
        check_range.append(input[i])
        if(len(check_range) > different_length):
            check_range.remove(check_range[0])
        if len(set(check_range))==different_length:
            return i-(different_length-1)
    