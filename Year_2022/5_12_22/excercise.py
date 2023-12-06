from utils import *

print("Ex 1:")
container_status = parse_container_input("input.txt")
print(container_status.container_stacks)
for stack in container_status.container_stacks:
    if len(stack) > 0:
        print(stack[len(stack)-1])
    else:
        print(" ")
print("Ex 2:")

container_status = parse_container_input_9001("input.txt")
print(container_status.container_stacks)
for stack in container_status.container_stacks:
    if len(stack) > 0:
        print(stack[len(stack)-1])
    else:
        print(" ")