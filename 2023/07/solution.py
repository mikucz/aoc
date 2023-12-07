#!/usr/bin/env python
import re

# A, K, Q, J, T -> H, G, F, E, D
translate_table = str.maketrans("AKQJT", "HGFED")
# in order for regex to work string must be in lexicographic order and
# card with highest value must be first (thats why AKQJT HGFED remap)
types = [
    r"(.)\1{4}",  # five of kind
    r"(.)\1{3}",  # four of kind
    r"(.)\1{2}(.)\2|(.)\3(.)\4{2}",  # full house
    r"(.)\1{2}",  # three of kind
    r"(.)\1{1}(.)\2{1}",  # two pair
    r"(.)\1",  # one pair
    r".",  # high card
]

types = [
    r"(.)\1{4}",
    r"(.)\1{3}",
    r"(.)\1\1(.)\2|(.)\3(.)\4\4",
    r"(.)\1\1",
    r"(.)\1.?(.)\2",
    r"(.)\1",
    ".",
]

with open("input.txt") as f:
    data = [
        (hand.translate(translate_table), int(bid))
        for hand, bid in (line.split() for line in f)
    ]


def points(hand):
    hand = "".join(sorted(hand))
    for i, t in enumerate(types):
        if re.search(t, hand):
            return 6 - i
    return 0


print(
    sum(
        bid * i
        for i, (_, bid) in enumerate(
            sorted(data, key=lambda d: (points(d[0]), d[0])), start=1
        )
    )
)
