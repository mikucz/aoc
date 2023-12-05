#!/usr/bin/env python
from collections import defaultdict


def parse_card(input):
    card, nums = input.split(":")
    nums = nums.split("|")
    card = int(card.split()[1])
    winning = set(map(int, nums[0].split()))
    owned = set(map(int, nums[1].split()))
    return card, winning, owned


def count_points(winning, owned):
    win = len(winning.intersection(owned))
    if win:
        return 1 * 2 ** (win - 1)
    return 0


def count_cards(card, winning, owned, cards_cnt):
    matches = len(winning.intersection(owned))
    cards_cnt[card] += 1
    if not matches:
        return
    for i in range(1, matches + 1):
        if cards_cnt[card] > 1:
            cards_cnt[card + i] += cards_cnt[card]
        else:
            cards_cnt[card + i] += 1


sum_1, sum_2 = 0, 0
with open("input.txt") as f:
    for line in f:
        sum_1 += count_points(*parse_card(line)[1:])

with open("input.txt") as f:
    cards_cnt = defaultdict(int)
    for line in f:
        count_cards(*parse_card(line), cards_cnt)
    sum_2 = sum(cards_cnt.values())

print(sum_1)
print(sum_2)
