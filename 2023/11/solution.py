#!/usr/bin/env python
import numpy as np

with open("input.txt") as f:
    data = np.array([[s == "#" for s in l.strip()] for l in f], dtype=int)
# List of galaxies is list of all non zero cells
galaxies = list(zip(*np.nonzero(data)))
# empty vectors along both axis
empty_vec = [(data.sum(axis=a) == 0) for a in range(2)]
# accumulated sum of empty space along both axis
s = [np.add.accumulate(vec) for vec in empty_vec]


def solve(n=2):
    return sum(
        [
            abs(bx - ax)
            + abs(s[0][bx] - s[0][ax]) * (n - 1)
            + abs(by - ay)
            + abs(s[1][by] - s[1][ay]) * (n - 1)
            for ay, ax in galaxies
            for by, bx in galaxies
            if (ay, ax) > (by, bx)
        ]
    )


# part 1
print(solve())

# part 2
print(solve(1000000))
