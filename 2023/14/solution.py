#!/usr/bin/env python
import re
from itertools import chain

with open("input.txt") as f:
    data = [line.strip() for line in f]

transposed = ["".join(l) for l in zip(*data)]

for i in range(len(transposed)):
    transposed[i] = "".join(
        chain(*[reversed(sorted(chunk)) for chunk in re.split(r"(#+)", transposed[i])])
    )

counts = [l.count("O") for l in zip(*transposed)]
print(sum([c * i for i, c in enumerate(reversed(counts), 1)]))
