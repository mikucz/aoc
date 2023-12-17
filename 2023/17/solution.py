#!/usr/bin/env python
from enum import IntEnum
from heapq import heappop, heappush
from pprint import pprint

with open("input.txt") as f:
    data = [[int(c) for c in line.strip()] for line in f]

h, w = len(data), len(data[0])


Direction = IntEnum("Direction", ["left", "up", "right", "down"], start=0)

move = {
    # (y, x)
    Direction.left: (0, -1),
    Direction.up: (-1, 0),
    Direction.right: (0, 1),
    Direction.down: (1, 0),
}
allowed_direction = {
    # from : allowed directions
    Direction.left: (Direction.up, Direction.down),
    Direction.up: (Direction.left, Direction.right),
    Direction.right: (Direction.up, Direction.down),
    Direction.down: (Direction.left, Direction.right),
}


def find_path(step_max):
    todo, done = [
        (0, 0, 0, Direction.right, step_max),
        (0, 0, 0, Direction.down, step_max),
    ], set()
    while todo:
        heat, y, x, d, steps = heappop(todo)
        y, x, steps = y + move[d][0], x + move[d][1], steps - 1
        if (y, x, d, steps) not in done and 0 <= y < h and 0 <= x < w:
            done.add((y, x, d, steps))
            heat += data[y][x]
            if (y, x) == (h - 1, w - 1):  # exit from map -> lower right corner
                return heat
            if steps:  # continue in same direction
                heappush(todo, (heat, y, x, d, steps))
            for new_d in allowed_direction[d]:  # change direction reset steps
                heappush(todo, (heat, y, x, new_d, step_max))


print(find_path(3))
