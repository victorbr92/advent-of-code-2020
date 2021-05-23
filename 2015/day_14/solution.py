from __future__ import annotations
from typing import NamedTuple
import re

test_data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".splitlines()


with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse(data):
    reindeers = []

    for line in data:
        name = line.split(' ')[0]
        numbers = re.findall(r'(\d+)', line)
        reindeer = Reindeer(
            name=name,
            speed_km_s=int(numbers[0]),
            duration_s=int(numbers[1]),
            rest_s=int(numbers[2]),
        )
        reindeers.append(reindeer)

    return reindeers


class Reindeer:

    def __init__(self, name, speed_km_s, duration_s, rest_s):
        self.name = name
        self.speed_km_s = speed_km_s
        self.duration_s = duration_s
        self.rest_s = rest_s

        self.distance: int = 0
        self.elapsed: int = 0
        self.state: str = 'flying'
        self.rest: int = duration_s
        self.points: int = 0

    def distance_traveled(self, seconds: int):
        full_cycles = seconds // (self.duration_s + self.rest_s)
        rest_of_last_cycle_s = seconds % (self.duration_s + self.rest_s)
        distance = full_cycles*self.duration_s*self.speed_km_s

        distance += min(rest_of_last_cycle_s, self.duration_s) * self.speed_km_s

        return distance

    def increment_second(self):
        if self.state == 'flying':
            self.distance += self.speed_km_s

        self.rest -= 1
        if self.rest == 0:
            if self.state == 'flying':
                self.rest = self.rest_s
                self.state = 'resting'
            else:
                self.rest = self.duration_s
                self.state = 'flying'

    def __repr__(self):
        return f'{self.name}: {self.distance}km and {self.points} points'


def find_winner(reindeers, given_seconds):
    max_distance = 0
    winner = ''

    for reindeer in reindeers:
        traveled = reindeer.distance_traveled(seconds=given_seconds)
        if traveled > max_distance:
            max_distance = traveled
            winner = reindeer.name

    print(winner, max_distance)


def run_race(end_s: int, reindeers_list):
    max_distance = 0

    for i in range(end_s):
        winners = []
        for reindeer in reindeers_list:
            reindeer.increment_second()

            if reindeer.distance > max_distance:
                max_distance = reindeer.distance
                winners = [reindeer]
            elif reindeer.distance == max_distance:
                winners.append(reindeer)

        for winner in winners:
            winner.points += 1


if __name__ == '__main__':
    SECONDS = 2_503
    reindeers = parse(raw_data)
    find_winner(reindeers, given_seconds=SECONDS)
    run_race(reindeers_list=reindeers, end_s=SECONDS)
    print(reindeers)
