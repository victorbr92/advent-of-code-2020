from typing import Set
from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod
from rich.layout import Layout
from rich.live import Live
from time import sleep
from rich.console import Console
from itertools import product
from tqdm import tqdm
from functools import lru_cache

console = Console(height=29)

DIRECTIONS = {
    '^': (-1, 0),
    'v': (+1, 0),
    '>': (0, +1),
    '<': (0, -1)
}



def read_input():
    with open("input.txt") as f:
        codes = f.read().splitlines()
    return codes


class Keypad(ABC):

    def __init__(self, row, col, name):
        if not self.is_valid(row, col):
            raise ValueError
        self.row = row
        self.col = col
        self.name = name
        self.fill_index()

    @property
    @abstractmethod
    def keypad(self):
        pass

    def fill_index(self):
        reverse_index = {}
        for row, line in enumerate(self.keypad):
            for col, el in enumerate(line):
                if el:
                    reverse_index[el] = (row, col)
        self.reverse_index = reverse_index
    
    def get_val(self):
        return self.keypad[self.row][self.col]

    def is_valid(self, row, col):
        return (
            0 <= row < len(self.keypad) 
            and 
            0 <= col < len(self.keypad[0])
            and
            self.keypad[row][col] is not None
        )

    def show(self) -> str:
        s = ""
        for i, row in enumerate(self.keypad):
            s += "\n+---+---+---+\n"
            row_content = "| " + " | ".join(self._get_color(cell) if cell is not None else " " for cell in row) + " |"
            s += row_content
        s += "\n+---+---+---+\n"
        return Panel(s, title=self.name)

    def move(self, movement):
        if movement not in DIRECTIONS:
            raise ValueError(f'{self.row, self.col} and to move {movement}')
        dr, dc = DIRECTIONS[movement]
        r, c = self.row, self.col
        if self.is_valid(r+dr, c+dc):
            self.row, self.col = r + dr, c + dc
        else:
            raise KeyError(f"movement not valid {r, c} {movement=}")
 
    def move_to(self, key):
        self.row, self.col = self.reverse_index[key]

    def _get_color(self, cell):
        val = self.get_val()
        if cell == val:
            return f"[green]{cell}[/green]"
        return cell


class NumericKeypad(Keypad):
    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"]
    ]

    def __init__(self, row=3, col=2, name='Numeric Keypad'):
        super().__init__(row, col, name)


class DirectionalKeypad(Keypad):
    keypad = [
        [None, "^", "A"],
        ["<", "v", ">"]
    ]

    def __init__(self, row=0, col=2, name='Directional Keypad'):
        super().__init__(row, col, name)


@lru_cache(maxsize=None)
def find_optimal_paths_to_key(keypad, start_row, start_col, key) -> Set[str]:
    er, ec = keypad.reverse_index[key]
    queue = [(start_row, start_col, [])]
    optimal_moves = set()
    optimal_move_len = None
    visited = set()
    while queue:
        r, c, moves = queue.pop(0)
        moves = ''.join(moves)

        if (r, c) == (er, ec) and moves not in optimal_moves:
            if optimal_move_len is None or len(moves) <= optimal_move_len:
                optimal_move_len = len(moves)
                optimal_moves.add(''.join(moves) + 'A')

        visited.add((r, c))

        for movement, (dr, dc) in DIRECTIONS.items():
            nr, nc = r + dr, c + dc
            if keypad.is_valid(nr, nc) and (nr, nc) not in visited:
                n_moves = moves + movement
                queue.append((nr, nc, n_moves))
    return optimal_moves


def get_possible_optimal_paths(keypad: Keypad, buttons: str):
    all_movements = []
    for key in buttons:
        movements = find_optimal_paths_to_key(keypad, keypad.row, keypad.col, key)
        keypad.move_to(key)
        all_movements.append(movements)

    all_combinations = [''.join(combination) for combination in product(*all_movements)]
    return all_combinations

@lru_cache(maxsize=None)
def recursive_optimal_paths(keypad, moves, depth):
    if depth == 0:
        return moves
    next_keypad = DirectionalKeypad()
    all_moves = set()
    for move in moves:
        next_moves = get_possible_optimal_paths(next_keypad, move)
        min_length = min(len(next_move) for next_move in next_moves)
        optimal_moves = {next_move for next_move in next_moves if len(next_move) == min_length}
        all_moves.update(optimal_moves)
    return recursive_optimal_paths(next_keypad, tuple(all_moves), depth - 1)

if __name__ == "__main__":
    codes = read_input()
    nk1 = NumericKeypad()
    dk1 = DirectionalKeypad()
    dk2 = DirectionalKeypad()

    part1 = 0
    for code in codes:
        moves_1 = get_possible_optimal_paths(nk1, code)

        all_moves_2 = set()
        optimal_move2_len = None
        for moves in moves_1:
            moves_2 = get_possible_optimal_paths(dk1, moves)
            for move_2 in moves_2:
                all_moves_2.add(move_2)
        min_length = min(len(move) for move in all_moves_2)
        moves_2 = [move for move in all_moves_2 if len(move) == min_length]
        
        all_moves_3 = set()
        optimal_move3_len = None
        for moves in moves_2:
            moves_3 = get_possible_optimal_paths(dk2, moves)
            for move_3 in moves_3:
                all_moves_3.add(move_3)
        min_length = min(len(move) for move in all_moves_3)
        moves_3 = [move for move in all_moves_3 if len(move) == min_length]
        num = int(code.rstrip('A'))
        print(f'{code}: {moves_3[0]} | Result: {len(moves_3[0])}*{num}')
        part1 += num * len(moves_3[0])

    
    # SIZE = 26
    # layout = Layout(name='keyboards')
    # layout.split_column(
    #     Layout(Panel('', title="Pressed NK0"),name="Pressed NK0", size=4),
    #     Layout(Panel('', title="Pressed DK1"),name="Pressed DK1", size=4),
    #     Layout(Panel('', title="Pressed DK2"),name="Pressed DK2", size=4),
    #     Layout(Panel('', title="Pressed DK3"),name="Pressed DK3", size=4),
    #     Layout(name="lower", size=12)
    # )
    # layout['lower'].split_row(
    #     Layout(nk1.show(), size=SIZE, name='NK1'),
    #     Layout(dk1.show(), size=SIZE, name='DK1'),
    #     Layout(dk2.show(), size=SIZE, name='DK2'),
    #     Layout(dk2.show(), size=SIZE, name='DK3'),
    # )
    # with Live(layout, console=console, refresh_per_second=2):
    #     total_moves = ''
    #     nk_moves = ''
    #     for m in moves_1[0]:
    #         total_moves += m
    #         dk1.move_to(m)
    #         layout['DK1'].update(dk1.show())
    #         layout['Pressed DK1'].update(Panel(total_moves, title="Pressed DK1"))
    #         sleep(1)
    #         if m != 'A':
    #             nk1.move(m)
    #             layout['NK1'].update(nk1.show())
    #         else:
    #             nk_moves += nk1.get_val()
    #             layout['Pressed NK0'].update(Panel(nk_moves, title='Pressed NK0'))

    print(f"Result of part1: {part1}")
    print('----------------------------')
