from collections import Counter

with open('input.txt', 'r') as f:
    raw_data = f.read()

test_data_1 = '(())'
test_data_2 = ')())())'
test_data_3 = '()())'


def get_floor(data: str) -> int:
    counter = Counter(data)
    return counter['('] - counter[')']


def get_basement(data: str) -> int:
    acc = 0
    for pos, char in enumerate(data):
        if char == '(':
            acc += 1
        elif char == ')':
            acc -= 1
        else:
            raise ValueError(char)

        if acc == -1:
            return pos+1


if __name__ == '__main__':
    assert get_floor(test_data_1) == 0
    assert get_floor(test_data_2) == -3
    assert get_basement(test_data_3) == 5
    print(get_floor(raw_data))
    print(get_basement(raw_data))
