from typing import NamedTuple
from collections import defaultdict

TEST_STR = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse(line: str):
    coords = line.split(' -> ')
    c1 = tuple(int(e) for e in coords[0].split(','))
    c2 = tuple(int(e) for e in coords[1].split(','))
    return c1, c2


test_data = [parse(e) for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [parse(e) for e in f.read().splitlines()]


def add_line(points, c1, c2, diagonal=False):
    if c1[0] == c2[0]:
        diff_y = abs(c2[1] - c1[1])
        y_init = min(c2[1], c1[1])
        for y in range(y_init, y_init+diff_y+1):
            point = (c1[0], y)
            points[point] += 1

    elif c1[1] == c2[1]:
        diff_x = abs(c2[0] - c1[0])
        x_init = min(c2[0], c1[0])
        for x in range(x_init, x_init+diff_x+1):
            point = (x, c1[1])
            points[point] += 1

    elif diagonal and abs(c1[1] - c2[1]) == abs(c1[0] - c2[0]):
        diff_x = c2[0] - c1[0]
        diff_y = c2[1] - c1[1]

        for x_inc, y_inc in zip(range(abs(diff_x)+1), range(abs(diff_y)+1)):
            if diff_y < 0:
                y = c1[1] - y_inc
            else:
                y = c1[1] + y_inc
            if diff_x < 0:
                x = c1[0] - x_inc
            else:
                x = c1[0] + x_inc
            point = (x, y)
            points[point] += 1

    return points


def complete_diagram(lines, diagonal=False):
    points = defaultdict(int)
    for line in lines:
        points = add_line(points, line[0], line[1], diagonal)
    return points


if __name__ == '__main__':
    print('===== PART1 ======')
    diagram = complete_diagram(test_data)
    intersection = [point for point in diagram if diagram[point] > 1]
    print(len(intersection), intersection)

    diagram = complete_diagram(data)
    intersection = [point for point in diagram if diagram[point] > 1]
    print(len(intersection))

    print('===== PART2 ======')
    diagram = complete_diagram(test_data, diagonal=True)
    intersection = [point for point in diagram if diagram[point] > 1]
    print(len(intersection), intersection)

    diagram = complete_diagram(data, diagonal=True)
    intersection = [point for point in diagram if diagram[point] > 1]
    print(len(intersection))
