from itertools import groupby

input_data = 1321131112
test_data = 1
REPETITIONS = 50


def transform_input(number: str):
    counter_list = groupby(number)
    modified_number = ''.join(f'{len(list(counter[1]))}{counter[0]}' for counter in counter_list)

    return modified_number


if __name__ == '__main__':
    new_number = transform_input(str(input_data))
    for i in range(REPETITIONS):
        print(i, len(new_number))
        new_number = transform_input(new_number)
