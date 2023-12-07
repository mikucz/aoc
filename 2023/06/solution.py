#!/usr/bin/env python
from math import ceil, floor, prod, sqrt

with open("input.txt") as f:
    data = [l.split(":")[1].strip() for l in f]


# x^2 - tx + d < 0
# delta = t^2 - 4d
# x1,x2 = t +- sqrt(delta) * .5
# use ceil and floor for correct ranges from right directions
def calculate(t, d):
    delta = sqrt(t * t - 4 * d)
    return (ceil((t + delta) / 2) - floor((t - delta) / 2)) - 1


print(prod([calculate(t, d) for t, d in zip(*(map(int, l.split()) for l in data))]))
