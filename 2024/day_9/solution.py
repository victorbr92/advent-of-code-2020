from typing import List

from tqdm import tqdm


def read_input():
    with open("input.txt") as f:
        text = f.read()
        disk = list(map(int, text))
        return disk


def decode_disk(disk: List[int]):
    file_id = 0
    decoded = []
    for i, el in enumerate(disk):
        if i % 2 == 0:
            for i in range(el):
                decoded.append(file_id)
            file_id += 1
        else:
            for i in range(el):
                decoded.append(".")
    return decoded

def rearrange_disk(disk: List[str]):
    numbers = [i for i in disk if i != "."]
    n = len(numbers)
    has_gap = True
    initial_i = 0

    while has_gap and numbers:
        for i, el in enumerate(disk[initial_i:], start=initial_i):
            if el == ".":
                number = numbers.pop(-1)
                disk[i] = number
                break
        else:
            has_gap = False
    return disk[:n]

def rearrange_disk_p2(disk: List[str]):
    last_id = max(int(el) for el in disk if el != ".")

    for file_id in tqdm(range(last_id, -1, -1)):  # Iterate from highest to lowest file ID
        first_file_index = disk.index(file_id)
        last_file_index = len(disk) - 1 - disk[::-1].index(file_id)
        len_id = last_file_index-first_file_index+1

        # print(f"Find place for {file_id}, idx={first_file_index}|{last_file_index}, len={len_id}")

        free_spans = []
        start = None
        for i, el in enumerate(disk):
            if el == ".":
                if start is None:
                    start = i
            else:
                if start is not None:
                    free_spans.append((start, i - 1))
                    start = None
        if start is not None:
            free_spans.append((start, len(disk) - 1))

        for span_start, span_end in free_spans:
            span_length = span_end - span_start + 1
            if span_length >= len_id and span_end < first_file_index:
                # print(f"Found place for {file_id}, idx={span_start}|{span_end}, len={len_id}")
                disk[span_start:span_start + len_id] = [str(file_id)] * len_id
                for i in range(len_id):
                    disk[first_file_index + i] = "."
                # print(f'---{disk}')
                break
        else:
            pass
            # print(f"Will keep {file_id} in same place")

    return disk

def apply_checksum(disk: str):
    total = 0
    i = 0
    for i,el in enumerate(disk):
        if el == ".":
            pass
        else:
            total += i*int(el)
    return total

if __name__ == "__main__":
    part2 = 0

    disk = read_input()

    # decoded = decode_disk(disk)
    # rearranged_disk = rearrange_disk(decoded)
    # part1 = apply_checksum(rearranged_disk)

    # print(f"Result of part1: {part1}")
    # print("---------------------------")

    decoded = decode_disk(disk)
    # print(decoded)
    defrag = rearrange_disk_p2(decoded)
    print(''.join(str(i) for i in defrag))
    part2 = apply_checksum(defrag)
    print(f"Result of part2: {part2}")
