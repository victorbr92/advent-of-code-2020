with open('input.txt', 'r') as f:
    raw_data = [line.strip() for line in f.readlines()]


class BoardingPass:
    def __init__(self, instructions):
        self.instructions = instructions
        self.row = self._get_row()
        self.column = self._get_column()

    @property
    def board_number(self) -> int:
        return int(self.row*8 + self.column)

    def _get_column(self) -> int:
        return int(''.join({'R': '1', 'L': '0'}[c] for c in self.instructions[7::]), 2)

    def _get_row(self) -> int:
        return int(''.join({'B': '1', 'F': '0'}[c] for c in self.instructions[0:7]), 2)


if __name__ == '__main__':
    board_cards = set()
    rows = set()
    columns = set()

    for data in raw_data:
        passenger = BoardingPass(instructions=data)
        row, column, board_id = passenger.row, passenger.column, passenger.board_number
        # print(passenger.instructions, row, column)
        rows.add(row)
        columns.add(column)
        board_cards.add(board_id)

    possible_ids = {
        int(row*8 + column) for row in range(min(rows)+1, max(rows)-1) for column in range(min(columns), max(columns))
    }

    print(f'\nMaximum value is {max(board_cards)}')
    print(f'The only remaining sits are {possible_ids - board_cards}')
