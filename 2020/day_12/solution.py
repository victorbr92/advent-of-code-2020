from typing import NamedTuple

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

CARDINAL_CHANGE = 90
DIRECTIONS = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}


class Instruction(NamedTuple):
    action: str
    value: int

    @staticmethod
    def parse(instructions_str: str):
        return Instruction(instructions_str[0], int(instructions_str[1::]))


class Ship:

    def __init__(self):
        self.direction = 'E'

        # north, east
        self.waypoint = (1, 10)
        self.ship = (0, 0)

    def follow_instruction(self, instruction: Instruction):
        if instruction.action in ('L', 'R'):
            self._rotate(turn=instruction.action, degrees=instruction.value)
        elif instruction.action in DIRECTIONS.keys():
            self._adjust(direction=instruction.action, positions=instruction.value)
        elif instruction.action == 'F':
            self._forward(positions=instruction.value)
        else:
            raise UserWarning('Wrong instruction.')

    @property
    def distance(self):
        east, north = self.ship
        return abs(east) + abs(north)

    def _rotate(self, turn: str, degrees: int):
        changes = (degrees // CARDINAL_CHANGE)
        if changes > 3:
            changes -= 4 * (changes // 4)

        if changes == 2:
            self.waypoint = -self.waypoint[0], -self.waypoint[1]
        elif (turn == 'L' and changes == 1) or (turn == 'R' and changes == 3):
            self.waypoint = self.waypoint[1], -self.waypoint[0]
        elif (turn == 'L' and changes == 3) or (turn == 'R' and changes == 1):
            self.waypoint = -self.waypoint[1], self.waypoint[0]

    def _adjust(self, direction: str, positions: int):
        add_north, add_east = DIRECTIONS[direction]
        self.waypoint = (
            self.waypoint[0] + add_north*positions,
            self.waypoint[1] + add_east*positions
        )

    def _forward(self, positions: int):
        add_north, add_east = self.waypoint
        self.ship = (
            self.ship[0] + add_north*positions,
            self.ship[1] + add_east*positions
        )


if __name__ == '__main__':
    instructions = [Instruction.parse(i) for i in raw_data]
    ship = Ship()

    for i in instructions:
        ship.follow_instruction(instruction=i)
    print(f'The distance is {ship.distance}.')
