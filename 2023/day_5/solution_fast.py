import re
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Condition:
    destination_start: int
    source_start: int
    range_length: int


@dataclass
class Map:
    name: str
    conditions: List[Condition]

    @classmethod
    def parse_from_str(cls, raw_str: str):
        name = raw_str.split('map')[0]
        numbers = [int(i) for i in re.findall(r'\d+', raw_str)]
        conditions = []
        for i in range(len(numbers)//3):
            dr_start, sr_start, r_l = numbers[3*i], numbers[3*i+1], numbers[3*i+2]
            condition = Condition(
                destination_start=dr_start,
                source_start=sr_start,
                range_length=r_l,
            )
            conditions.append(condition)

        return cls(
            name=name,
            conditions=conditions
        )

    def apply_map(self, n: int):
        for condition in self.conditions:
            source_min = condition.source_start
            source_max = condition.source_start + condition.range_length
            if n >= source_min and n < source_max:
                diff = n - source_min
                return condition.destination_start + diff
        return n

    def change_ranges(self, seed_range: Tuple[int, int]):
        new_ranges = []
        seeds_to_check = [seed_range]
        while seeds_to_check:
            n_min, n_max = seeds_to_check.pop()
            for condition in self.conditions:
                source_min = condition.source_start
                source_max = condition.source_start + condition.range_length
                diff = condition.destination_start - source_min
                overlap_start = max(n_min, source_min)
                overlap_end = min(n_max, source_max)
                if overlap_end >= overlap_start:
                    new_ranges.append((overlap_start + diff, overlap_end + diff))
                    if overlap_start > n_min:
                        seeds_to_check.append((n_min, overlap_start-1))
                    if n_max > overlap_end:
                        seeds_to_check.append((overlap_end+1, n_max))
                    break
            else:
                new_ranges.append((n_min, n_max))
        return new_ranges


def read():
    with open("day_5/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    part_1 = 0
    part_2 = 0
    seeds = [int(i) for i in re.findall(r'\d+', input.splitlines()[0])]
    print(seeds)
    maps = input.split('\n\n')[1:]
    map_list = []
    for map_str in maps:
        map = Map.parse_from_str(map_str)
        map_list.append(map)
    print('part_1')
    seed_location = {}
    for seed in seeds:
        n = seed
        for map in map_list:
            n = map.apply_map(n)
        seed_location[seed] = n
    print(min(seed_location.values()))
    print('part_2')
    new_seeds = []
    for i in range(len(seeds)//2):
        seed_start, seed_end = seeds[2*i], seeds[2*i]+seeds[2*i+1]
        new_seeds.append((seed_start, seed_end))
    seed_location = []
    for seed_range in new_seeds:
        ranges = [seed_range]
        for map in map_list:
            new_possible_ranges = []
            for r in ranges:
                new_ranges = map.change_ranges(r)
                new_possible_ranges += new_ranges
            ranges = new_possible_ranges
        seed_location.append((min(i[0] for i in ranges)))
    print(min(seed_location))
