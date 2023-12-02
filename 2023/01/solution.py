#!/usr/bin/env python



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


sum = 0
with open("input.txt") as f:
    for line in f:
        sum += get_num(line)
print(sum)
