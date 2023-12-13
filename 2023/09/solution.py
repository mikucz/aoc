#!/usr/bin/env python
from itertools import pairwise

with open("input.txt") as f:
    data = [list(map(int, line.split())) for line in f]


def extrapolate(data):
    def rec(data):
        sequence = [b - a for a, b in pairwise(data)]
        if any(sequence):
            return sequence[-1] + rec(sequence)
        return 0

    return data[-1] + rec(data)


def extrapolate_backwards(data):
    def rec(data):
        sequence = [b - a for a, b in pairwise(data)]
        if any(sequence):
            return sequence[0] - rec(sequence)
        return 0

    return data[0] - rec(data)


# part 1
print(sum(extrapolate(d) for d in data))
# part 2
print(sum(extrapolate_backwards(d) for d in data))
