with open('input.txt', 'r') as f:
    raw_data = [line.strip() for line in f.readlines()]


class BoardingPass:
    def __init__(self, instructions):
        self.instructions = instructions
        self.row_instructions, self.column_instructions = instructions[0:7], instructions[7::]

        self.row_max = 127
        self.row_min = 0

        self.column_max = 7
        self.column_min = 0

    def _get_row_position(self, instruction):
        delta = int((self.row_max - self.row_min + 1) / 2)
        if instruction == 'B':
            self.row_min += delta
        elif instruction == 'F':
            self.row_max -= delta
        else:
            print('wat')

    def _get_column_position(self, instruction):
        delta = int((self.column_max - self.column_min + 1) / 2)
        if instruction == 'R':
            self.column_min += delta
        elif instruction == 'L':
            self.column_max -= delta
        else:
            print('wat')

    def get_position(self):
        [self._get_column_position(instruction=i) for i in self.column_instructions]
        [self._get_row_position(instruction=i) for i in self.row_instructions]

        board_number = int(self.row_min*8 + self.column_min)
        return board_number, (self.row_min, self.column_min)


if __name__ == '__main__':
    passengers = [BoardingPass(instructions=data) for data in raw_data]

    board_cards = set()
    rows = set()
    columns = set()

    for passenger in passengers:
        board_id, position = passenger.get_position()
        print(passenger.instructions, position, board_id)
        rows.add(position[0])
        columns.add(position[1])
        board_cards.add(board_id)

    possible_ids = {
        int(row*8 + column) for row in range(min(rows), max(rows)) for column in range(min(columns), max(columns))
    }

    print(f'\nMaximum value is {max(board_cards)}')
    print(f'The only remaining sits are {possible_ids - board_cards}')
