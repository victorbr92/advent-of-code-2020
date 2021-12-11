from typing import List, Tuple, Dict

POINTS = {
    ']': 57,
    ')': 3,
    '}': 1197,
    '>': 25137,
}
AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
MATCHES = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

TEST_STR = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


test_data = [e for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [e for e in f.read().splitlines()]


def verify_line(line: str, fix_incomplete=False):
    stack = []

    for i, c in enumerate(line):
        if c in MATCHES.values():
            stack.append(c)
        elif c in MATCHES.keys():
            open_match = MATCHES[c]
            open_available = stack.pop()
            if open_available != open_match:
                return POINTS[c]

    if fix_incomplete:
        inv_map = {v: k for k, v in MATCHES.items()}
        return [inv_map[c] for c in stack[::-1]]

    return 0


def get_error_score(lines: List[str]):
    points = 0
    for line in lines:
        points += verify_line(line)
    return points


def get_autocomplete_score(lines: List[str]):
    points = []
    for line in lines:
        point = 0
        autocomplete = verify_line(line, fix_incomplete=True)
        if isinstance(autocomplete, list):
            for c in autocomplete:
                point *= 5
                point += AUTOCOMPLETE_POINTS[c]
            points.append(point)
    return sorted(points)[len(points)//2]


if __name__ == '__main__':
    print('===== PART1 ======')
    print('> test input')
    # print(verify_line('[[<[([]))<([[{}[[()]]]'))
    print(get_error_score(test_data))
    print('> input')
    print(get_error_score(data))

    print('===== PART2 ======')
    print('> test input')
    print(get_autocomplete_score(test_data))
    print('> input')
    print(get_autocomplete_score(data))
