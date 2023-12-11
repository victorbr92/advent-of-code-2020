from collections import deque
from rich import print
from rich.live import Live
from rich.panel import Panel
import time

def read():
    with open("day_10/input.txt") as f:
        input = f.read()
    # Just for the visualization    
    symbol_map = {'J': '┘', 'L': '└', 'F': '┌', '7': '┐'}
    for key, value in symbol_map.items():
        input = input.replace(key, value)
    return input

# Incoming direction and step direction
PIPES = {
    '|': {
        (0,-1): (0, -1),
        (0, 1): (0, 1),
    },
    '-': {
        (1,  0): ( 1, 0),
        (-1, 0): (-1, 0),
    },
    '└': {
        ( 0, 1): (1, 0),
        (-1, 0): (0,-1),
    },
    '┘': {
        (0, 1): (-1, 0),
        (1, 0): ( 0,-1),
    },
    '┐': {
        (0, -1): (-1, 0),
        (1, 0): (0, 1),
    },
    '┌': {
        (0, -1): (1, 0),
        (-1, 0): (0, 1),
    },
}

def show_sketch(sketch_viz):
    s = ''
    for l in sketch_viz:
        s += ''.join(l) + '\n'
    return Panel.fit(s, title='Pipe Layout')

def get_neighbors(current_position):
    x, y = current_position
    directions = [
        (0, 1),   # North
        (0, -1),  # South
        (1, 0),   # East
        (-1, 0),  # West
        (1, 1),   # Northeast
        (-1, 1),  # Northwest
        (1, -1),  # Southeast
        (-1, -1)  # Southwest
    ]
    possible_moves = [(x + dx, y + dy) for dx, dy in directions]
    return possible_moves


def get_possible_directions(current_position):
    x, y = current_position
    directions = [
        (0, 1),   # North
        (0, -1),  # South
        (1, 0),   # East
        (-1, 0),  # West
    ]
    possible_moves = [(x + dx, y + dy) for dx, dy in directions]
    return possible_moves

def get_next_position(input_pos, pipe_pos, pipe_type):
    direction = pipe_pos[0] - input_pos[0], pipe_pos[1] - input_pos[1]
    # print(input_pos, pipe_pos, pipe_type)
    # print(direction)
    step = PIPES[pipe_type][direction]
    return pipe_pos[0] + step[0], pipe_pos[1] + step[1]

if __name__ == "__main__":
    inp = read()
    lines = inp.splitlines()
    part_1 = 0
    part_2 = 0
    sketch = []
    sketch_viz = []
    for i, line in enumerate(lines):
        sketch.append(line)
        sketch_viz.append(list(line))
        if 'S' in line:
            pos = line.find('S'), i
            print(f"Starting position: {pos}")
    current_pos = pos
    possible_directions = get_possible_directions(pos)
    queue = deque(possible_directions)
    it = 0
    sketch_viz[pos[1]][pos[0]] = f'[bold red]S[/bold red]'
    seen = set()
    # with Live(show_sketch(sketch_viz), refresh_per_second=4) as live:
    while queue:
        new_pos = queue.pop()
        if new_pos[0] < 0 or new_pos[1] < 0:
            # print(f'New position {new_pos} is unfeasible')
            continue
        new_pipe = sketch[new_pos[1]][new_pos[0]]
        if new_pipe == '.':
            # print(f'New position {new_pos} is {new_pipe} = ground')
            continue
        if new_pipe == 'S':
            print(f'S found in {it} steps')
            break
        else:
            it+=1
            new_pipe_type = sketch[new_pos[1]][new_pos[0]]
            try:
                current_pos, new_pos = new_pos, get_next_position(
                    current_pos,
                    new_pos,
                    new_pipe_type
                )
                sketch_viz[current_pos[1]][current_pos[0]] = f'[bold red]{new_pipe_type}[/bold red]'
                seen.add((current_pos[1], current_pos[0]))
                queue.append(new_pos)
                # time.sleep(0.1)
                # live.update(show_sketch(sketch_viz))
            except KeyError as e:
                pass
                # print('Hit a wall')
    print(show_sketch(sketch_viz))
    print(f'First Part: {it//2}')
    new_viz = []
    print(sorted(seen))
    for i, line in enumerate(sketch):
        for j, column in enumerate(list(sketch)):
            valid_neighbors = sorted(get_neighbors((j, i)))
            all_in_loop = all(p in seen for p in valid_neighbors)
            if all_in_loop or (i==6 and j==4):
                print((i,j), valid_neighbors)
    # print('PART 2')
    # print(part_2)
