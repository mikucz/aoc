#!/usr/bin/env python
from itertools import cycle
from re import findall

with open("input.txt") as f:
    moves = list(map(int, f.readline().translate(str.maketrans("LR", "01")).strip()))
    data = {
        el: (left, right)
        for el, left, right in (findall("[A-Z]+", line) for line in f if line.strip())
    }


def steps(start, end):
    choice = data[start]
    for i, move in enumerate(cycle(moves), 1):
        if choice[move] == end:
            return i
        choice = data[choice[move]]

print(steps("AAA", "ZZZ"))
