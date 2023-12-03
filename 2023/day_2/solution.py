import re
from dataclasses import dataclass
from collections import namedtuple
from typing import List, Tuple

Round = namedtuple("Round", ["red", "green", "blue"])

@dataclass
class Game:
    game_id: int
    rounds: List[Round] # (r,g,b)

    @classmethod
    def parse_from_line(cls, line: str):
        game_id = int(re.findall(r'Game (\d+)', line)[0])
        line = line.split(': ')[1]
        rounds_str = line.split('; ')
        rounds = []
        for r in rounds_str:
            red = re.findall(r'(\d+) red', r) or [0]
            green = re.findall(r'(\d+) green', r) or [0]
            blue = re.findall(r'(\d+) blue', r) or [0]
            rounds.append(Round(
                red=int(red[0]),
                green=int(green[0]),
                blue=int(blue[0]),
                )
            )
        return cls(
            game_id=game_id,
            rounds=rounds
        )

    def valid_round_limits(self, round_max: Round):
        for r in self.rounds:
            if (r.red > round_max.red) or (r.green > round_max.green) or (r.blue > round_max.blue):
                return False
        return True
 
    def get_min_cubes(self):
        red, green, blue = 0, 0, 0
        for r in self.rounds:
            if r.red>red:
                red=r.red
            if r.green>green:
                green=r.green
            if r.blue>blue:
                blue=r.blue
        return red, green, blue


def read():
    with open("day_2/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    games = []
    round_max = Round(red=12, green=13, blue=14)
    part_1 = 0
    part_2 = 0
    for line in input.splitlines():
        game = Game.parse_from_line(line)
        print(game)
        if game.valid_round_limits(round_max):
            games.append(game)
            part_1 += game.game_id
        min_values = game.get_min_cubes()
        power_min_values = min_values[0]*min_values[1]*min_values[2]
        part_2 += power_min_values
    print(part_1)
    print(part_2)
