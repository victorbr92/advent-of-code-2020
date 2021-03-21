from typing import List, Tuple, NamedTuple
from itertools import product

with open('input.txt', 'r') as f:
    raw_data = f.read().split()

DIRECTIONS = [d for d in product((-1, 0, 1), repeat=4) if d != (0, 0, 0, 0)]


class Cube(NamedTuple):
    x: int
    y: int
    z: int = 0
    w: int = 0


class Grid:

    def __init__(self, initial_state: List[str], directions: List[Tuple[int, int, int]] = DIRECTIONS):
        self.active_cubes = {
            Cube(x=x, y=y) for y, r in enumerate(initial_state) for x, item in enumerate(r) if item == '#'
        }
        self.directions = directions
        self.cycle = 0

    def update(self):
        active_new = self.active_cubes.copy()
        range_x, range_y, range_z, range_w = self._get_limits()

        for z in range(range_z[0], range_z[1]):
            for y in range(range_y[0], range_y[1]):
                for x in range(range_x[0], range_x[1]):
                    for w in range(range_w[0], range_w[1]):
                        cube = Cube(x, y, z, w)

                        if cube in self.active_cubes and not self._check_active_adjacent(point=(x, y, z, w), values=[2, 3]):
                            active_new.remove(cube)
                        elif cube not in self.active_cubes and self._check_active_adjacent(point=(x, y, z, w), values=[3]):
                            active_new.add(Cube(x, y, z, w))

        self.active_cubes = active_new
        self.cycle += 1

    def count_active(self):
        return len(self.active_cubes)

    def _get_limits(self):
        x = []
        y = []
        z = []
        w = []
        for cube in self.active_cubes:
            x.append(cube.x)
            y.append(cube.y)
            z.append(cube.z)
            w.append(cube.w)

        return (min(x)-1, max(x)+2), (min(y)-1, max(y)+2), (min(z)-1, max(z)+2), (min(w)-1, max(w)+2)

    def _check_active_adjacent(self, point: Tuple[int, int, int, int], values: List[int]):
        """
        This checks the point for neighbors which are active
        """
        n = 0
        sel_x, sel_y, sel_z, sel_w = point

        for x_inc, y_inc, z_inc, w_inc in self.directions:
            x, y, z, w = sel_x + x_inc, sel_y + y_inc, sel_z + z_inc, sel_w + w_inc
            if Cube(x, y, z, w) in self.active_cubes:
                n += 1

        return n in values


if __name__ == '__main__':
    grid = Grid(raw_data)
    print(grid.active_cubes)
    while grid.cycle < 6:
        grid.update()
        print(grid.count_active())
