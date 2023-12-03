import re
from dataclasses import dataclass
from collections import namedtuple
from typing import List, Tuple

# Each symbol has a x and y value
# y is the line number
# x is their initial position

# Each number has an value, y value and x list
# y is the line number
# x is the start of the number + the length of the number
# it should have a method called is_adjacent_to_symbol receiving the list of symbols as input
# to check if it is adjacent
# create a border coordinate lits adding 1 and reducing to every coordinates combination and then iterating over the symbols to see if any match

Symbol = namedtuple('Symbol', ['value', 'x', 'y'])

@dataclass
class Number:
    value: int
    x: List[int]
    y: int

    def get_border_coordinates(self):
        points = [
            (min(self.x) - 1, self.y - 1),  # Top-left
            (min(self.x) - 1, self.y),   # Left
            (min(self.x) - 1, self.y + 1),  # Bottom-left
            (max(self.x) + 1, self.y),   # Right
            (max(self.x) + 1, self.y - 1),  # Top-right
            (max(self.x) + 1, self.y + 1),  # Bottom-right
        ]
        for x in self.x:
            points += [(x, self.y - 1),(x, self.y + 1)]   # Up and Down

        # removing all negative points
        return [p for p in points if p[0]>=0 and p[1]>=0]

    def is_adjacent_to_symbol(self, symbols: List[Symbol]):
        borders = self.get_border_coordinates()
        for symbol in symbols:
            if (symbol.x, symbol.y) in borders:
                return True
        return False


def parse_schematic(schematic):
    symbols = []
    numbers = []
    p = re.compile("\d+")
    for y, line in enumerate(schematic.splitlines()):
        for m in p.finditer(line):
            number = Number(
                value=int(m.group()),
                y=y,
                x=[i for i in range(m.start(), m.end())]
            )
            numbers.append(number)
        symbols += [Symbol(x=m.start(), y=y, value=m.group()) for m in re.finditer(r'[^\w^\.]', line)]

    return symbols, numbers

def find_adjacent_numbers(symbol: Symbol, numbers: List[Number]):
    points =  [
        (symbol.x, symbol.y - 1), # Up
        (symbol.x, symbol.y + 1), # Down
        (symbol.x - 1, symbol.y - 1),  # Top-left
        (symbol.x - 1, symbol.y),   # Left
        (symbol.x - 1, symbol.y + 1),  # Bottom-left
        (symbol.x + 1, symbol.y),   # Right
        (symbol.x + 1, symbol.y - 1),  # Top-right
        (symbol.x + 1, symbol.y + 1),  # Bottom-right
    ]
    # removing all negative points
    symbol_border = [p for p in points if p[0]>=0 and p[1]>=0]
    numbers_borders = set()
    for number in numbers:
        y = number.y
        for x in number.x:
            if (x, y) in symbol_border:
                numbers_borders.add(number.value)
    return list(numbers_borders)

def read():
    with open("day_3/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    symbols, numbers = parse_schematic(input)
    adjacent = []
    for number in numbers:
        if number.is_adjacent_to_symbol(symbols):
            adjacent.append(number.value)
    print(sum(adjacent))
    gear_ratios = []
    for symbol in symbols:
        if symbol.value == '*':
            gears = find_adjacent_numbers(symbol, numbers)
            if len(gears) == 2:
                gear_ratios.append(gears[0]*gears[1])
    print(sum(gear_ratios))
