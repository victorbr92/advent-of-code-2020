
input_data = 1321131112
test_data = 1
REPETITIONS = 40


class NumberReader:

    def __init__(self, digit: str):
        self.digit = digit
        self.repeat = 1


def transform_input(number: int):
    counter_list = create_counter(number=number)
    modified_number = ''

    for counter in counter_list:
        modified_number += f'{counter.repeat}{counter.digit}'

    return int(modified_number)


def create_counter(number: int):
    position = 0
    element = str(number)[position]
    counters = [NumberReader(digit=element)]

    while position < len(str(number)) - 1:
        position += 1
        element = str(number)[position]
        if element == counters[-1].digit:
            counters[-1].repeat += 1
        else:
            counters.append(NumberReader(digit=element))

    return counters


if __name__ == '__main__':
    new_number = transform_input(input_data)
    for i in range(REPETITIONS):
        print(i, len(str(new_number)))
        new_number = transform_input(new_number)
