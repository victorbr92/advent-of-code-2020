from typing import Dict

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


test_data = '''123 -> x
x AND y -> d
456 -> y
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''.splitlines()

TO_REPLACE = {
    'AND': '&',
    'OR': '|',
    'NOT': '~',
    'LSHIFT': '<<',
    'RSHIFT': '>>'
}


def parse(instruction_line: str):
    elements = instruction_line.split(' -> ')

    for case in TO_REPLACE:
        elements[0] = elements[0].replace(case, TO_REPLACE[case])

    return elements[1], elements[0].split()


def apply_operation(wire: str, existing_wires: Dict, all_instructions: Dict):
    final_operation = ''
    operations = all_instructions[wire]

    for element in operations:
        if element in TO_REPLACE.values() or element.isdigit():
            final_operation += element
        elif element in existing_wires:
            final_operation += str(existing_wires[element])
        else:
            op = apply_operation(wire=element, existing_wires=wires, all_instructions=instructions)
            existing_wires[element] = op
            final_operation += str(op)

    return eval(final_operation)


if __name__ == '__main__':
    instructions = {}
    wires = {}
    letter = 'a'

    for line in raw_data:
        variable, operation = parse(instruction_line=line)
        instructions[variable] = operation

    wires[letter] = apply_operation(wire=letter, existing_wires=wires, all_instructions=instructions)
    if wires[letter] < 0:
        print(65536 + wires[letter])
    else:
        print(wires[letter])

    wires = {}
    instructions['b'] = ['3176']
    wires[letter] = apply_operation(wire=letter, existing_wires=wires, all_instructions=instructions)
    if wires[letter] < 0:
        print(65536 + wires[letter])
    else:
        print(wires[letter])
