class CodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.instructions = []

    def gen_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def gen_label(self):
        self.label_count += 1
        return f"L{self.label_count}"
    
    def emit(self, instruction):
        self.instructions.append(instruction)
        
    def print_instructions(self):
        print("\nCódigo de Três Endereços Gerado:")
        for idx, instr in enumerate(self.instructions, 1):
            print(f"{idx}: {instr}")
