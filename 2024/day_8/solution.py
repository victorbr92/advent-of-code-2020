from typing import Tuple
from rich import print
from rich.panel import Panel
from rich.text import Text

def read_input():
    with open("input.txt") as f:
        text = f.read()
        grid = text.splitlines()
        return grid

def find_nearest_antinode(reference: Tuple[int, int], other: Tuple[int, int]):
    drow = reference[0] - other[0]
    dcol = reference[1] - other[1]
    return (reference[0] + drow, reference[1] + dcol)

def antinode_line(reference: Tuple[int, int], other: Tuple[int, int], grid):
    drow = reference[0] - other[0]
    dcol = reference[1] - other[1]

    an_list = [reference, other]
    an = (reference[0] + drow, reference[1] + dcol)
    while (0 <= an[0] < len(grid[0]) and 0 <= an[1] < len(grid)):
        an_list.append(an)
        an = (an[0] + drow, an[1] + dcol)

    return an_list


def generate_panel_content(grid, positions):
    # time.sleep(0.1)
    grid_copy = [list(row) for row in grid]
    for position in positions:
        row, col = position
        elem = grid_copy[row][col]
        if elem == '.':
            grid_copy[row][col] = f"[bold red]#[/bold red]"
        else:
            grid_copy[row][col] = f"[bold red]{elem}[/bold red]"

    s = ''
    for row in grid_copy:
        s += ''.join(row) + '\n'
    return Panel.fit(
        s,
        title=Text(f"Grid - Unique Antinodes {len(positions)}",style="bold blue"),
        border_style="blue",
        padding=(0, 0),  # Remove padding (top/bottom, left/right)
    )

if __name__ == "__main__":
    part2 = 0

    grid = read_input()
    antennas = dict()

    # pylint: disable=C0200
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elem = grid[row][col]
            if elem not in '.':
                current = antennas.get(elem, [])
                antennas[elem] = current + [(row, col)]
    # print(antennas)
    antinodes = set()

    for ant in antennas:
        to_check =  antennas[ant]
        for ref in to_check:
            for pos in to_check:
                if ref != pos:
                    antinode = find_nearest_antinode(ref, pos)
                    if (0 <= antinode[0] < len(grid[0]) and 0 <= antinode[1] < len(grid)):
                        antinodes.add(antinode)

    print(generate_panel_content(grid, antinodes))
    part1 = len(antinodes)
    print(f"Result of part1: {part1}")

    print("---------------------------")
    for ant in antennas:
        to_check =  antennas[ant]
        for ref in to_check:
            for pos in to_check:
                if ref != pos:
                    an_line = antinode_line(ref, pos, grid)
                    for an in an_line:
                        antinodes.add(an)
    print(generate_panel_content(grid, antinodes))
    part2 = len(antinodes)
    print(f"Result of part2: {part2}")
