import re

REPLACE = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6", 
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def read():
    with open("day_1/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    s = 0
    for line in input.splitlines():
        expression = r'|'.join(k for k in REPLACE) + r'|\d{1}'
        expression = f'?=({expression})'
        digits = re.findall(f'({expression})', line)
        digits = [REPLACE.get(d, d) for d in digits]
        print(digits)
        number = int(digits[0] + digits[-1])
        print(number)
        s += number
    print(s)
import re