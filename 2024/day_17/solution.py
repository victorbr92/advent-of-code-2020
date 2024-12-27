from rich import print
from math import trunc

def find_combo(registers, operand):
    if 0 <= operand <= 3:
        return operand
    else:
        return registers[operand - 4]

def bxl(registers, operand):
    t = registers[1] ^ operand
    registers[1] = t
    return None

def bst(registers, operand):
    t = find_combo(registers, operand) % 8
    registers[1] = t
    return None

def jnz(registers, operand):
    if registers[0] == 0:
        return None
    else:
        return operand

def bxc(registers, operand):
    t =  registers[1] ^ registers[2]
    registers[1] = t
    return None

def out(registers, operand, output):
    temp = find_combo(registers, operand) % 8
    output.append(temp)
    # return None

def t_div(registers, operand):
    numerator = registers[0]
    denominator = 2 ** find_combo(registers, operand)
    return trunc(numerator/denominator)

def adv(registers, operand):
    registers[0] = t_div(registers, operand)
    return None

def bdv(registers, operand):
    registers[1] = t_div(registers, operand)
    return None

def cdv(registers, operand):
    registers[2] = t_div(registers, operand)
    return None

def read_input():
    with open("input.txt") as f:
        text = f.read().split('\n\n')

        registers = []
        for register in text[0].splitlines():
            registers.append(int(register.split(": ")[-1]))

        instructions = []
        for i in text[1].strip("Program: ").split(','):
            instructions.append(int(i))

        return registers, instructions

def exe(instruction, operand, registers, output):
    INST = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }
    func = INST[instruction]
    if instruction == 5:
        r = func(registers, operand, output)
    else:
        r = func(registers, operand)
    return r

def run_program(registers, program):
    ins_pointer = 0
    output = []
    while ins_pointer < len(program):
        instruction = program[ins_pointer]
        operand = program[ins_pointer + 1]
        r = exe(instruction, operand, registers, output)
        if instruction == 3 and r is not None:
            ins_pointer = r
        else:
            ins_pointer += 2
    so = (','.join(str(o) for o in output))
    return so


def find_a(program, ans):
    print(program, ans)
    if program == []:
        return ans

    for t in range(8):
        a = ans << 3 | t
        b = a % 8 # 2,4
        b = b ^ 5 # 1,5
        c = a >> b # 7,5
        b = b ^ 6 # 1,6
        b = b ^ c # 4,2
        output = b % 8 # 5,5

        if output == program[-1]:
            sub = find_a(program[:-1], a)
            if sub is not None:
                return sub

if __name__ == "__main__":

    og_registers, program = read_input()
    output = run_program(og_registers, program)
    print(f"Result of part1: {output}")
    print("-"*20)

    find_a(program, 0)
