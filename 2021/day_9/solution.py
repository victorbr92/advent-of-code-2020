from typing import List, Tuple, Dict

TEST_STR = """2199943210
3987894921
9856789892
8767896789
9899965678"""

COORDS = [
    (1, 0),  # right,
    (-1, 0),  # left
    (0, 1),  # up
    (0, -1)  # left
]

test_data = [e for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [e for e in f.read().splitlines()]


def find_low_points(heightmap: List[str]):
    max_x = len(heightmap)
    max_y = len(heightmap[0])

    low_points = []
    acc_risk_levels = 0
    for x in range(max_x):
        for y in range(max_y):
            point = int(heightmap[x][y])
            for coord in COORDS:
                if (0 <= (x + coord[0]) < max_x) and (0 <= (y + coord[1]) < max_y) and \
                        point >= int(heightmap[x + coord[0]][y + coord[1]]):
                    break
            else:
                low_points.append((x, y))
                acc_risk_levels += 1 + point

    print(acc_risk_levels)
    return low_points


def find_basins(heightmap: List[str], test_low_points: List[Tuple[int, int]]):
    max_x = len(heightmap)
    max_y = len(heightmap[0])

    basin_sizes = []
    for low_point in test_low_points:
        edges = [low_point]
        basin_points = set()
        while len(edges) > 0:
            point = edges.pop()
            x, y = point
            point_value = int(heightmap[x][y])
            basin_points.add(point)
            for coord in COORDS:
                new_edge = (x + coord[0], y + coord[1])
                if (0 <= new_edge[0] < max_x) and (0 <= new_edge[1] < max_y) \
                        and int(heightmap[new_edge[0]][new_edge[1]]) != 9 and \
                        point_value <= int(heightmap[new_edge[0]][new_edge[1]]) \
                        and new_edge not in basin_points:
                    edges.append(new_edge)
        basin_sizes.append(len(basin_points))

    biggest = sorted(basin_sizes, reverse=True)[:3]
    print(biggest)
    return biggest[0]*biggest[1]*biggest[2]


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    test_low_points = find_low_points(heightmap=test_data)
    print('> input')
    low_points = find_low_points(heightmap=data)

    print('===== PART2 ======')
    print(find_basins(test_data, test_low_points))
    print(find_basins(data, low_points))
