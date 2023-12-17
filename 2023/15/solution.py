#!/usr/bin/env python
from collections import OrderedDict, defaultdict
from re import split

with open("input.txt") as f:
    data = [h.strip() for h in f.read().split(",")]


def hash_alg(s):
    i = 0
    for c in s:
        i = (i + ord(c)) * 17 % 256
    return i


# part 1
print(sum((hash_alg(s) for s in data)))

# part 2
boxes = defaultdict(OrderedDict)
for d in data:
    label, operation, count = split("([-=])", d)
    box_id = hash_alg(label)
    if operation == "=":
        boxes[box_id][label] = int(count)
    elif operation == "-":
        boxes[box_id].pop(label, None)


print(
    sum(
        (
            sum(
                (box + 1) * i * focal_len
                for i, focal_len in enumerate(lenses.values(), 1)
            )
            for box, lenses in boxes.items()
        )
    )
)
