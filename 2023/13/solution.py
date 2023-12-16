#!/usr/bin/env python
import numpy as np

with open("input.txt") as f:
    data = [
        np.array(
            [[c == "#" for c in line] for line in mirror.split("\n")],
            dtype=int,
        )
        for mirror in f.read().strip().split("\n\n")
    ]


def mirror_index(m, smudge=0):
    for i in range(1, m.shape[0]):
        a, b = m[max(0, 2 * i - m.shape[0]) : i], m[i : min(2 * i, m.shape[0])]
        if np.count_nonzero(a != b[::-1]) == smudge:
            return i
    return 0


print(
    sum(
        [
            mirror_index(mirror) * 100 or mirror_index(mirror.transpose())
            for mirror in data
        ]
    )
)
# part 2
print(
    sum(
        [
            mirror_index(mirror, 1) * 100 or mirror_index(mirror.transpose(), 1)
            for mirror in data
        ]
    )
)
