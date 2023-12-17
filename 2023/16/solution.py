#!/usr/bin/env python
from enum import IntEnum

with open("input.txt") as f:
    data = [line.strip() for line in f]
a = [[c for c in l] for l in data]
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

h, w = len(data), len(data[0])


def trace_beams(d: Direction, y, x):
    beams, visited_tiles = {(y, x, d)}, set()
    while beams:
        yo, xo, d = beams.pop()
        y, x = yo + move[d][0], xo + move[d][1]
        if (y, x, d) not in visited_tiles and 0 <= y < h and 0 <= x < w:
            visited_tiles.add((y, x, d))
            for next_d in next_direction[(d, data[y][x])]:
                beams.add((y, x, next_d))
    return len({(y, x) for y, x, _ in visited_tiles})


# part 1
print(trace_beams(Direction.right, 0, -1))

# part 2
print(
    max(
        max(
            max(trace_beams(Direction.right, i, -1), trace_beams(Direction.left, i, w))
            for i in range(h)  # find mix in beam for each row
        ),
        max(
            max(
                trace_beams(Direction.down, -1, i),
                trace_beams(Direction.up, h, i),
            )
            for i in range(w)  # find mix in beam for each col
        ),
    )
)
