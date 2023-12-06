#!/usr/bin/env python

with open("input.txt") as f:
    seeds = list(map(int, f.readline().split(":")[1].split()))
    maps = [
        [[*map(int, n.split())] for n in i.strip().split("map:\n")[1].split("\n")]
        for i in f.read().split("\n\n")
    ]

location = []
for seed in seeds:
    for map in maps:
        for dst, src, rng in map:
            if src <= seed < src + rng:
                seed = dst + seed - src
                break
    location.append(seed)
print(min(location))
