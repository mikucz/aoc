#!/usr/bin/env python
from functools import cache

with open("input.txt") as f:
    data = [
        (a, tuple(map(int, b.split(",")))) for a, b in (l.strip().split() for l in f)
    ]


@cache
def arrangements(line, rules):
    n = 0
    if not rules:
        return int("#" not in line)
    elif len(line) < sum(rules) + len(rules) - 1:
        return 0
    if line[0] in ".?":
        n += arrangements(line[1:], rules)
    if (
        line[0] in "#?"
        and len(line) >= rules[0]
        and "." not in line[: rules[0]]
        and (len(line) == rules[0] or line[rules[0]] != "#")
    ):
        n += arrangements(line[rules[0] + 1 :], rules[1:])
    return n


print(sum(arrangements(*d) for d in data))
print(sum(arrangements("?".join([line] * 5), rules * 5) for line, rules in data))
