class Computer:
    registers=None
    open_instructions=[]
    subscriptions=[]
    current_completed_cycle=0
    canvas=None
    
    def __init__(self, registers, canvas) -> None:
        self.registers = registers
        self.open_instructions = []
        self.subscriptions=[]
        self.canvas=canvas

    def add_instruction(self,new_exercise):
        if new_exercise:
            new_instruction = Instruction(new_exercise.number_of_cycles, new_exercise)
            self.open_instructions.append(new_instruction)
            
    def make_cycle(self):
        if len(self.open_instructions) == 0:
            return
        current_instruction = self.open_instructions[0]
        #this is current cycle:

        if not current_instruction.started:
            current_instruction.started = True
            current_instruction.start_cycle=self.current_completed_cycle

        self.canvas.draw_pixel(self.current_completed_cycle+1, self.registers)

        #this creates state after cycle        
        if current_instruction.completes_after_cycle() == self.current_completed_cycle+1:
            if current_instruction.exercise.register:
                self.registers[current_instruction.exercise.register]=current_instruction.exercise.make_calculation(self.registers[current_instruction.exercise.register])
            del self.open_instructions[0]

        
        self.current_completed_cycle+=1

class Canvas:
    screen=[]
    width = 0
    height = 0
    def __init__(self, width, height) -> None:
        self.screen = [["."]*width for i in range(height)]
        self.width=width
        self.height=height
    
    def draw_pixel(self, cycle, register):
        register_value = register["x"]
        position = cycle-1
        row = position//40
        column = position%40
        if register_value -1 <= column and register_value+1 >= column:
            self.screen[row][column]="#"
        else:
            self.screen[row][column]="."

    def output_canvas(self):
        for row in self.screen:
            for pixel in row:
                print(pixel, end="")
            print()



class Instruction:
    start_cycle=None
    cycles_to_complete=None
    exercise=None
    started = False

    def __init__(self, cycles_to_complete, exercise) -> None:
        self.start_cycle = 0
        self.cycles_to_complete = cycles_to_complete
        self.exercise = exercise
        self.started=False
    
    def completes_after_cycle(self):
        return self.start_cycle+self.cycles_to_complete


class Exercise:
    number_of_cycles=0
    calc_value=0
    register=None
    def __init__(self, number_of_cycles) -> None:
        self.number_of_cycles = number_of_cycles
        self.calc_value=0
        self.register=None
    
    def define_calculation(self, register,value):
        self.calc_value=value
        self.register=register
    
    def make_calculation(self, current_value):
        return current_value+ self.calc_value
