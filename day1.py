import math

file = open('day1Input.txt', 'r')


def part_one(f):
    result = 0
    for x in f:
        result += math.floor(int(x) / 3) - 2
    return result


def part_two(f):
    result = 0
    for x in f:
        while int(x) > 0:
            x = math.floor(int(x) / 3) - 2
            if x > 0:
                result += x
    return result


print(part_two(file))
