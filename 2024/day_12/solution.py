from collections import defaultdict
import pprint

DIRECTIONS = [(1, 0),(0, 1),(-1, 0),(0, -1)]


def read_input():
    with open("input.txt") as f:
        text = f.read().splitlines()
        return text


def is_in_grid(pos, grid):
    return (0 <= pos[0] < len(grid[0])) and (0 <= pos[1] < len(grid))


def get_region(grid):
    seen = set()
    regions = defaultdict(list)
    region_counter = 0

    for row, line in enumerate(grid):
        for col, plot in enumerate(line):
            if (row, col) not in seen:
                region_counter += 1
                regions[f'{plot}_{region_counter}'] = [(row, col)]
                seen.add((row, col))
                queue = [(row, col)]
                while len(queue) > 0:
                    current_plot = queue.pop(-1)
                    current_type = grid[current_plot[0]][current_plot[1]]
                    for direction in DIRECTIONS:
                        next_pos = (current_plot[0] + direction[0], current_plot[1] + direction[1])
                        if is_in_grid(next_pos, grid) and next_pos not in seen:
                            next_val = grid[next_pos[0]][next_pos[1]]
                            if next_val == current_type:
                                queue.append(next_pos)
                                seen.add(next_pos)
                                regions[f'{plot}_{region_counter}'] += [next_pos]
                # print(f"Found region {plot}:{regions[f'{plot}_{region_counter}']}")
    return dict(regions)

def calculate_price(region_cords, grid):
    area = len(region_cords)
    perimeter = 4*len(region_cords)
    for coords in region_cords:
        current_type = grid[coords[0]][coords[1]]
        for direction in DIRECTIONS:
            next_pos = (coords[0] + direction[0], coords[1] + direction[1])
            if not is_in_grid(next_pos, grid):
                continue
            next_val = grid[next_pos[0]][next_pos[1]]
            if next_val == current_type:
                perimeter -= 1
    return area*perimeter

def calculate_price_advanced(region_cords, grid):
    # How to identify side, not perimeter ???
    area = len(region_cords)
    perimeter = 4*len(region_cords)
    for coords in region_cords:
        current_type = grid[coords[0]][coords[1]]
        for direction in DIRECTIONS:
            next_pos = (coords[0] + direction[0], coords[1] + direction[1])
            if not is_in_grid(next_pos, grid):
                continue
            next_val = grid[next_pos[0]][next_pos[1]]
            if next_val == current_type:
                perimeter -= 1
    return area*perimeter


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    grid = read_input()
    regions = get_region(grid)
    pprint.pprint(regions)

    for coords in regions:
        part1 += calculate_price(region_cords=regions[coords], grid=grid)
    print(f"Result of part1: {part1}")
    print("---------------------------")
    print(f"Result of part2: {part2}")
