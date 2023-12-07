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
# print(min(location))


# part 2
seed_ranges = zip(seeds[::2], seeds[1::2])

remain = set(seed_ranges)
done = set()
for map in maps:
    remain, done = done.union(remain), set()
    for dst, src, rng in map:
        for s, r in [(s, r) for s, r, in remain if s + r > src and s < src + rng]:
            remain.remove((s, r))
            if s < src:
                remain.add((s, src - s))
            if s + r > src + rng:
                remain.add((src + rng, s + r - src - rng))
            done.add((dst + max(s - src, 0), min(s + r, src + rng) - max(src, s)))

print(min(remain | done)[0])
