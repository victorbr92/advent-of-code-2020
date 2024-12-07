from typing import List
from itertools import chain, product
from tqdm import tqdm


PART1_ELEMENTS = '+*'
PART2_ELEMENTS = '+*|'

def read():
    with open("input.txt") as f:
        inp = f.read().splitlines()
        equations = []
        for i in inp:
            left, right = i.split(':')
            e = ((int(left), [i for i in right.split()]))
            equations.append(e)

        return equations

def evaluate_equation(left: int, right: List[str], elements: str) -> bool:
    # I will keep a queue of values and I will evaluate
    # If the value is larger
    # running_total = right.pop(0)

    # while right:
    #     element = right.pop(0)
    #     running_total
    possible_operators = product(elements, repeat=len(right)-1)
    for operators in possible_operators:
        total = int(right[0])
        for i, element in enumerate(right[1:]):
            if operators[i] == '+':
                total += int(element)
            elif operators[i] == '*':
                total *= int(element)
            elif operators[i] == '|':
                total = int(str(total) + element)
            else:
                raise ValueError(f'Error with operator {operators[i]}')

            if total > left:
                break
        if total == left:
            return True

    return False

if __name__ == "__main__":
    equations = read()

    part1 = 0
    part2 = 0
    for equation in equations:
        left, right = equation
        correct = evaluate_equation(left, right, PART1_ELEMENTS)
        if correct:
            part1 += left
    print(f"Result of part1: {part1}")
    print("---------------------------")
    for equation in tqdm(equations):
        left, right = equation
        correct = evaluate_equation(left, right, PART2_ELEMENTS)
        if correct:
            part2 += left
    print(f"Result of part1: {part2}")
