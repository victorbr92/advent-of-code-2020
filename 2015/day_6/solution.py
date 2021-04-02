from typing import List, NamedTuple
import re

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


class Position(NamedTuple):
    x: int
    y: int


class Grid:

    def __init__(self):
        self.lit = set()

    @property
    def lights_on(self):
        return len(self.lit)

    def turn_on(self, start: Position, end: Position):

        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                self.lit.add(Position(x, y))

    def turn_off(self, start: Position, end: Position):

        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                if Position(x, y) in self.lit:
                    self.lit.remove(Position(x, y))

    def toggle(self, start: Position, end: Position):

        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):

                if Position(x, y) in self.lit:
                    self.lit.remove(Position(x, y))

                elif Position(x, y) not in self.lit:
                    self.lit.add(Position(x, y))

    def parse_instructions(self, instructions: List[str]):
        for instruction in instructions:
            positions = re.findall(r'\d+', instruction)

            start = Position(x=int(positions[0]), y=int(positions[1]))
            end = Position(x=int(positions[2]), y=int(positions[3]))

            if instruction.startswith('turn on'):
                self.turn_on(start, end)

            elif instruction.startswith('turn off'):
                self.turn_off(start, end)

            elif instruction.startswith('toggle'):
                self.toggle(start, end)

            else:
                raise ValueError('Wrong instruction')

            print(self.lights_on)


if __name__ == '__main__':
    # grid = Grid()
    # grid.turn_on(start=Position(0, 0), end=Position(2, 2))
    # grid.turn_off(start=Position(0, 0), end=Position(0, 0))
    # grid.toggle(start=Position(0, 0), end=Position(2, 2))
    # print(grid.lights_on)

    grid = Grid()
    grid.parse_instructions(instructions=raw_data)
    print(grid.lights_on)
