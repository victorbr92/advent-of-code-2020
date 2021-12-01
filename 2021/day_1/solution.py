TEST_STR = """199
200
208
210
200
207
240
269
260
263"""
test_data = [int(e) for e in TEST_STR.splitlines()]

with open('input.txt', 'r') as f:
    data = [int(e) for e in f.read().splitlines()]


def evaluate_report(report, window=1):
    ant = sum(report[0:window])
    inc = 0
    for i in range(window+1, len(report)+window):
        n = sum(report[i-window:i])
        if n > ant:
            inc += 1
        ant = n
    return inc


if __name__ == '__main__':
    print(evaluate_report(test_data))
    print(evaluate_report(data))

    print(evaluate_report(test_data, window=3))
    print(evaluate_report(data, window=3))
