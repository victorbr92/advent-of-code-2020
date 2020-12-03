from typing import List

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().splitlines()]

INITIAL_SLOPE = (3, 1)
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


class TreeGrid:

    def __init__(self, tree_lines: List[str]):
        self.line_path = tree_lines
        self.line_length = len(self.line_path)
        self.line_size = len(tree_lines[0])

        self.h_position = 0
        self.v_position = 0

    def walk_path(self, h_movement: int, v_movement: int):

        tree_count = 0
        while self.v_position < self.line_length - v_movement:
            tree_count += self.check_tree_line(h_movement, v_movement)

        self.h_position = 0
        self.v_position = 0

        return tree_count

    def check_tree_line(self, h_movement: int, v_movement: int):
        self.h_position += h_movement
        self.v_position += v_movement

        current_line = self.line_path[self.v_position]

        while self.h_position >= self.line_size:
            self.h_position -= self.line_size

        has_tree = current_line[self.h_position] == '#'
        return has_tree


if __name__ == '__main__':
    grid = TreeGrid(tree_lines=lines)

    trees = grid.walk_path(h_movement=INITIAL_SLOPE[0], v_movement=INITIAL_SLOPE[1])
    print(trees)

    product = 1
    for slope in SLOPES:
        trees = grid.walk_path(h_movement=slope[0], v_movement=slope[1])
        product *= trees
    print(product)
