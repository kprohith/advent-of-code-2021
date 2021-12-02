import csv
import sys


def main():
    joint = get_data()
   # print('Joint:', joint)
    value = find_value()
    value_2 = find_value_2()


def get_data():
    with open('./data.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    # print(data)
    joint = []
    for data in data:
        joint.append(' '.join(data).split(' '))

    return joint


def find_value():
    forward = 0
    depth = 0
    joint = get_data()

    for loc, data in joint:
        if loc == 'forward':
            forward += int(data)
        elif loc == 'up':
            depth -= int(data)
        elif loc == 'down':
            depth += int(data)

    print('Forward:', forward)
    print('Depth:', depth)
    print('Total:', forward * depth)

    return forward * depth

def find_value_2():
    forward = 0
    depth = 0
    aim = 0
    joint = get_data()

    for loc, data in joint:
        if loc == 'forward':
            forward += int(data)
            depth += aim * int(data)
        elif loc == 'up':
            aim -= int(data)
        elif loc == 'down':
            aim += int(data)

    print('Forward:', forward)
    print('Depth:', depth)
    print('Total:', forward * depth)

    return forward * depth

__init__ = main()
