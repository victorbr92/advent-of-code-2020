from typing import List
from timeit import default_timer as timer

STARTING_NUMBERS = '11,0,1,10,5,19'
TEST_NUMBERS_1 = '0,3,6'
TEST_NUMBERS_2 = '3,1,2'
TEST_NUMBERS_3 = '2,1,3'


class Game:

    def __init__(self, starting_numbers: str):
        numbers: List = [int(n) for n in starting_numbers.split(',')]

        self.turn = len(numbers)
        self.last_turn_memo = {n: p + 1 for p, n in enumerate(numbers[:-1])}
        self.last_number_spoken = numbers[-1]

    def play_turn(self):
        if self.last_number_spoken in self.last_turn_memo:
            number = self.turn - self.last_turn_memo[self.last_number_spoken]
        else:
            number = 0
        self.last_turn_memo[self.last_number_spoken] = self.turn

        self.turn += 1
        self.last_number_spoken = number


if __name__ == '__main__':

    game = Game(starting_numbers=STARTING_NUMBERS)
    start = timer()
    while game.turn < 30000000:
        game.play_turn()
    print(game.last_number_spoken)
    end = timer()
    print(f'Took {end - start}s to 1M')
