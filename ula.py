from utils import execute_program, generate_program

def main():
    program_file = 'program.txt'
    num_instructions = 10  
    generate_program(program_file, num_instructions)

    input_a = 10
    input_b = 20
    execute_program(program_file, input_a, input_b)

if __name__ == "__main__":
    main()
