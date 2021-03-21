from typing import List, Dict
from math import gcd

with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

START = int(raw_data[0])
BUSES = [int(bus) for bus in sorted(raw_data[1].split(',')) if bus != 'x']
RAW_BUSES = [bus for bus in raw_data[1].split(',')]


def find_earliest_time(buses: List[int], start_time: int) -> Dict[int, int]:
    earliest = {}
    for bus in buses:
        t = bus - start_time % bus
        if t < 0:
            t = 0
        earliest[bus] = t

    return earliest


def find_earliest_sequential_time(buses: List[str]):
    start_buses = {}
    for i, bus in enumerate(buses):
        if bus != 'x':
            start_buses[int(bus)] = i

    step = 1
    t = 0
    for bus in start_buses:
        while (t + start_buses[bus]) % bus != 0:
            t += step
        step = step * bus // gcd(step, bus)
        print(step, bus)
    return t


if __name__ == '__main__':
    wait_times = find_earliest_time(buses=BUSES, start_time=START)
    bus = min(wait_times, key=wait_times.get)
    print(f'The bus is {bus} and wait time is {wait_times[bus]}. Answer is {wait_times[bus] * bus}')

    time = find_earliest_sequential_time(buses=RAW_BUSES)
    print(f'The earliest time is {time}')
