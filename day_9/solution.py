from typing import List

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def check_next(preamble: List[int], next_number: int):
    possible_values = set()

    for i in range(0, len(preamble)):
        temp = next_number - preamble[i]

        if temp in possible_values:
            return True

        possible_values.add(preamble[i])
    else:
        return False


def move_sequence(sequence: List[int], n_sequence: int):
    preamble = sequence[0:n_sequence]
    remaining = sequence[n_sequence::]
    position = n_sequence

    for p, next_value in enumerate(remaining):
        valid = check_next(preamble=preamble, next_number=next_value)
        if not valid:
            print(f'Sum not valid: sum({preamble}) = {next_value}')
            return position + p
        preamble.pop(0)
        preamble.append(next_value)
        print(f'> Adding {next_value}')


def find_contiguous_sum(sequence_to_check: List[int], value: int):

    for initial in range(0, len(sequence_to_check)):
        for final in range(1, len(sequence_to_check)):
            values = sequence_to_check[initial:final]
            s = sum(values)
            if s > value:
                break

            if sum(values) == value:
                print(f'Found that sum({values}) = {value}')
                return max(values) + min(values)


if __name__ == '__main__':

    all_sequences = [int(line) for line in raw_data]
    position = move_sequence(sequence=all_sequences, n_sequence=25)

    sequence_to_check = all_sequences[0:position][::-1]
    desired_value = all_sequences[position]

    result = find_contiguous_sum(sequence_to_check=sequence_to_check, value=desired_value)
    print(result)
