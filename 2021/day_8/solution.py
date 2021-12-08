from typing import List, Tuple, Dict

MAP_NUMBER_SEGMENTS = {
    # n_segment: possible_numbers
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

TEST_STR = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parse_entry(entry: str):
    divided = entry.split(' | ')
    output = divided[1].split(' ')
    signal = divided[0].split(' ')
    return signal, output


test_data = [parse_entry(e) for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [parse_entry(e) for e in f.read().splitlines()]


def decode_output(line: List[str], sorted_signal_pattern: Dict[str, str] = None) -> List[str]:
    decoded = []
    for output in line:
        output_size = len(output)
        if output_size in (2, 3, 4, 7):
            digit = MAP_NUMBER_SEGMENTS[output_size][0]
            decoded.append(str(digit))
        elif output_size not in (2, 3, 4, 7) and sorted_signal_pattern:
            sorted_output = ''.join(sorted(output))
            digit = sorted_signal_pattern.get(sorted_output, 'X')
            decoded.append(str(digit))
    return decoded


def count_digits(lines: List[Tuple[List[str], List[str]]]):
    c = 0
    for line in lines:
        decoded = decode_output(line[1])
        c += len(decoded)
    return c


def get_pattern(line: List[str]) -> Dict[str, str]:
    mapper = dict()
    mapper[1] = [set(output) for output in line if len(output) == 2][0]
    mapper[7] = [set(output) for output in line if len(output) == 3][0]
    mapper[4] = [set(output) for output in line if len(output) == 4][0]
    mapper[8] = [set(output) for output in line if len(output) == 7][0]

    len_5 = [set(output) for output in line if len(output) == 5]
    len_6 = [set(output) for output in line if len(output) == 6]

    for case in len_5:
        if len(mapper[7].intersection(case)) == 3:
            mapper[3] = case
        elif len(mapper[4].intersection(case)) == 3:
            mapper[5] = case
        else:
            mapper[2] = case

    for case in len_6:
        if len(mapper[4].intersection(case)) == 4:
            mapper[9] = case
        elif len(mapper[7].intersection(case)) == 3:
            mapper[0] = case
        else:
            mapper[6] = case

    return {''.join(sorted(mapper[k])): k for k, v in mapper.items()}


def get_output(lines: List[Tuple[List[str], List[str]]]):
    c = 0
    for line in lines:
        sorted_signal_pattern = get_pattern(line[0])
        counter_line = decode_output(line[1], sorted_signal_pattern)
        number = ''.join(counter_line)
        c += int(number)
    return c


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    print(count_digits(test_data))
    print('> input')
    print(count_digits(data))

    print('===== PART2 ======')
    print('> test input')
    print(get_output(test_data))
    print('> input')
    print(get_output(data))