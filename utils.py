import random

def generate_instruction():
    
    return ''.join(str(random.randint(0, 1)) for _ in range(6))

def generate_program(file_name, num_instructions):
    
    with open(file_name, 'w') as file:
        for _ in range(num_instructions):
            instruction = generate_instruction()
            file.write(instruction + '\n')

def ula(instruction, a, b):
    a_bits = list(bin(a)[2:].zfill(32))
    b_bits = list(bin(b)[2:].zfill(32))
    
    inva, ena, enb, f0, f1, inc = [int(x) for x in instruction]
    
    carry = 0  # Inicializa carry com 0
    
    if inva:
        a_bits = ['1' if bit == '0' else '0' for bit in a_bits]
    if ena == 0:
        a_bits = ['0'] * 32
    if enb == 0:
        b_bits = ['0'] * 32
    
    if f0 == 0 and f1 == 0:
        result = ['0'] * 32
    elif f0 == 0 and f1 == 1:
        result = ['1'] * 32
    elif f0 == 1 and f1 == 0:
        result = ['1' if a_bits[i] == '1' or b_bits[i] == '1' else '0' for i in range(32)]
    elif f0 == 1 and f1 == 1:
        result = ['1' if a_bits[i] == '1' and b_bits[i] == '1' else '0' for i in range(32)]
    
    if inc:
        carry = 1
        for i in range(31, -1, -1):
            if result[i] == '1' and carry == 1:
                result[i] = '0'
            elif result[i] == '0' and carry == 1:
                result[i] = '1'
                carry = 0
    
    return ''.join(result), carry


def execute_program(program_file, input_a, input_b):
    with open(program_file, 'r') as file:
        program = file.readlines()
    
    a = input_a
    b = input_b
    pc = 0
    log = []
    
    for instruction in program:
        instruction = instruction.strip()
        s, carry = ula(instruction, a, b)
        
        log.append(f'IR: {instruction}, PC: {pc}, A: {a}, B: {b}, S: {s}, Carry: {carry}')
        
        a = int(s, 2)
        pc += 1
    
    with open('log.txt', 'w') as logfile:
        for line in log:
            logfile.write(line + '\n')

