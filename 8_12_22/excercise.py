from utils import *
forest = parse_input_file("input.txt")
visible_trees = 0
for i in range(len(forest.tree_map)):
    for j in range(len(forest.tree_map[0])):
        if forest.is_tree_visible(i,j):
            visible_trees+=1

print("visible trees(EX1): " + str(visible_trees))
highest_score = 0
for i in range(len(forest.tree_map)):
    for j in range(len(forest.tree_map[0])):
        score = forest.get_tree_scenic_score(i,j)
        if score > highest_score:
            highest_score = score
        
print("highest score(EX2): " + str(highest_score))
#1: 1690
#2: 535680