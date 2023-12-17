#!/usr/bin/env python
import sys
from enum import IntEnum

with open("input.txt") as f:
    data = [l.strip() for l in f]
energized = [[0 for _ in l] for l in data]

Direction = IntEnum("Direction", ["left", "up", "right", "down"])

next_direction = {
    # \
    (Direction.left, "\\"): (Direction.up,),
    (Direction.up, "\\"): (Direction.left,),
    (Direction.right, "\\"): (Direction.down,),
    (Direction.down, "\\"): (Direction.right,),
    # /
    (Direction.left, "/"): (Direction.down,),
    (Direction.up, "/"): (Direction.right,),
    (Direction.right, "/"): (Direction.up,),
    (Direction.down, "/"): (Direction.left,),
    # .
    (Direction.left, "."): (Direction.left,),
    (Direction.up, "."): (Direction.up,),
    (Direction.right, "."): (Direction.right,),
    (Direction.down, "."): (Direction.down,),
    # |
    (Direction.left, "|"): (Direction.up, Direction.down),
    (Direction.up, "|"): (Direction.up,),
    (Direction.right, "|"): (Direction.up, Direction.down),
    (Direction.down, "|"): (Direction.down,),
    # -
    (Direction.left, "-"): (Direction.left,),
    (Direction.up, "-"): (Direction.left, Direction.right),
    (Direction.right, "-"): (Direction.right,),
    (Direction.down, "-"): (Direction.left, Direction.right),
}
move = {
    Direction.left: (0, -1),
    Direction.up: (-1, 0),
    Direction.right: (0, 1),
    Direction.down: (1, 0),
}

max_y, max_x = len(data), len(data[0])

cnt = 0

loops = set()


sys.setrecursionlimit(3000)


def trace_beam(direction: Direction, y, x):
    tile = data[y][x]
    energized[y][x] = 1
    if (direction, y, x) in loops:
        return
    loops.add((direction, y, x))
    for d in next_direction[(direction, tile)]:
        ny, nx = y + move[d][0], x + move[d][1]
        if not 0 <= ny < max_y or not 0 <= nx < max_x:
            continue
        trace_beam(d, ny, nx)


trace_beam(Direction.right, 0, 0)
print(sum(sum(l) for l in energized))
