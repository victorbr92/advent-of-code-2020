from typing import List
import math
from collections import defaultdict


def part_1() -> int:
    number = 0
    gifts = 0
    while gifts < 29_000_000:
        number += 1
        divisors = get_divisors(n=number)
        gifts = sum(divisors)*10
    print(gifts)
    print(number)


def part_2():
    number = 0
    gifts = 0
    while gifts <= 29_000_000:
        number += 1
        divisors = get_divisors(number)
        gifts = sum(d for d in divisors if number / d <= 50) * 11
    print(gifts)
    print(number)


def get_divisors(n: int) -> List[int]:
    # credits to https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    divs.append(n)
    return set(divs)


if __name__ == '__main__':
    part_1()
    part_2()

