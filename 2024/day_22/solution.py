from rich import print
from math import floor
from functools import lru_cache
from tqdm import tqdm

def read_input():
    with open("input.txt") as f:
        return [int(i) for i in f.read().splitlines()]

def mix(sn, other):
    return sn ^ other

def prune(sn):
    return sn % 16777216


@lru_cache(maxsize=None)
def calc(sn):
    sn = prune(mix(sn, sn * 64))
    sn = prune(mix(sn, floor(sn / 32)))
    return prune(mix(sn, sn * 2048))

if __name__ == "__main__":
    numbers = read_input()
    max_gen = 2_000

    part1 = 0
    for sn in tqdm(numbers):
        for _ in range(max_gen):
            sn = calc(sn)
        part1 += sn
    print(f"Result of part1: {part1}")

    print('----------------------------')
    all_seq = {}
    for sn in tqdm(numbers):
        last_price = None
        buyer_seq = {}
        seq = []
        for i in range(max_gen+1):
            price = int(str(sn)[-1])
            diff = price - last_price if last_price is not None else None
            last_price = price
            seq.append(diff)
            if len(seq) > 4:
                seq.pop(0)
            if None not in seq and tuple(seq) not in buyer_seq:
                buyer_seq[tuple(seq)] = price
                all_seq[tuple(seq)] = all_seq.get(tuple(seq), 0) + price
            sn = calc(sn)
    sorted_tuples = sorted(all_seq.items(), key=lambda x:x[1], reverse=True)
    print(sorted_tuples[0:10])
    part2 = sorted_tuples[0][1]
    print(f"Result of part2: {part2}")
