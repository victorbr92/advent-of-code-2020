from __future__ import annotations
import itertools

test_data = '''20
15
10
5
5
'''

with open('input.txt', 'r') as f:
    raw_data = f.read()


def parse(data):
    c = [int(i) for i in data.splitlines()]
    return c


def get_combinations(containers_list, target):
    for i in range(len(containers_list)):
        for c in itertools.combinations(containers_list, i+1):
            if sum(c) == target:
                yield c


def get_smaller_combination(containers_list, target):
    for i in range(len(containers_list)):
        for c in itertools.combinations(containers_list, i+1):
            if sum(c) == target:
                return i+1


if __name__ == '__main__':
    TARGET = 150
    containers = parse(raw_data)

    print(containers)
    combinations = [c for c in get_combinations(containers, TARGET)]
    print(len(combinations))
    min_containers = get_smaller_combination(containers, TARGET)
    min_combinations = [c for c in combinations if len(c) == min_containers]
    print(len(min_combinations))
