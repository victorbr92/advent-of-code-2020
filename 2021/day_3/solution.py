import pandas as pd

TEST_STR = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
test_data = pd.DataFrame([list(e) for e in TEST_STR.splitlines()])

with open('input.txt', 'r') as f:
    data = pd.DataFrame([list(e) for e in f.read().splitlines()])


def read_report(report: pd.DataFrame):
    gamma_rate_bin = ''.join(report.mode().values.tolist()[0])
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate_bin = gamma_rate_bin.replace('1', '2').replace('0', '1').replace('2', '0')
    epsilon_rate = int(epsilon_rate_bin, 2)
    return gamma_rate, epsilon_rate, gamma_rate * epsilon_rate


def read_crazy_report(report: pd.DataFrame):
    selected_oxygen = report.copy()
    selected_co2 = report.copy()

    for column in report.columns:
        if len(selected_oxygen)> 1:
            mode = selected_oxygen[column].mode()
            most_common = '1' if len(mode) > 1 else mode.iloc[0]
            selected_oxygen = selected_oxygen.loc[selected_oxygen[column] == most_common]

        if len(selected_co2)> 1:
            mode = selected_co2[column].mode()
            most_common = '1' if len(mode) > 1 else mode.iloc[0]
            least_common = '1' if most_common == '0' else '0'
            selected_co2 = selected_co2.loc[selected_co2[column] == least_common]

    oxygen_rate_bin = ''.join(selected_oxygen.iloc[0])
    oxygen_rate = int(oxygen_rate_bin, 2)

    co2_bin = ''.join(selected_co2.iloc[0])
    co2 = int(co2_bin, 2)

    return oxygen_rate, co2, oxygen_rate * co2


if __name__ == '__main__':
    print(read_report(test_data))
    print(read_report(data))

    print(read_crazy_report(test_data))
    print(read_crazy_report(data))
