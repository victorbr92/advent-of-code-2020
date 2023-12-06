import re
from dataclasses import dataclass
from collections import namedtuple
from typing import List, Tuple


@dataclass
class Card:
    card_id: int
    winning_numbers: List[int]
    my_numbers: List[int]
    matching_numbers: int

    @classmethod
    def parse_from_line(cls, line: str):
        card_id = int(re.findall(r'Card \W*(\d+)', line)[0])
        line = line.split(': ')[1].split(' | ')
        winning_numbers = [int(i) for i in re.findall(r'(\d+)', line[0])]
        my_numbers = [int(i) for i in re.findall(r'(\d+)', line[1])]
        return cls(
            card_id=card_id,
            my_numbers=my_numbers,
            winning_numbers=winning_numbers,
            matching_numbers=len(set(winning_numbers)&set(my_numbers))
        )

    def get_points(self):
        p = self.matching_numbers-1
        return int(2**p)


def read():
    with open("day_4/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    part_1 = 0
    part_2 = 0
    whole_deck = {}
    multipliers = {}
    for line in input.splitlines():
        card = Card.parse_from_line(line)
        points = card.get_points()
        part_1 += points
        whole_deck[card.card_id] = card
    print(part_1)

    total_amount = 0
    for i, card in whole_deck.items():
        matches = card.matching_numbers
        amount = multipliers.get(i, 0) + 1
        # print(f'We have {amount} copies of {i}')
        for c in range(amount):
            # print(f'...copy {c} of card {i}')
            for new in range(i+1,i+matches+1):
                # print(f'------won one card of {new}')
                multipliers[new] = multipliers.get(new, 0) + 1
        total_amount += amount
    print(total_amount)
    # part2
    # print(part_2)
