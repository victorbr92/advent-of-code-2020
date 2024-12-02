def read():
    with open("input.txt") as f:
        return f.read()

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
    safe_1 = 0
    safe_2 = 0

    for line in text.splitlines():
        line_report = [int(i) for i in line.split()]
        safe_report = check_report(line_report)
        if safe_report:
            print(line_report)
        safe_1 += safe_report
        if safe_report == 0:
            for level in range(len(line_report)):
                modified_line_report = line_report.copy()
                del modified_line_report[level]
                safe_report_2 = check_report(modified_line_report)
                if safe_report_2 > 0:
                    safe_2 += 1
                    break
    print(safe_1)
    print(safe_2 + safe_1)
