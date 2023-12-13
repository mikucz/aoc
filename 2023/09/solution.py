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

print(sum(extrapolate(d) for d in data))
