from __future__ import annotations
from typing import List, NamedTuple

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


class Instruction(NamedTuple):
    operation: str
    argument: int

    def action(self):
        if self.operation == 'nop':
            return 1, 0
        elif self.operation == 'acc':
            return 1, self.argument
        elif self.operation == 'jmp':
            return self.argument, 0
        else:
            print('Operation not recognized')

    @staticmethod
    def parse_from_str(definition: str) -> Instruction:
        operation, argument = definition.split()

        return Instruction(operation, int(argument))


def compute(stack: List[Instruction]) -> int:
    position = 0
    acc = 0

    executed = set()
    repetition = False

    while position < len(stack) and not repetition:
        if position in executed:
            print(f'Repeated on {position}')
            return acc

        inst = stack[position]
        executed.add(position)

        position_increment, acc_increment = inst.action()
        print(f'Executing {inst} from {position} to {position + position_increment}')

        position += position_increment
        acc += acc_increment

    return acc


def evaluate_compute(stack: List[Instruction]) -> int:
    list_to_change = [p for p, i in enumerate(stack) if i.operation in ('nop', 'jmp')]
    original_instructions = stack.copy()

    for to_change in list_to_change:
        position = 0
        acc = 0

        executed = set()
        repetition = False

        stack = original_instructions.copy()
        inst = stack[to_change]
        if inst.operation == 'jmp':
            print(f'Changing jmp to nop on position {to_change}')
            stack[to_change] = Instruction(operation='nop', argument=inst.argument)
        elif inst.operation == 'nop':
            print(f'Changing nop to jmp on position {to_change}')
            stack[to_change] = Instruction(operation='jmp', argument=inst.argument)
        else:
            print('Error')

        while position < len(stack) and not repetition:
            if position in executed:
                print(f'Repeated on {position} after changing {to_change}, restarting it\n')
                break

            inst = stack[position]
            executed.add(position)

            position_increment, acc_increment = inst.action()

            position += position_increment
            acc += acc_increment

        if position == len(stack):
            return acc
    else:
        print('FAIL')


if __name__ == '__main__':

    instructions = [Instruction.parse_from_str(line) for line in raw_data]
    # result = compute(stack=instructions)
    # print(f'Last value of acc is {result}\n')

    result = evaluate_compute(stack=instructions)
    print(f'==> Last value of acc with change is {result}')
