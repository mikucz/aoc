#!/usr/bin/env python
import re
from itertools import chain

with open("input.txt") as f:
    data = tuple((line.strip() for line in f))


def rotate(m, i=1):
    return tuple("".join(reversed(l)) for l in zip(*m))


def tilt(m):
    return tuple(
        "".join(chain(*[sorted(chunk) for chunk in re.split(r"(#+)", l)])) for l in m
    )


def load(m):
    return sum([c * i for i, c in enumerate(reversed([l.count("O") for l in m]), 1)])


# part 1
# rotate 1, tilt east, rotate 3 more to return into orig pos, calc load
t = tilt(rotate(data))
for _ in range(3):
    t = rotate(t)
print(load(t))


# part 2
cycles = 1000000000
cache = dict()
head = -1
for cycle in range(cycles):
    if (cached_index := cache.get(data)) is not None:
        head = cached_index
        repeat_count = cycle - head
        break
    cache[data] = cycle
    for _ in range(4):
        data = tilt(rotate(data))

print(
    load(
        next(
            (
                m
                for m, n in cache.items()
                if n - head == (cycles - head) % (cycle - head)
            )
        )
    )
)
