

def parse_container_input(filename):
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            