from collections import defaultdict
from tqdm import tqdm


def read_input():
    with open("input.txt") as f:
        text = list(map(int, f.read().split()))
        return text

def blink(stones_dict):
    new_stone_dict = stones_dict.copy()
    for s in stones_dict:
        # First Rule
        v = stones_dict[s]

        if s == 0:
            # print(f'{stones_dict[s]} of {s} to 1')
            new_stone_dict[1] += v

        # Second Rule
        elif len(str(s)) % 2 == 0:
            str_stone = str(s)
            left_half = str_stone[:len(str_stone)//2]
            right_half = str_stone[len(str_stone)//2:]
            new_stone_dict[int(left_half)] += v
            new_stone_dict[int(right_half)] += v
            # print(f"{stones_dict[s]} of {s} dividing in {int(left_half)} and {int(right_half)}")

        # Third Rule
        else:
            new_stone_dict[s*2024] += v
            # print(f"{stones_dict[s]} of {s} multiplying to {s*2024}")

        new_stone_dict[s] -= v
        # print(stones_dict)


    return new_stone_dict


if __name__ == "__main__":
    part1 = 0
    part2 = 0
    N_BLINKS = 25
    N_BLINKS_2 = 75

    stones = read_input()
    stones_dict = defaultdict(int)
    for stone in stones:
        stones_dict[stone] += 1

    for i in range(1,N_BLINKS+1):
        # print('---------------------------')
        stones_dict = blink(stones_dict)
        # print({k:stones_dict[k]  for k in stones_dict if stones_dict[k] > 0})
        # print(sum([stones_dict[k] for k in stones_dict]))
        # print(f"After {i} blinks:\n{' '.join(str(i) for i in stones)}\n")

    part1 = sum([stones_dict[k] for k in stones_dict])
    print(f"Result of part1: {part1}")
    print("---------------------------")

    stones_dict = defaultdict(int)
    for stone in stones:
        stones_dict[stone] += 1

    for i in range(1,N_BLINKS_2+1):
        stones_dict = blink(stones_dict)

    part2 = sum([stones_dict[k] for k in stones_dict])
    print(f"Result of part2: {part2}")
