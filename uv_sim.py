class UVSim:
    def __init__(self):
        self.memory = [0] * 100  # 100-word memory
        self.accumulator = 0  # This is the accumulator register
        self.instruction_counter = 0  # This is the instruction counter
        self.running = True

    def load_program(self, program):
        if len(program) > len(self.memory):
            print("Program size exceeds memory capacity")
            return False
        for index, instruction in enumerate(program):
            self.memory[index] = instruction
        print(f"Program loaded: {self.memory[:len(program)]}")
        return True

    def fetch(self):
        if self.instruction_counter >= len(self.memory):
            print("Instruction counter out of memory bounds")
            self.halt()
            return None
        instruction = self.memory[self.instruction_counter]
        print(f"Fetched instruction at {self.instruction_counter}: {instruction}")
        self.instruction_counter += 1
        return instruction

    def decode(self, instruction):
        if instruction is None:
            return None, None
        opcode = instruction // 100
        operand = instruction % 100
        print(f"Decoded instruction: opcode {opcode}, operand {operand}")
        return opcode, operand

    def execute(self, opcode, operand):
        print(f"Executing opcode {opcode} with operand {operand}")
        if opcode == 10:
            self.read(operand)
        elif opcode == 11:
            self.write(operand)
        elif opcode == 20:
            self.load(operand)
        elif opcode == 21:
            self.store(operand)
        elif opcode == 30:
            self.add(operand)
        elif opcode == 31:
            self.subtract(operand)
        elif opcode == 32:
            self.divide(operand)
        elif opcode == 33:
            self.multiply(operand)
        elif opcode == 40:
            self.branch(operand)
        elif opcode == 41:
            self.branchneg(operand)
        elif opcode == 42:
            self.branchzero(operand)
        elif opcode == 43:
            self.halt()
        else:
            print(f"Invalid opcode: {opcode}")

    # def run(self):
    #     while True:
    #         instruction = self.fetch()
    #         opcode, operand = self.decode(instruction)
    #         print(f"Fetched instruction: {instruction}")
    #         print(f"Decoded to opcode: {opcode}, operand: {operand}")
    #         self.execute(opcode, operand)
    # self.display_memory() # optional to display memory state

    def run(self):
        while self.running:
            instruction = self.fetch()
            if instruction is None:  # Properly handle None before decoding
                print("No more instructions or an error occurred.")
                break
            opcode, operand = self.decode(instruction)
            self.execute(opcode, operand)
            print(f"Memory state: {self.memory}")
            print(f"Accumulator: {self.accumulator}")
            print(f"Instruction Counter: {self.instruction_counter}")

    
    def read(self, operand):
        while True:
            value = input("Enter a 4-digit value: ")
            if value.isdigit() and len(value) == 4:
                self.memory[operand] = int(value)
                break
            else:
                print("Invalid input. Enter a 4-digit number.")

    def write(self, operand):
        print(f"Value at memory location {operand}: {self.memory[operand]}")

    def load(self, operand):
        self.accumulator = self.memory[operand]

    def store(self, operand):
        self.memory[operand] = self.accumulator

    def add(self, operand):
        print(f"Accumulator before add: {self.accumulator}")
        self.accumulator += self.memory[operand]
        print(f"Accumulator after add: {self.accumulator}")

    def subtract(self, operand):
        print(f"Accumulator before subtract: {self.accumulator}")
        self.accumulator -= self.memory[operand]
        print(f"Accumulator after subtract: {self.accumulator}")

    def divide(self, operand):
        if self.memory[operand] == 0:
            print("Cannot divide by zero")
            self.halt()
        else:
            print(f"Accumulator before divide: {self.accumulator}")
            self.accumulator //= self.memory[operand]
            print(f"Accumulator after divide: {self.accumulator}")

    def multiply(self, operand):
        print(f"Accumulator before multiply: {self.accumulator}")
        self.accumulator *= self.memory[operand]
        print(f"Accumulator after multiply: {self.accumulator}")

    def branch(self, operand):
        print(f"Branching to instruction {operand}")
        self.instruction_counter = operand

    def branchneg(self, operand):
        if self.accumulator < 0:
            print(f"Branching to {operand} because accumulator is negative")
            self.instruction_counter = operand

    def branchzero(self, operand):
        if self.accumulator == 0:
            print(f"Branching to {operand} because accumulator is zero")
            self.instruction_counter = operand

    def halt(self):
        print("Program halted.")
        # exit()
        self.running = False

    def display_memory(self):
        # Create a string representation of the memory array
        return '[' + ', '.join(str(mem) for mem in self.memory) + ']'

