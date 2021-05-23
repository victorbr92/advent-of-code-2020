from itertools import groupby

FORBIDDEN_LETTERS = ['i', 'l', 'o']


def is_valid(pwd: str):
    condition_1 = any([check_increasing(pwd[i:i+3]) for i in range(len(pwd) - 2)])
    condition_2 = not any(letter in pwd for letter in FORBIDDEN_LETTERS)
    condition_3 = sum([sum(1 for _ in group) > 1 for label, group in groupby(pwd)]) > 1

    return condition_1 and condition_2 and condition_3


def check_increasing(sequence: str):
    return (ord(sequence[0])+1 == ord(sequence[1])) and (ord(sequence[1])+1 == ord(sequence[2]))


def increment(original: str):
    letter_to_increment = original[-1]
    if letter_to_increment == 'z':
        new_part = increment(original[0:-1])
        pwd = new_part + 'a'
    else:
        pwd = original[0:-1] + chr(ord(letter_to_increment)+1)

    return pwd


if __name__ == '__main__':
    valid = False
    pwd = 'hxbxxyzz'
    print(pwd)

    while not valid:
        pwd = increment(original=pwd)
        valid = is_valid(pwd)
    print(pwd, valid)
