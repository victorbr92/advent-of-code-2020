from typing import NamedTuple
import hashlib

REQUIRED_START = '000000'

raw_data = 'iwrupvqb'
test_data_1 = 'abcdef'
test_data_2 = 'pqrstuv'


def lowest_hash_number(key: str) -> int:
    for number in range(100_000_000):
        str_to_hash = f'{key}{number}'
        result = hashlib.md5(str_to_hash.encode()).hexdigest()
        if result.startswith(REQUIRED_START):
            return number
    print('try harder')


if __name__ == '__main__':
    delivered_houses = lowest_hash_number(key=raw_data)
    print(delivered_houses)
