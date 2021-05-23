from __future__ import annotations
from collections import defaultdict
from itertools import permutations
from typing import Dict, List

import re

test_data = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".splitlines()


with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def parse(data):
    happiness = defaultdict(dict)
    for line in data:
        person_1 = line.split(' ')[0]
        amount_text = re.findall(r'(lose|gain|\d+)', line)
        if amount_text[0] == 'gain':
            amount = int(amount_text[1])
        else:
            amount = - int(amount_text[1])
        person_2 = line.split(' ')[-1][0:-1]
        happiness[person_1][person_2] = amount
    return dict(happiness)


class Person:
    def __init__(self, name):
        self.name = name

        self.left_name = ''
        self.left_value = 0

        self.right_name = ''
        self.right_value = 0

    def assign(self, person: Person, position: str, happiness: Dict):
        if position == 'left' and self.left_name != person.name:
            self.left_value = happiness[self.name][person.name]
            self.left_name = person.name
            person.assign(person=self, position='right', happiness=happiness)

        if position == 'right' and self.right_name != person.name:
            self.right_value = happiness[self.name][person.name]
            self.right_name = person.name
            person.assign(person=self, position='left', happiness=happiness)

    @property
    def happiness(self):
        return self.right_value + self.left_value

    def __repr__(self):
        return self.name


class Table:
    def __init__(self, guests_order: List[str], happiness: dict):
        self.guests = [Person(name) for name in guests_order]
        self.guests[0].assign(self.guests[-1], 'left', happiness)
        for i in range(len(self.guests)-1):
            self.guests[i].assign(self.guests[i+1], 'right', happiness)

    @property
    def total_happiness(self):
        return sum(person.happiness for person in self.guests)

    def __repr__(self):
        return '->'.join(guest.name for guest in self.guests)


def find_optimal(guests: list, happinnes_dict: dict):
    max_happiness = 0
    for orders in permutations(guests[0:-1]):
        resulting_order = list(orders)
        resulting_order.append(guests[-1])
        table = Table(guests_order=resulting_order, happiness=happinnes_dict)
        if table.total_happiness > max_happiness:
            max_happiness = table.total_happiness
            print(table, table.total_happiness)
    print(max_happiness)


def add_myself(original_dict):
    modified = {}
    modified['me'] = {}

    for person in original_dict:
        modified[person] = original_dict[person]
        modified[person]['me'] = 0
        modified['me'][person] = 0

    return modified


if __name__ == '__main__':
    happy_dict = parse(raw_data)
    find_optimal(guests=list(happy_dict.keys()), happinnes_dict=happy_dict)
    print('----- PART 2 -----')
    new_happy_dict = add_myself(happy_dict)
    find_optimal(guests=list(new_happy_dict.keys()), happinnes_dict=new_happy_dict)
