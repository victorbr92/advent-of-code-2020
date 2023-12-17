#credit to https://advent-of-code.xavd.id/writeups/2023/day/12/
import re
from itertools import product
from tqdm import tqdm
from functools import cache

def read():
    with open("day_12/input.txt") as f:
        input = f.read()
    return input

def replace_unk(records, possible_values):
    new_record = []
    for r in records:
        if r != '?':
            new_record.append(r)
        else:
            new_record.append(possible_values.pop())
    return ''.join(i for i in new_record)

def is_valid(record, damaged):
    damaged_count = [len(i) for i in re.split(r'\.+', record) if i]
    if len(damaged_count) != len(damaged):
        return False
    # print(damaged_count, damaged)
    return damaged_count == damaged

@cache
def num_valid_solutions(record: str, damaged: tuple[int, ...]) -> int:
    if record == "":
        return len(damaged) == 0

    if not damaged:
        # if there are no more groups the only possibility of success
        # is that there are no `#` remaining
        return "#" not in record

    char, rest_of_record = record[0], record[1:]

    if char == ".":
        # dots are ignores, so keep recursing
        return num_valid_solutions(rest_of_record, damaged)

    if char == "#":
        group = damaged[0]
        # we're at the start of a group! make sure there are enough here to fill the first group
        # to be valid, we have to be:
        if (
            # long enough to match
            len(record) >= group
            # made of only things that can be `#` (no `.`)
            and all(c != "." for c in record[:group])
            # either at the end of the record (allowed)
            # or the next character isn't also a `#` (would be too big)
            and (len(record) == group or record[group] != "#")
        ):
            return num_valid_solutions(record[group + 1 :], damaged[1:])

        return 0

    if char == "?":
        return num_valid_solutions(f"#{rest_of_record}", damaged) + num_valid_solutions(
            f".{rest_of_record}", damaged
        )

def solve_line(line: str, multiplier=1) -> int:
    l = line.split(' ')
    damaged = tuple(int(i) for i in l[1].split(','))
    records = l[0]

    if multiplier > 1:
        records = "?".join([records] * 5)
        damaged *= 5

    return num_valid_solutions(records, damaged)

def count_arrangements(line):
    l = line.split(' ')
    damaged = (int(i) for i in l[1].split(','))
    records = l[0]
    unknown = records.count('?')
    counter = 0
    for c in product('.#', repeat=unknown):
        new_record = replace_unk(records, list(c))
        if is_valid(new_record, damaged):
            counter+=1
    return counter

if __name__ == "__main__":
    inp = read()
    lines = inp.splitlines()
    part_1 = 0
    part_2 = 0
    for line in tqdm(lines):
        part_1 += solve_line(line)
    print('PART 1')
    print(part_1)
    print('PART 2')
    for line in tqdm(lines):
        part_2 += solve_line(line, multiplier=5)
    print(part_2)
