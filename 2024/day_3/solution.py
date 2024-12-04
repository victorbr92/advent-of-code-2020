import re


def read():
    with open("input.txt") as f:
        return f.read()

PATTERN=r"mul\(\d{1,5},\d{1,5}\)"

def check_report(report):
    last_diff = report[1] - report[0]
    if abs(last_diff) > 3 or abs(last_diff) < 1:
        return 0
    for i in range(len(report[2:])):
        diff = report[i+2] - report[i+1]
        if diff*last_diff < 0 or abs(diff) > 3 or abs(diff) < 1:
            return 0
        last_diff = diff
    return 1

if __name__ == "__main__":
    text = read()
    first_list = []
    second_list = []

    reports = []

    total = 0
    matches = re.findall(PATTERN, text)
    for m in matches:
        numbers = m.lstrip('mul(').rstrip(')').split(',')
        mul = 1
        for number in numbers:
            mul *= int(number)
        total += mul
    print(total)

    total = 0
    sections = re.split(r"(do\(\)|don't\(\))", text)
    consider = True
    for s in sections:
        if s == "don't()":
            consider = False
        elif s == 'do()':
            consider = True
        else:
            if not consider:
                continue
            matches = re.findall(PATTERN, s)
            for m in matches:
                numbers = m.lstrip('mul(').rstrip(')').split(',')
                mul = 1
                for number in numbers:
                    mul *= int(number)
                # print(mul)
                total += mul
        # print(numbers, mul)
    print(total)
