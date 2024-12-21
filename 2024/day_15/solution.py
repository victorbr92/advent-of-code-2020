from time import sleep
from rich import print
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

DIRECTIONS = {
    '^': (-1, 0),
    'v': (+1, 0),
    '>': (0, +1),
    '<': (0, -1)
}

def read_input():
    with open("2024/day_15/input.txt") as f:
        warehouse, movements = f.read().split('\n\n')

    return warehouse.splitlines(), movements.replace('\n', '')

def move(start_pos, movement, grid):
    current_el = grid[start_pos[0]][start_pos[1]]

    # check what is in the next pos
    next_pos = start_pos[0] + DIRECTIONS[movement][0], start_pos[1] + DIRECTIONS[movement][1]
    el_next_pos = grid[next_pos[0]][next_pos[1]]

    if el_next_pos == '#':
        # print('Hit a wall')
        return start_pos, grid, False

    if el_next_pos == '.':
        # print('Ok to move.')
        grid[next_pos[0]][next_pos[1]] = current_el
        grid[start_pos[0]][start_pos[1]] = '.'
        return next_pos, grid, True

    if el_next_pos == 'O':
        # print(f'Trying to move {current_el} from {start_pos} to {next_pos}')
        _, _, ok = move(start_pos=next_pos, movement=movement, grid=grid)
        if ok:
            grid[next_pos[0]][next_pos[1]] = current_el
            grid[start_pos[0]][start_pos[1]] = '.'
            return next_pos, grid, True
        else:
            return start_pos, grid, False

    raise ValueError(f'GULP: {el_next_pos=}')


def move_part2(start_pos, movement, grid):
    current_el = grid[start_pos[0]][start_pos[1]]

    # check what is in the next pos
    next_pos = start_pos[0] + DIRECTIONS[movement][0], start_pos[1] + DIRECTIONS[movement][1]
    el_next_pos = grid[next_pos[0]][next_pos[1]]

    if el_next_pos == '#':
        return start_pos, grid, False

    if el_next_pos == '.':
        grid[next_pos[0]][next_pos[1]] = current_el
        grid[start_pos[0]][start_pos[1]] = '.'
        return next_pos, grid, True

    if el_next_pos in '[]' and movement in '><':
        # If this happens, both should move together
        print(f'Trying to move {current_el} from {start_pos} to {next_pos}')
        _, _, ok = move_part2(start_pos=next_pos, movement=movement, grid=grid)
        if ok:
            grid[next_pos[0]][next_pos[1]] = current_el
            grid[start_pos[0]][start_pos[1]] = '.'
            return next_pos, grid, True
        else:
            return start_pos, grid, False

    if el_next_pos in '[]' and movement in '^v':
        print(f'Trying to move {current_el} from {start_pos} to {next_pos}')
        if el_next_pos == '[':
            other = 1
        else:
            other = -1
        other_next_pos = next_pos[0], next_pos[1] + other
        other_el_next_pos = grid[other_next_pos[0]][other_next_pos[1]]
        print(f'Have to move {el_next_pos} from {next_pos}')
        print(f'Have to move {other_el_next_pos} from {other_next_pos}')
        _, _, ok = move_part2(start_pos=next_pos, movement=movement, grid=grid)
        other_next_pos, _, ok_other = move_part2(start_pos=other_next_pos, movement=movement, grid=grid)
        if ok and ok_other:
            grid[next_pos[0]][next_pos[1]] = current_el
            grid[start_pos[0]][start_pos[1]] = '.'
            return next_pos, grid, True
        else:
            return start_pos, grid, False

    raise ValueError(f'GULP: {el_next_pos=}')


def show_grid(grid, direction, i):
    sleep(1)
    s = ''
    for line in grid:
        s += ''.join(line) + '\n'
    return Panel.fit(
        s,
        title=Text(f'Movement {i} for direction {direction}'),
        style="bold blue",
        border_style="blue",
    )

def calc_gps(grid):
    total = 0
    for col, line in enumerate(grid):
        for row, el in enumerate(line):
            if el == 'O':
                total += 100*col + row
    return total

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    # warehouse, movements = read_input()
    # grid = []
    # max_col, max_row = len(warehouse), len(warehouse[0])
    # for col, line in enumerate(warehouse):
    #     grid_line = []
    #     for row, el in enumerate(line):
    #         if el == '@':
    #             fish_pos = (col, row)
    #         grid_line.append(el)
    #     grid.append(grid_line)

    # with Live(show_grid(grid, 0, 0), refresh_per_second=10) as live:
    #     for i, direction in enumerate(movements):
    #         fish_pos, grid, ok = move(start_pos=fish_pos, movement=direction, grid=grid)
    #         live.update(show_grid(grid, direction, i))

    # part1 = calc_gps(grid)
    print(f"Result of part1: {part1}")
    print("---------------------------")
    warehouse, movements = read_input()
    grid = []
    for col, line in enumerate(warehouse):
        g_line = ''
        for row, el in enumerate(line):
            if el == '@':
                g_line += '@.'
                fish_pos = (col, row*2)
            elif el == '#':
                g_line += '##'
            elif el == '.':
                g_line +=  '..'
            elif el == 'O':
                g_line += '[]'
            else:
                raise ValueError(el)
        grid.append(list(g_line))

    # with Live(show_grid(grid, 0, 0), refresh_per_second=10) as live:
    for i, direction in enumerate(movements):
        fish_pos, grid, ok = move_part2(start_pos=fish_pos, movement=direction, grid=grid)
        print(show_grid(grid, direction, i))
        
    print(f"Result of part2: {part2}")
