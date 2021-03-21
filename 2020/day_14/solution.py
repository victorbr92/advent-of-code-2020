from typing import List
from itertools import product

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse_mask(raw_str: str) -> str:
    return raw_str.lstrip('mask =')


def parse_mem(raw_str: str) -> str:
    k = int(raw_str.lstrip('mem[').split(']')[0])
    v = int(raw_str.split(' = ')[-1])
    return k, v


def to_binary(value: int) -> List[int]:
    digits = []
    for _ in range(36):
        digits.append(value % 2)
        value = value // 2
    return digits[::-1]


def to_int(binary: List[int]):
    return sum([b * (2 ** i) for i, b in enumerate(binary[::-1])])


def apply_mask(binary: List[int], mask: str) -> int:
    for i, (b, m) in enumerate(zip(binary, mask)):
        if m == '0':
            binary[i] = 0
        elif m == '1':
            binary[i] = 1
    return to_int(binary)


def apply_float_mask(original: List[int], mask: str) -> List[int]:
    float_pos = []
    base = original.copy()
    for i, (b, m) in enumerate(zip(original, mask)):
        if m == '1':
            base[i] = 1
        elif m == 'X':
            base[i] = 'X'
            float_pos.append(i)

    possible_keys = []

    for values in product([0, 1], repeat=len(float_pos)):
        new = base.copy()
        for i, p in enumerate(float_pos):
            new[p] = values[i]
        possible_keys.append(to_int(new))

    return possible_keys


if __name__ == '__main__':

    mem = {}
    for line in raw_data:
        if line.startswith('mask'):
            mask = parse_mask(line)
        elif line.startswith('mem'):
            k, v = parse_mem(line)
            original_memory = to_binary(k)
            all_keys = apply_float_mask(original=original_memory, mask=mask)
            for k in all_keys:
                mem[k] = v
    print(mem)
    print(sum(mem.values()))
