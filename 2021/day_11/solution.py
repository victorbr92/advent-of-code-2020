from typing import List, Tuple, Dict
import numpy as np

TEST_STR = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

TEST_STR2 = """11111
19991
19191
19991
11111"""

COORDS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1)
]

test_data = [[int(i) for i in e] for e in TEST_STR.splitlines()]
test_data_2 = [[int(i) for i in e] for e in TEST_STR2.splitlines()]

with open('input.txt', 'r') as f:
    data = [[int(i) for i in e] for e in f.read().splitlines()]


def pass_step(grid: np.ndarray):
    max_x, max_y = grid.shape

    flashed = []
    grid = grid + 1
    bigger_than_9 = np.argwhere(grid > 9)
    while len(bigger_than_9):
        flashed += bigger_than_9.tolist()
        grid[grid > 9] = 0
        for flash in bigger_than_9:
            for coord in COORDS:
                adjacent = [flash[0] + coord[0], flash[1] + coord[1]]
                if (0 <= adjacent[0] < max_x) and (0 <= adjacent[1] < max_y) \
                        and adjacent not in flashed:
                    grid[adjacent[0]][adjacent[1]] += 1
        bigger_than_9 = np.argwhere(grid > 9)

    return grid, len({(i[0], i[1]) for i in flashed})


def run_steps(initial_grid: List[List[int]], steps: int = 100, stop=False):
    grid = np.array(initial_grid)
    flashed = 0
    for i in range(steps):
        grid, flashes = pass_step(grid)
        if flashes == grid.size and stop:
            return i+1
        flashed += flashes
    return flashed


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    # run_steps(initial_grid=test_data_2, steps=4)
    print(run_steps(initial_grid=test_data, steps=100))
    print('> input')
    print(run_steps(initial_grid=data, steps=100))

    print('===== PART2 ======')
    print('> test input')
    print(run_steps(initial_grid=test_data, steps=1000, stop=True))
    print('> input')
    print(run_steps(initial_grid=data, steps=1000, stop=True))

