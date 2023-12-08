import re
from dataclasses import dataclass
from typing import List
from enum import Enum
from collections import Counter
from collections import deque

card_power = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    # "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3, 
    "2": 2
}

class HandType(Enum):
    five_of_kind = 6
    four_of_kind = 5
    full_house = 4
    three_of_kind = 3
    two_pair = 2
    one_pair = 1
    high_card = 0

@dataclass
class Hand:
    cards: str
    bid: int
    hand_type: HandType

    @classmethod
    def parse_from_line(cls, line:str):
        line = line.split(' ')
        hand, bid = line[0], int(line[1])
        hand_type = cls.get_card_type(hand)
        return cls(
            cards=hand,
            bid=bid,
            hand_type=hand_type,
        )

    # @staticmethod
    # def get_card_type(cards: List[str]):
    #     count_cards = Counter(cards).most_common()
    #     if count_cards[0][1] == 5:
    #         return HandType.five_of_kind
    #     if count_cards[0][1] == 4:
    #         return HandType.four_of_kind
    #     if count_cards[0][1] == 3 and count_cards[1][1] == 2:
    #         return HandType.full_house
    #     if count_cards[0][1] == 3:
    #         return HandType.three_of_kind
    #     if count_cards[0][1] == 2 and count_cards[1][1] == 2:
    #         return HandType.two_pair
    #     if count_cards[0][1] == 2:
    #         return HandType.one_pair
    #     return HandType.high_card

    @staticmethod
    def get_card_type(cards: str):
        count_cards = Counter(cards).most_common()
        new_cards = cards
        if 'J' in cards:
            mostfrequent = count_cards[0][0]
            if mostfrequent == 'J' and len(count_cards) == 1:
                mostfrequent = 'A'
            if mostfrequent == 'J' and len(count_cards) > 1:
                mostfrequent = count_cards[1][0]
            new_cards = cards.replace('J', mostfrequent)
            # print(cards, new_cards)
        count_cards = Counter(new_cards).most_common()
        if count_cards[0][1] == 5:
            return HandType.five_of_kind
        if count_cards[0][1] == 4:
            return HandType.four_of_kind
        if count_cards[0][1] == 3 and count_cards[1][1] == 2:
            return HandType.full_house
        if count_cards[0][1] == 3:
            return HandType.three_of_kind
        if count_cards[0][1] == 2 and count_cards[1][1] == 2:
            return HandType.two_pair
        if count_cards[0][1] == 2:
            return HandType.one_pair
        return HandType.high_card

    def __repr__(self) -> str:
        return f"{''.join(self.cards)}-{self.hand_type.name}: {self.bid}"

    def __lt__(self, other):
        if other.hand_type.value > self.hand_type.value:
            return True
        if other.hand_type.value < self.hand_type.value:
            return False
        for card1, card2 in zip(other.cards, self.cards):
            if card_power[card1] > card_power[card2]:
                return True
            if card_power[card2] > card_power[card1]:
                return False
        raise ValueError(f'WTF {self} cannot be compared with {other}')

def read():
    with open("day_7/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    inp = read()
    lines = inp.splitlines()
    # print('PART 1')
    # part_1 = 0
    # rank = []
    # for line in lines:
    #     hand = Hand.parse_from_line(line)
    #     rank.append(hand)
    # print(rank)
    # for i, hand in enumerate(sorted(rank)):
    #     part_1 += hand.bid*(i+1)
    # print(part_1)
    print('PART 2')
    part_2 = 0
    rank = []
    for line in lines:
        hand = Hand.parse_from_line(line)
        rank.append(hand)
    for i, hand in enumerate(sorted(rank)):
        # print(hand)
        part_2 += hand.bid*(i+1)
    print(part_2)
