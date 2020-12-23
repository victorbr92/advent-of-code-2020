from __future__ import annotations
from typing import NamedTuple

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

test_data_1 = '2x3x4'


class Present(NamedTuple):
    l: int
    w: int
    h: int

    @staticmethod
    def parse(dimensions_str: str) -> Present:
        l, w, h = tuple(dimensions_str.split('x'))
        return Present(int(l), int(w), int(h))

    @property
    def wrapping_paper(self):
        side1 = self.l*self.w
        side2 = self.w*self.h
        side3 = self.h*self.l
        return 2*side1 + 2*side2 + 2*side3 + min(side3, side2, side1)

    @property
    def ribbon(self):
        perimeter1 = 2*self.l + 2*self.w
        perimeter2 = 2*self.l + 2*self.h
        perimeter3 = 2*self.h + 2*self.w
        return min(perimeter1, perimeter2, perimeter3) + self.l*self.h*self.w


if __name__ == '__main__':
    assert Present.parse(test_data_1).wrapping_paper == 58
    assert Present.parse(test_data_1).ribbon == 34
    presents = [Present.parse(data) for data in raw_data]
    paper = sum([present.wrapping_paper for present in presents])
    ribbon = sum([present.ribbon for present in presents])
    print(paper, ribbon)


