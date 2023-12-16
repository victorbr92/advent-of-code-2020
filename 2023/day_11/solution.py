from itertools import combinations
from typing import List


def read():
    with open("day_11/input.txt") as f:
        input = f.read()
    return input

def duplicate_rows(lines: List[List[str]], rows_to_dup: List[int]):
    empty = ['.' for _ in range(len(lines[0]))]
    count = 0
    for r in rows_to_dup:
        lines.insert(r+count, empty)
        count+=1
    return lines

def duplicate_cols(lines: List[List[str]], cols_to_dup: List[int]):

    for line in lines:
        count = 0
        for c in cols_to_dup:
            line.insert(c+count, '.')
            count += 1
    return lines

def show(board):
    s = ''
    for l in board:
        s += ''.join(l) + '\n'
    print(s)

if __name__ == "__main__":
    inp = read()
    lines = [list(i) for i in inp.splitlines()]
    part_1 = 0
    part_2 = 0
    rows_to_dup = set(i for i in range(len(lines)))
    cols_to_dup = set(i for i in range(len(lines[0])))
    galaxies_coord = {}
    i=0
    for row, line in enumerate(lines):
        if '#' in line:
            if row in rows_to_dup:
                rows_to_dup.remove(row)
            for col, c in enumerate(line):
                if c == "#":
                    i+=1
                    galaxies_coord[i] = (row, col)
                    if col in cols_to_dup:
                        cols_to_dup.remove(col)
    for g1, g2 in combinations(galaxies_coord.keys(), r=2):
        empty_rows_passed = len(
            [
                r
                for r in rows_to_dup
                if (galaxies_coord[g2][0] < r < galaxies_coord[g1][0]) or (galaxies_coord[g1][0] < r < galaxies_coord[g2][0])
            ]
        )
        empty_cols_passed = len(
            [
                c
                for c in cols_to_dup
                if (galaxies_coord[g2][1] < c < galaxies_coord[g1][1]) or (galaxies_coord[g1][1] < c < galaxies_coord[g2][1])
            ]
        )
        dist = abs(galaxies_coord[g1][0] - galaxies_coord[g2][0]) \
            + abs(galaxies_coord[g1][1] - galaxies_coord[g2][1]) + empty_cols_passed + empty_rows_passed
        part_1 += dist
    print('PART 1')
    print(part_1)
    print('PART 2')
    exp = 999_999
    for g1, g2 in combinations(galaxies_coord.keys(), r=2):
        empty_rows_passed = len(
            [
                r
                for r in rows_to_dup
                if (galaxies_coord[g2][0] < r < galaxies_coord[g1][0]) or (galaxies_coord[g1][0] < r < galaxies_coord[g2][0])
            ]
        )*exp
        empty_cols_passed = len(
            [
                c
                for c in cols_to_dup
                if (galaxies_coord[g2][1] < c < galaxies_coord[g1][1]) or (galaxies_coord[g1][1] < c < galaxies_coord[g2][1])
            ]
        )*exp
        dist = abs(galaxies_coord[g1][0] - galaxies_coord[g2][0]) \
            + abs(galaxies_coord[g1][1] - galaxies_coord[g2][1]) + empty_cols_passed + empty_rows_passed
        part_2 += dist
    print(part_2)