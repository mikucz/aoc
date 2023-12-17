#!/usr/bin/env python

with open("input.txt") as f:
    data = [h.strip() for h in f.read().split(",")]


def hash_alg(s):
    i = 0
    for c in s:
        i = (i + ord(c)) * 17 % 256
    return i

print(sum((hash_alg(s) for s in data)))
