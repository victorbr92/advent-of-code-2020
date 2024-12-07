from typing import List
from tqdm import tqdm


PART1_ELEMENTS = '+*'
PART2_ELEMENTS = '+*|'

def read():
    with open("input.txt") as f:
        inp = f.read().splitlines()
        equations = []
        for i in inp:
            left, right = i.split(':')
            e = (int(left), [int(i) for i in right.split()])
            equations.append(e)

        return equations

def evaluate_equation(left: int, right: List[int], elements: str, current_total: int = 0, depth: int = 0) -> bool:
    if depth == len(right) - 1:
        return current_total == left

    for operator in elements:
        next_total = current_total
        next_value = int(right[depth + 1])

        if operator == '+':
            next_total += next_value
        elif operator == '*':
            next_total *= next_value
        elif operator == '|':
            next_total = int(str(next_total) + str(next_value))
        else:
            raise ValueError(f'Unknown operator {operator}')

        if next_total > left:
            continue

        if evaluate_equation(left, right, elements, next_total, depth + 1):
            return True

    return False

if __name__ == "__main__":
    equations = read()

    part1 = 0
    part2 = 0
    for equation in equations:
        left, right = equation
        correct = evaluate_equation(
            left=left,
            right=right,
            elements=PART1_ELEMENTS,
            current_total=right[0],
            depth=0
        )
        if correct:
            part1 += left
    print(f"Result of part1: {part1}")
    print("---------------------------")
    for equation in tqdm(equations):
        left, right = equation
        correct = evaluate_equation(
            left=left,
            right=right,
            elements=PART2_ELEMENTS,
            current_total=right[0],
            depth=0
        )
        if correct:
            part2 += left
    print(f"Result of part2: {part2}")
