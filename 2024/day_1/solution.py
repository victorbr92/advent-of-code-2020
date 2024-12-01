from collections import Counter

def read():
    with open("day_1/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    first_list = []
    second_list = []
    for line in input.splitlines():
        results = line.split('   ')
        print(results)
        first_list.append(int(results[0]))
        second_list.append(int(results[1]))
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    total = 0
    for n1, n2 in zip(first_list, second_list):
        total += abs(n1-n2)
    print(total)

    counter_second = Counter(second_list)
    similarity_score = 0
    for n1 in first_list:
        appeared = counter_second[n1]
        similarity_score += n1*appeared
    print(similarity_score)
