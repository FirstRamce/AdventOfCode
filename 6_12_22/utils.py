

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
    