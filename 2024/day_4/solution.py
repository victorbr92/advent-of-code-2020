from typing import List, Tuple

DIRECTIONS = [
    (0, 1),   # left-to-right
    (0, -1),  # right-to-left
    (1, 0),   # top-to-bottom
    (-1, 0),  # bottom-to-top
    (1, 1),   # top-left to bottom-right
    (-1, -1), # bottom-right to top-left
    (1, -1),  # top-right to bottom-left
    (-1, 1),  # bottom-left to top-right
]

X_DIRECTIONS = [
    (1, -1),  # center to bottom-left
    (-1, 1),  # center to top-right
]

def read():
    with open("input.txt") as f:
        return f.read().splitlines()

def check_xmas(grid: List[List[str]], x: int, y: int, direction: Tuple[int, int]):
    TARGET_WORD = 'XMAS'
    word=''
    for i in range(4):
        row = y + i*direction[0]
        col = x + i*direction[1]
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return 0
        if grid[row][col] != TARGET_WORD[i]:
            return 0
        word += grid[row][col]

    return 1

def check_x(grid: List[List[str]], col: int, row: int):
    if not (1 <= row < len(grid)-1 and 1 <= col < len(grid[0])-1):
        return 0

    top_left = grid[row-1][col-1]
    bottom_left = grid[row+1][col-1]
    bottom_right = grid[row+1][col+1]
    top_right = grid[row-1][col+1]

    add = 0
    if (top_left == 'M') and (bottom_right == 'S'):
        add +=1
    if (top_right == 'M') and (bottom_left == 'S'):
        add +=1
    if (bottom_right == 'M') and (top_left == 'S'):
        add +=1
    if (bottom_left == 'M') and (top_right == 'S'):
        add +=1

    if add == 2:
        return 1
    
    return 0


if __name__ == "__main__":
    text = read()
    first_list = []
    second_list = []

    reports = []

    part1 = 0
    part2 = 0
    for y, line in enumerate(text):
        for x, word in enumerate(line):
            if word == 'X':
                for direction in DIRECTIONS:
                    part1 += check_xmas(text, x, y, direction)
            if word == 'A':
                part2 += check_x(text, x, y)

    print(part1)
    print(part2)
