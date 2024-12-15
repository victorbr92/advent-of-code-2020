from pprint import pprint
from collections import namedtuple, defaultdict
from typing import List, Tuple
from functools import reduce
from operator import mul
from rich import print
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

Robot = namedtuple('Robot', ['p', 'v'])

def read_input():
    with open("input.txt") as f:
        text = f.read().splitlines()
    robots = []
    for sample in text:
        p,v = sample.split(' ')
        p = p.strip('p=').split(',')
        v = v.strip('v=').split(',')
        robot = Robot(p=[int(i) for i in p], v=[int(i) for i in v])
        robots.append(robot)
    return robots

def run(robots: List[Robot], grid_max: Tuple[int, int]):
    for robot in robots:
        for coord in range(2):
            robot.p[coord] += robot.v[coord]
            if robot.p[coord] > grid_max[coord]:
                robot.p[coord] -= grid_max[coord] + 1
            if robot.p[coord] < 0:
                robot.p[coord] = grid_max[coord] + robot.p[coord] + 1
    return robots

def count_safety(robots: List[Robot], grid_max: Tuple[int, int]):
    half_x = grid_max[0]//2
    half_y = grid_max[1]//2
    quadrants = {
        'q1': [(0, half_x-1), (0, grid_max[1]//2-1)], # top-left
        'q2': [(half_x+1, grid_max[0]), (0, grid_max[1]//2-1)], # top-right
        'q3': [(0, half_x-1), (half_y+1, grid_max[1])], # bottom-left
        'q4': [(half_x+1, grid_max[0]), (half_y+1, grid_max[1])], # top-right
    }
    pprint(quadrants)
    q_robots = defaultdict(int)
    for robot in robots:
        for quadrant in quadrants:
            q = quadrants[quadrant]
            if (q[0][0] <= robot.p[0] <= q[0][1]) and (q[1][0] <= robot.p[1] <= q[1][1]):
                q_robots[quadrant] += 1
    return q_robots

def count_unique(robots: List[Robot]):
    seen = set()
    for robot in robots:
        seen.add((robot.p[0], robot.p[1]))
    return seen

def show_grid(seen, max_row, max_col):
    s = ''  
    for row in range(max_row):
        l = ''
        for col in range(max_col):
            if (row, col) in seen:
                e = '.'
            else:
                e = '#'
            s += e
        s += ''.join(l) + '\n'
    return print(Panel.fit(
        s,
        title=Text(f"Robots {len(seen)}",
        style="bold blue"),
        border_style="blue",
    ))


if __name__ == "__main__":
    SECONDS = 100
    GRID = (100, 102)
    part1 = 0
    part2 = 0

    robots = read_input()
    n_robots = len(robots)
    for _ in range(SECONDS):
        run(robots, grid_max=GRID)
    q_robots = count_safety(robots, grid_max=GRID)
    pprint(q_robots)
    part1 = reduce(mul, [q_robots[q] for q in q_robots])
    print(f"Result of part1: {part1}")
    print("---------------------------")
    # visualize to help this
    robots = read_input()
    for part2 in range(100_000):
        run(robots, grid_max=GRID)
        seen = count_unique(robots)
        prop = 100*len(seen)/len(robots)
        if prop > 99.9:
            print(prop, part2)
            show_grid(seen=seen, max_row=GRID[0], max_col=GRID[1])
            break
    print(f"Result of part2: {part2}")
