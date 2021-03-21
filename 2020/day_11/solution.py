from typing import List

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

hv_directions = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
dg_directions = [(+1, +1), (-1, -1), (+1, -1), (-1, +1)]


class SeatGrid:
    def __init__(self, initial_state: List[str], leave_threshold: int = 3):
        self.grid = [list(row) for row in initial_state]
        self.max_row = len(self.grid)
        self.max_column = len(self.grid[0])
        self.leave_threshold = leave_threshold

        self.directions = hv_directions + dg_directions

    def update(self):
        changed = 0
        new_seats = []
        for row in range(self.max_row):
            new_row = []
            for column in range(self.max_column):

                seat = self.grid[row][column]
                if seat == 'L' and not self._check_adjacent(sel_row=row, sel_column=column, thresh=0):
                    seat = '#'
                    changed += 1
                elif seat == '#' and self._check_adjacent(sel_row=row, sel_column=column, thresh=self.leave_threshold):
                    seat = 'L'
                    changed += 1

                new_row.append(seat)

            new_seats.append(new_row)

        self.grid = new_seats
        return changed > 0

    def update_new_logic(self):
        changed = 0
        new_seats = []
        for row in range(self.max_row):
            new_row = []
            for column in range(self.max_column):

                seat = self.grid[row][column]

                if seat == 'L' and not self._check_directions(sel_row=row, sel_column=column, thresh=0):
                    seat = '#'
                    changed += 1
                elif seat == '#' and self._check_directions(sel_row=row, sel_column=column, thresh=self.leave_threshold):
                    seat = 'L'
                    changed += 1

                new_row.append(seat)

            new_seats.append(new_row)

        self.grid = new_seats
        return changed > 0

    def count_occupied(self):
        n = 0
        for row in range(self.max_row):
            for column in range(self.max_column):
                if self.grid[row][column] == '#':
                    n += 1
        return n

    def _check_adjacent(self, sel_row: int, sel_column: int, thresh: int):
        n = 0
        for row_inc, column_inc in self.directions:
            row, column = sel_row + row_inc, sel_column + column_inc
            if (0 <= row < self.max_row) and (0 <= column < self.max_column) and (self.grid[row][column] == '#'):
                n += 1

        return n > thresh

    def _check_directions(self, sel_row: int, sel_column: int, thresh: int):
        n = 0

        for row_inc, column_inc in self.directions:
            row = sel_row
            column = sel_column

            row, column = row + row_inc, column + column_inc
            inside_grid = (0 <= row < self.max_row) and (0 <= column < self.max_column)
            while inside_grid:
                if self.grid[row][column] == '#':
                    n += 1
                    break
                elif self.grid[row][column] == 'L':
                    break
                row, column = row + row_inc, column + column_inc
                inside_grid = (0 <= row < self.max_row) and (0 <= column < self.max_column)

        return n > thresh


if __name__ == '__main__':
    seat_grid = SeatGrid(initial_state=raw_data, leave_threshold=3)
    changed = seat_grid.update()

    while changed:
        changed = seat_grid.update()

    print(f'\nThere are {seat_grid.count_occupied()} seats occupied.')

    seat_grid = SeatGrid(initial_state=raw_data, leave_threshold=4)
    changed = seat_grid.update_new_logic()

    while changed:
        changed = seat_grid.update_new_logic()

    print(f'\nThere are {seat_grid.count_occupied()} seats occupied with the new logic.')
