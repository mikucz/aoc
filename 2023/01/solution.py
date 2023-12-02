#!/usr/bin/env python

digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def part_1(input):
    d1, d2 = "0", "0"
    for i in input:
        if i.isdigit():
            d1 = i
            break
    for i in reversed(input):
        if i.isdigit():
            d2 = i
            break
    return int(d1 + d2)


def part_2(input):
    def d_1():
        for i in range(len(input)):
            if input[i].isdigit():
                return input[i]
            for v, d in enumerate(digits, 1):
                if input[i:].startswith(d):
                    return str(v)

    def d_2():
        for i in reversed(range(len(input))):
            if input[i].isdigit():
                return input[i]
            for v, d in enumerate(digits, 1):
                if input[:i].endswith(d):
                    return str(v)

    return int(d_1() + d_2())


sum, sum_2 = 0, 0
with open("input.txt") as f:
    for line in f:
        sum += part_1(line)
        sum_2 += part_2(line)
print(sum)
print(sum_2)
