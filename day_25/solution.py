from typing import NamedTuple
from timeit import default_timer as timer

TEST_INPUT = (5764801, 17807724)
INPUT = (6270530, 14540258)

COMMON_SUBJECT_NUMBER = 7
DIVIDING_VALUE = 20201227


class PublicKeys(NamedTuple):
    card: int
    door: int


class Subject:

    def __init__(self, public_key: int, dividing_value: int = DIVIDING_VALUE):
        self.public_key = public_key
        self.dividing_value = dividing_value
        self.loop_number = None
        self.memo = {}

    def transform(self, loops: int, subject_number: int = COMMON_SUBJECT_NUMBER):
        if loops == 0:
            self.memo[0] = 1
            return 1

        if loops in self.memo:
            value = self.memo[loops]
            return value

        value = subject_number * self.transform(loops=loops-1)
        value = value % self.dividing_value
        self.memo[loops] = value

        return value

    def find_loop_number(self):
        loop = 0
        value = 1
        while value != self.public_key:
            value = self.transform(loops=loop)
            loop += 1

            if loop > 10E9:
                raise UserWarning('Loop number not found')

        if value == self.public_key:
            self.loop_number = loop-1
            return loop-1

    def get_encryption_key(self, loop_number):
        value = 1
        for _ in range(loop_number):
            value *= self.public_key
            value %= self.dividing_value
        return value


if __name__ == '__main__':
    start = timer()

    public_keys = PublicKeys(*INPUT)

    card = Subject(public_key=public_keys.card)
    card_loop = card.find_loop_number()
    print(card_loop)
    print(card.transform(loops=card_loop))

    print('')
    door = Subject(public_key=public_keys.door)
    door_loop = door.find_loop_number()
    print(door_loop)
    print(door.transform(loops=door_loop))

    print('')
    print(door.get_encryption_key(loop_number=card.loop_number))
    print(card.get_encryption_key(loop_number=door.loop_number))
    print('')

    end = timer()
    print('\nElapsed time: ', end - start)

