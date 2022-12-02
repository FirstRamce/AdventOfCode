from rps import *

print("First excercise: ")
round_list = parse_file_move_indication("input")
score = 0
for round in round_list:
    score += round.calc_points(2)
print(score)

print("Second excercise: ")
round_list = parse_file_win_indication("input")
score = 0
for round in round_list:
    score += round.calc_points(2)
print(score)