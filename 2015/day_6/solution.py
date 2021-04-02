from typing import List, NamedTuple
import re
import numpy as np

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


class Position(NamedTuple):
    x: int
    y: int
    brightness: int = 0


class Grid:

    def __init__(self):
        self.lights = np.zeros((1_000, 1_000), dtype=bool)

    @property
    def lights_on(self):
        return self.lights.sum()

    def parse_instructions(self, instructions: List[str]):
        for instruction in instructions:
            positions = re.findall(r'\d+', instruction)

            start = (int(positions[0]), int(positions[1]))
            end = (int(positions[2]), int(positions[3]))

            if instruction.startswith('turn on'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = True

            elif instruction.startswith('turn off'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = False

            elif instruction.startswith('toggle'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = ~self.lights[start[0]:end[0]+1, start[1]:end[1]+1]

            else:
                raise ValueError('Wrong instruction')


class NewGrid:

    def __init__(self):
        self.lights = np.zeros((1_000, 1_000), dtype=int)

    @property
    def brightness(self):
        return self.lights.sum()

    def parse_instructions(self, instructions: List[str]):
        for instruction in instructions:
            positions = re.findall(r'\d+', instruction)

            start = (int(positions[0]), int(positions[1]))
            end = (int(positions[2]), int(positions[3]))

            if instruction.startswith('turn on'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] += 1

            elif instruction.startswith('turn off'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] -= 1
                self.lights = self.lights.clip(min=0)

            elif instruction.startswith('toggle'):
                self.lights[start[0]:end[0]+1, start[1]:end[1]+1] += 2

            else:
                raise ValueError('Wrong instruction')


if __name__ == '__main__':
    grid = Grid()
    grid.parse_instructions(instructions=raw_data)
    print(grid.lights_on)

    grid = NewGrid()
    grid.parse_instructions(instructions=raw_data)
    print(grid.brightness)
