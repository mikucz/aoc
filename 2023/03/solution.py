#!/usr/bin/env python
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
