from collections import namedtuple
from typing import List
from dataclasses import dataclass

Instruction = namedtuple('Instruction', ['direction', 'units'])


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0


TEST_STR = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
test_data = [Instruction(e.split()[0], int(e.split()[1])) for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [Instruction(e.split()[0], int(e.split()[1])) for e in f.read().splitlines()]


def follow_initial_instructions(instructions: List[Instruction]):
    position = Position()
    for instruction in instructions:
        if instruction.direction == 'up':
            position.depth -= instruction.units
        elif instruction.direction == 'down':
            position.depth += instruction.units
        elif instruction.direction == 'forward':
            position.horizontal += instruction.units
        else:
            print('Direction not recognized!', instruction)
    return position, position.depth*position.horizontal


def follow_instructions(instructions: List[Instruction]):
    position = Position()
    for instruction in instructions:
        if instruction.direction == 'up':
            position.aim -= instruction.units
        elif instruction.direction == 'down':
            position.aim += instruction.units
        elif instruction.direction == 'forward':
            position.horizontal += instruction.units
            position.depth += instruction.units*position.aim
        else:
            print('Direction not recognized!', instruction)
    return position, position.depth*position.horizontal


if __name__ == '__main__':
    print(follow_initial_instructions(test_data))
    print(follow_initial_instructions(data))

    print(follow_instructions(test_data))
    print(follow_instructions(data))