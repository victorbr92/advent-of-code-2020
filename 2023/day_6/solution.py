import re


def read():
    with open("day_6/input.txt") as f:
        input = f.read()
    return input

if __name__ == "__main__":
    input = read()
    print('PART 1')
    time = [int(i) for i in re.findall(r'\d+', input.splitlines()[0])]
    distance = [int(i) for i in re.findall(r'\d+', input.splitlines()[1])]
    part_1 = 1
    for race in zip(time, distance):
        win = 0
        for hold in range(1, race[0]):
            speed = hold
            time_left = race[0]-hold
            my_distance = speed*time_left
            if my_distance > race[1]:
                win+=1
        part_1*=win
    print(part_1)
    print('PART 2')
    time = int(''.join([i for i in re.findall(r'\d+', input.splitlines()[0])]))
    distance = int(''.join([i for i in re.findall(r'\d+', input.splitlines()[1])]))
    part_2 = 0
    for hold in range(time):
        speed = hold
        time_left = time-hold
        my_distance = speed*time_left
        if my_distance > distance:
            part_2+=1
    print(part_2)
