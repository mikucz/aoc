#!/usr/bin/env python

with open("input.txt") as f:
    data = f.readlines()
start = next((l.index("S"), i) for i, l in enumerate(data) if "S" in l)


# 0,1,2,3 -> left, up, right, down
# if direction is 0 (left) and tile is 'L' next direction will be :
# direction[0].index('L') = 1 (up)
# '_' for space indexing only
direction = [
    "-L_F",
    "7|F_",
    "_J-7",
    "J_L|",
]
move_x_map = {0: -1, 1: 0, 2: 1, 3: 0}
move_y_map = {0: 0, 1: -1, 2: 0, 3: 1}


p, cnt, d, d_start = start, 0, 0, 0
while p != start or cnt == 0:
    "if beginning direction not found -> start with new direction"
    if d == -1:
        p, cnt, d, d_start = start, 0, d_start + 1, d_start + 1
    p = (p[0] + move_x_map[d], p[1] + move_y_map[d])
    d = direction[d].find(data[p[1]][p[0]])
    cnt += 1

print(cnt // 2)
