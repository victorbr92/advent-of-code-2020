from __future__ import annotations
from typing import NamedTuple

with open('input.txt', 'r') as f:
    raw_data = f.read()

test_data_1 = '^>v<'
test_data_2 = '^v^v^v^v^v'

ORDERS = {'>': (+1, 0), '<': (-1, 0), '^': (0, +1), 'v': (0, -1)}


class House(NamedTuple):
    x: int
    y: int


def deliver_presents_first(directions):
    houses = set()

    x, y = 0, 0
    houses.add(House(x=x, y=y))

    for direction in directions:
        x_add, y_add = ORDERS.get(direction)
        x, y = x + x_add, y + y_add
        houses.add(House(x=x, y=y))

    return len(houses)


def deliver_presents_second(directions):
    houses = set()

    x, y = 0, 0
    x_robot, y_robot = 0, 0

    turn = 'Santa'
    houses.add(House(x=x, y=y))

    for direction in directions:
        x_add, y_add = ORDERS.get(direction)

        if turn == 'Santa':
            x, y = x + x_add, y + y_add
            houses.add(House(x=x, y=y))
            turn = 'Robo-Santa'

        elif turn == 'Robo-Santa':
            x_robot, y_robot = x_robot + x_add, y_robot + y_add
            houses.add(House(x=x_robot, y=y_robot))
            turn = 'Santa'

    return len(houses)


if __name__ == '__main__':
    assert deliver_presents_first(directions=test_data_1) == 4
    assert deliver_presents_first(directions=test_data_2) == 2

    delivered_houses = deliver_presents_first(directions=raw_data)
    print(delivered_houses)

    assert deliver_presents_second(directions=test_data_1) == 3
    assert deliver_presents_second(directions=test_data_2) == 11

    delivered_houses = deliver_presents_second(directions=raw_data)
    print(delivered_houses)
