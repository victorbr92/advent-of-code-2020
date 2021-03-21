"""Let's assume there is only one pair that sums to 2020"""
import itertools

with open('input.txt', 'r') as f:
    inputs = sorted([int(n) for n in f.read().splitlines()])


def find_sum_2020(numbers, elements):
    """
    Find one pair of elements in a list that the sum is 2020 and multiply them together
    """
    for group in itertools.combinations(numbers, elements):
        if sum(group) == 2020:
            p = 1
            for e in group:
                p *= e
            return p


if __name__ == '__main__':
    answer = find_sum_2020(numbers=inputs, elements=2)
    print(answer)
    answer = find_sum_2020(numbers=inputs, elements=3)
    print(answer)
