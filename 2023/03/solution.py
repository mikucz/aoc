#!/usr/bin/env python
import math
import re

with open("input.txt") as f:
    data = list(map(str.strip, f))


symbols_coordinates = [
    [m.start() for m in re.finditer("[^0-9.]", line)] for line in data
]


def is_adjecent(y, x_start, x_end):
    y_start, y_end = max(0, y - 1), min(len(symbols_coordinates), y + 2)
    for y in range(y_start, y_end):
        for sym_x in symbols_coordinates[y]:
            if x_start - 1 <= sym_x <= x_end:
                return True
    return False


# part 1
print(
    sum(
        [
            sum(
                [
                    int(m[0])
                    for m in re.finditer("[0-9]+", line)
                    if is_adjecent(y, m.start(), m.end())
                ]
            )
            for y, line in enumerate(data)
        ]
    )
)

gears_coordinates = sum(
    [[(m.start(), y) for m in re.finditer("[*]", line)] for y, line in enumerate(data)],
    [],
)
numbers_coordinates = [
    [(m.start(), m.end(), int(m[0])) for m in re.finditer("[0-9]+", line)]
    for line in data
]


def gear_adjecent_numbers(gear):
    y_start, y_end = max(0, gear[1] - 1), min(len(numbers_coordinates), gear[1] + 2)
    adjecent_nums = []
    for y in range(y_start, y_end):
        for num in numbers_coordinates[y]:
            if num[0] - 1 <= gear[0] <= num[1]:
                adjecent_nums.append(num[2])
    if len(adjecent_nums) < 2:
        return 0
    return math.prod(adjecent_nums)


# part 2
print(sum([gear_adjecent_numbers(gear) for gear in gears_coordinates]))
