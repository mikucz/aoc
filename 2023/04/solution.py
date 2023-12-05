#!/usr/bin/env python
def parse_card(input):
    nums = line.split(":")[1].split("|")
    winning = set(map(int, nums[0].split()))
    owned = set(map(int, nums[1].split()))
    return winning, owned


def count_points(winning, owned):
    win = len(winning.intersection(owned))
    if win:
        return 1 * 2 ** (win - 1)
    return 0


sum = 0
with open("input.txt") as f:
    for line in f:
        sum += count_points(*parse_card(line))

print(sum)
