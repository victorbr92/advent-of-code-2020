from typing import List
import numpy as np

TEST_STR = "16,1,2,0,4,2,7,1,2,14"

test_data = [int(e) for e in TEST_STR.split(',')]

with open('input.txt', 'r') as f:
    data = [int(e) for e in f.read().split(',')]


def calculate_fuel(crabs_position: np.ndarray, aligned_position: int):
    return sum(abs(crabs_position - aligned_position))


def calculate_new_fuel(crabs_position: np.ndarray, aligned_position: int):
    """
    We will basically use the triangular number formula.
    """
    diff = abs(crabs_position - aligned_position)
    ind_consumption = (diff * (diff + 1)) // 2
    return sum(ind_consumption)


def brute_force(crabs: List[int], comp: bool = False):
    """
    We can basically frame as an optimization problem. We should minimize the fuel given a position X.
    Let's brute force it for now to be faster, but then we can use more smart techniques to do it faster if
    it does not work.
    """
    min_position, max_position = min(crabs), max(crabs)
    crabs_position = np.array(crabs)

    min_loss = (0, 1E10)
    for p in range(min_position, max_position + 1):
        if comp:
            loss = calculate_new_fuel(crabs_position, p)
        else:
            loss = calculate_fuel(crabs_position, p)
        if loss < min_loss[1]:
            min_loss = (p, loss)
        # print(f'~~Position {p}~~ {loss}')
    return min_loss


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    print(brute_force(test_data))
    print('> input')
    print(brute_force(data))

    print('===== PART2 ======')
    print('> test input')
    print(brute_force(test_data, comp=True))
    print('> input')
    print(brute_force(data, comp=True))
