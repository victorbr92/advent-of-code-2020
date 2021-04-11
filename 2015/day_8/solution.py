with open('input.txt', 'r') as f:
    raw_data = f.read().splitlines()

test_data = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''.splitlines()

if __name__ == '__main__':
    instructions = {}
    wires = {}

    string_len = 0
    raw_string_len = 0

    for line in raw_data:
        line_replaced = line.encode().decode('unicode_escape')
        string_len += len(line_replaced) - 2
        raw_string_len += len(line)

    print(raw_string_len - string_len)

    string_len = 0
    for line in raw_data:
        string_len += 2+line.count('\\')+line.count('"')

    print(string_len)
