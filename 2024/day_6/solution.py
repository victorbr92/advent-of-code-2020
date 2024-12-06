from rich.panel import Panel
from rich import print
from rich.live import Live
from rich.text import Text
import time
from tqdm import tqdm

DIRECTIONS = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
}
CHANGE = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0),
}


def generate_panel_content(grid, positions):
    # time.sleep(0.1)
    grid_copy = [list(row) for row in grid]
    for position in positions:
        row, col = position
        grid_copy[row][col] = f"[bold red]{grid_copy[row][col]}[/bold red]" 

    s = ''
    for row in grid_copy:
        s += ''.join(row) + '\n'
    return Panel.fit(
        s,
        title=Text(f"Grid - Unique Positions {len(positions)}",style="bold blue"),
        border_style="blue",
        padding=(0, 0),  # Remove padding (top/bottom, left/right)
    )

def execute_route(g, current_row, current_col, direction):
    positions = []
    pos = (current_row, current_col)
    positions = {pos}
    position_direction = {(pos, direction)}

    # If the guard visits the same position with the same direction it is a loop
    # with Live(generate_panel_content(grid, positions)) as live:
    i = 0
    while True:
        # Next position
        current_row, current_col = current_row + direction[0], current_col + direction[1]
        # live.update(generate_panel_content(grid, positions))

        # Check if I left the map
        if not (0 <= current_col < len(g[0]) and 0 <= current_row < len(g)):
            break

        elem = g[current_row][current_col]
        if elem == '#':
            current_row, current_col = current_row - direction[0], current_col - direction[1]
            direction = CHANGE[direction]
        else:
            pos = (current_row, current_col)
            if (pos, direction) in position_direction:
                return -1
            position_direction.add((pos, direction))
            positions.add((current_row, current_col))

        # to debug when shit happens
        i +=1
        if i >10_000:
            p = generate_panel_content(g, positions)
            print(p)
            exit(-1)

    return len(positions)

def read():
    with open("input.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    grid = read()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elem = grid[row][col]
            if elem in DIRECTIONS:
                current_row, current_col = row, col
                direction = DIRECTIONS[elem]
                break

    start = time.time()
    visited = execute_route(grid, current_row, current_col, direction)
    print(f'Unique Positions Visited: {visited}. Solved in {time.time()-start:.3f}s')

    # Brute Force all the way, it takes 1min
    start = time.time()
    loop_positions = 0
    for row in tqdm(range(len(grid))):
        for col in range(len(grid[0])):
            grid_copy = [list(row) for row in grid]
            elem = grid_copy[row][col]
            if elem == '.':
                grid_copy[row][col] = '#'
                visited = execute_route(grid_copy, current_row, current_col, direction)
                if visited == -1:
                    loop_positions += 1
    print(f'Loop Positions: {loop_positions}. Solved in {time.time()-start:.3f}s')
    