from typing import List, Dict

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()


def count_min_differences(adapters: List[int]):

    diff_counter = {1: 0, 2: 0, 3: 0}

    previous_adapter = adapters[0]
    for pos, adapter in enumerate(adapters[1::]):
        diff = int(adapter - previous_adapter)
        previous_adapter = adapter

        if diff not in diff_counter:
            raise RuntimeError(f'Diff higher than 1,2,3')
        diff_counter[diff] += 1

    return diff_counter


def count_paths(adapters: List[int], position: int = 0, memo: Dict = {}):
    if position == len(adapters) - 1:
        return 1

    if position in memo:
        return memo[position]

    n = 0
    for next_position in range(position+1, min(position+4, len(adapters))):
        if adapters[next_position] - adapters[position] <= 3:
            n += count_paths(adapters=adapters, position=next_position, memo=memo)

    memo[position] = n
    return n


if __name__ == '__main__':

    adapters_output_joltage = [int(line) for line in raw_data]
    adapters_output_joltage.append(0)
    adapters_output_joltage = sorted(adapters_output_joltage)
    device_joltage = max(adapters_output_joltage) + 3
    adapters_output_joltage.append(device_joltage)

    counter = count_min_differences(adapters=adapters_output_joltage)
    print(counter)
    result = counter[1] * counter[3]
    print(result)
    print('-------------')
    paths = count_paths(adapters=sorted(adapters_output_joltage))
    print(paths)


