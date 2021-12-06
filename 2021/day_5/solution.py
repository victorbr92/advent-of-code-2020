from typing import List
import numpy as np
from collections import Counter

TEST_STR = "3,4,3,1,2"


class LanternFish:
    NEW_INITIAL = 8

    def __init__(self, state: int):
        self.state = state

    def __repr__(self):
        return f'Lantern Fish (state={self.state})'

    def evolve(self):
        self.state -= 1

    @staticmethod
    def produce():
        return LanternFish(state=LanternFish.NEW_INITIAL)


test_data = [int(e) for e in TEST_STR.split(',')]

with open('input.txt', 'r') as f:
    data = [int(e) for e in f.read().split(',')]


def evolve(initial_shoal: List[LanternFish], days: int):
    shoal = initial_shoal.copy()
    for i in range(days):
        print(f'~~day {i + 1}~~ {len(shoal)}')
        new_shoal = []
        for fish in shoal:
            fish.evolve()
            if fish.state == -1:
                fish.state = 6
                new_fish = fish.produce()
                new_shoal.append(new_fish)
            new_shoal.append(fish)
        shoal = new_shoal.copy()
    print(f'~~day {days}~~ {len(shoal)}')
    return shoal


def evolve_faster(initial_shoal: List[int], days: int):
    shoal = np.array(initial_shoal)
    for i in range(days):
        print(f'~~day {i + 1}~~ {len(shoal)}')
        shoal -= 1
        n_to_create = len(shoal[shoal == -1])
        shoal[shoal == -1] = 6
        shoal = np.append(shoal, np.ones(n_to_create)*8)

    print(f'~~day {days}~~ {len(shoal)}')
    return shoal


def evolve_even_faster(initial_shoal: List[int], days: int):
    shoal = dict(Counter(initial_shoal))
    for i in range(days):
        print(f'~~day {i + 1}~~ {sum(shoal.values())}')
        new_shoal = {key-1: shoal[key] for key in shoal}
        n_to_create = new_shoal.get(-1, 0)
        new_shoal[-1] = 0
        new_shoal[6] = new_shoal.get(6, 0) + n_to_create
        new_shoal[8] = new_shoal.get(8, 0) + n_to_create
        shoal = new_shoal.copy()

    print(f'~~day {days}~~ {sum(shoal.values())}')
    return shoal


if __name__ == '__main__':
    print('===== PART1 ======')
    # _ = evolve(initial_shoal=test_data.copy(), days=18)
    # # _ = evolve(initial_shoal=data.copy(), days=80)
    # _ = evolve_faster(initial_shoal=test_data.copy(), days=18)
    # _ = evolve_faster(initial_shoal=data.copy(), days=80)
    print('> test input')
    _ = evolve_even_faster(initial_shoal=test_data.copy(), days=18)
    print('> input')
    _ = evolve_even_faster(initial_shoal=data.copy(), days=80)

    print('===== PART2 ======')
    print('> test input')
    _ = evolve_even_faster(initial_shoal=test_data.copy(), days=256)
    print('> input')
    _ = evolve_even_faster(initial_shoal=data.copy(), days=256)
