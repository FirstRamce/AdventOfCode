from utils import *
work_pairs = parse_input("input.txt")
obsolete_elves = 0
print("Excercise 1: ")
for pair in work_pairs:
    if pair.one_in_the_other():
        obsolete_elves+= 1
print(obsolete_elves)

partly_obsolete = 0
print("Excercise 2: ")
for pair in work_pairs:
    if pair.is_overlapping_worker_pair():
        partly_obsolete+= 1
print(partly_obsolete)