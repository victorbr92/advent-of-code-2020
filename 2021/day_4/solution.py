from typing import List, Set

TEST_STR = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class Board:
    def __init__(self, board_lines: List[List[int]]):
        self.rows = board_lines
        self.columns = list(map(list, zip(*board_lines)))
        self.won = False

    def mark_number(self, number: int):
        rows = []
        for row in self.rows:
            row = [0 if x == number else x for x in row]
            rows.append(row)
        self.rows = rows

        columns = []
        for column in self.columns:
            column = [0 if x == number else x for x in column]
            columns.append(column)
        self.columns = columns

        return self.check_won

    @property
    def check_won(self):
        all = set()
        for row in self.rows:
            all |= set(row)
            if sum(row) == 0:
                self.won = True
        for column in self.columns:
            all |= set(column)
            if sum(column) == 0:
                self.won = True

        return sum(all) if self.won else 0

    def __repr__(self):
        s = ''
        for l in self.rows:
            s += '\n'
            s += ' '.join(str(e) for e in l)
        return s


def read_boards(boards_string: List[str]) -> List[Board]:
    b = []
    board_lines = []
    for line in boards_string:
        if line == '':
            b.append(Board(board_lines))
            board_lines = []
        else:
            board_lines.append([int(e) for e in line.split(' ') if e != ''])
    b.append(Board(board_lines))
    return b


test_numbers = [int(e) for e in TEST_STR.splitlines()[0].split(',')]
test_boards = read_boards(TEST_STR.splitlines()[2:])


with open('input.txt', 'r') as f:
    s = f.read().splitlines()
    numbers = [int(e) for e in s[0].split(',')]
    in_boards = read_boards(s[2:])


def play_bingo(number_list: List[int], board_list: List[Board]):
    for n in number_list:
        for p, board in enumerate(board_list):
            winner = board.mark_number(n)
            if winner != 0:
                return winner*n, p


if __name__ == '__main__':
    score, board_n = play_bingo(board_list=test_boards, number_list=test_numbers)
    print(score, board_n)
    del test_boards[board_n]
    while len(test_boards) > 0:
        score, board_n = play_bingo(board_list=test_boards, number_list=test_numbers)
        print(score, board_n)
        del test_boards[board_n]

    print('\n')

    score, board_n = play_bingo(board_list=in_boards, number_list=numbers)
    print(score, board_n)
    del in_boards[board_n]
    while len(in_boards) > 0:
        score, board_n = play_bingo(board_list=in_boards, number_list=numbers)
        print(score, board_n)
        del in_boards[board_n]
