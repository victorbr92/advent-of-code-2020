import re

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

test_data_1 = 'ugknbfddgicrmopn'
test_data_2 = 'aaa'
test_data_3 = 'jchzalrnumimnmhp'
test_data_4 = 'haegwjzuvuyypxyu'
test_data_5 = 'dvszwmarrgswjxmb'

test_data_6 = 'qjhvhtzxzqqjkmpb'
test_data_7 = 'xxyxx'
test_data_8 = 'uurcxstgmygtbstg'
test_data_9 = 'aabcdefegaa'
test_data_10 = 'ieodomkazucvgmuy'
test_data_11 = 'aabaa'
test_data_12 = 'xyxy'
test_data_13 = 'aaaa'

FORBIDDEN = ['ab', 'cd', 'pq', 'xy']
VOWELS = ['a', 'e', 'i', 'o', 'u']


def is_nice_string(text: str) -> bool:

    before = text[0]
    condition_2 = False
    condition_3 = True

    vowel_counter = int(before in VOWELS)

    for letter in text[1::]:

        if before+letter in FORBIDDEN:
            condition_3 = False

        if letter in VOWELS:
            vowel_counter += 1

        if letter == before:
            condition_2 = True

        before = letter

    condition_1 = vowel_counter >= 3
    return condition_1 and condition_2 and condition_3


RE_PAIR = r'(\w{2}).*\1'
RE_REPEATED = r'(\w).\1'


def is_super_nice_string(text: str) -> bool:
    condition_1 = len(re.findall(pattern=RE_PAIR, string=text)) > 0
    condition_2 = len(re.findall(pattern=RE_REPEATED, string=text)) > 0

    return condition_1 and condition_2


if __name__ == '__main__':
    assert is_nice_string(text=test_data_1) is True
    assert is_nice_string(text=test_data_2) is True
    assert is_nice_string(text=test_data_3) is False
    assert is_nice_string(text=test_data_4) is False
    assert is_nice_string(text=test_data_5) is False

    counter = sum(is_nice_string(text=text) for text in raw_data)
    print(counter)

    assert is_super_nice_string(text=test_data_6) is True
    assert is_super_nice_string(text=test_data_7) is True
    assert is_super_nice_string(text=test_data_8) is False
    assert is_super_nice_string(text=test_data_9) is True
    assert is_super_nice_string(text=test_data_10) is False
    assert is_super_nice_string(text=test_data_11) is True
    assert is_super_nice_string(text=test_data_12) is True
    assert is_super_nice_string(text=test_data_13) is True

    counter = sum(is_super_nice_string(text=text) for text in raw_data)
    print(counter)
