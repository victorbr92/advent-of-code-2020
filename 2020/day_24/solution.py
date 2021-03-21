from __future__ import annotations
from typing import NamedTuple, List
import re
from timeit import default_timer as timer

DIRECTIONS = {
    'w':  (-1, +1, 0),
    'nw': (0, +1, -1),
    'ne': (+1, 0, -1),
    'e':  (+1, -1, 0),
    'se': (0, -1, +1),
    'sw': (-1, 0, +1)
}


class Tile(NamedTuple):
    x: int
    y: int
    z: int

    def next_position(self, direction) -> Tile:
        x_add, y_add, z_add = DIRECTIONS.get(direction)
        x = self.x + x_add
        y = self.y + y_add
        z = self.z + z_add

        return Tile(x, y, z)


class Grid:

    def __init__(self, initial_tile=Tile(0, 0, 0)):
        self.black_tiles = set()
        self.current = initial_tile

    def flip(self, direction):
        self.current = self.current.next_position(direction)

    def change_color(self):
        if self.current in self.black_tiles:
            self.black_tiles.remove(self.current)
        else:
            self.black_tiles.add(self.current)

    def flip_many(self, lines: str):
        for line in lines:
            actions = self._parse(line)
            self.restart()
            for action in actions:
                self.flip(action)
            self.change_color()

    @staticmethod
    def _parse(line: str) -> List[str]:
        return re.findall(r'(e|se|sw|w|nw|ne)', line)

    def restart(self, tile=Tile(0, 0, 0)):
        self.current = tile
        self.change_color()

    def simulate_day(self):
        new_black = self.get_new_black()
        to_black = self.get_white_to_flip()

        self.black_tiles = new_black | to_black

    def get_white_to_flip(self):
        white_adjacent = {}
        for tile in self.black_tiles:
            for direction in DIRECTIONS:
                possible_tile = tile.next_position(direction)
                if possible_tile not in self.black_tiles:
                    white_adjacent[possible_tile] = white_adjacent.get(possible_tile, 0) + 1
        return {tile for tile in white_adjacent if white_adjacent[tile] == 2}

    def get_new_black(self):
        to_flip = set()
        for tile in self.black_tiles:
            counter = 0
            for direction in DIRECTIONS:
                if tile.next_position(direction) in self.black_tiles:
                    counter += 1
            if counter in (1, 2):
                to_flip.add(tile)

        return to_flip


if __name__ == '__main__':
    start = timer()
    with open('input.txt', 'r') as f:
        raw_data = f.read().splitlines()

    grid = Grid()
    grid.flip_many(raw_data)

    print(f'Day 0: {len(grid.black_tiles)}')
    for day in range(1, 101, 1):
        grid.simulate_day()
        print(f'Day {day}: {len(grid.black_tiles)}')

    end = timer()
    print(f'Elapsed time: {end - start}')
