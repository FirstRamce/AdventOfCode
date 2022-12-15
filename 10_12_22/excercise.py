from utils import * 
import re
number_regex =r'add(\w) (-{0,1}\d+)'
new_exercise=None
computer = Computer({"x":1}, Canvas(width=40, height=6))
with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            match = re.search(number_regex,line)
            if match:
                new_exercise = Exercise(2)
                new_exercise.define_calculation(match.group(1),int(match.group(2)))
                pass
            elif "noop" in line:
                new_exercise = Exercise(1)
                pass
            else:
                continue
            computer.add_instruction(new_exercise)

signal_sum = 0
while len(computer.open_instructions) > 0:
    computer.make_cycle()
    completed_cycle = computer.current_completed_cycle
    #print("current completed cycle: " + str(computer.current_completed_cycle) + " registers: " + str(computer.registers))
    if (completed_cycle+1 -20) % 40 == 0:
        signal_sum+=(completed_cycle+1)*computer.registers["x"]
        print("signal Strength: " + str((completed_cycle+1)*computer.registers["x"]))
print("Signal Sum: " + str(signal_sum))

print("canvas:")
computer.canvas.output_canvas()