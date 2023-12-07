#!/usr/bin/env python
import re

# A, K, Q, J, T -> M, L, K, J, I
translate_table = str.maketrans("AKQJT", "MLKJI")
# in order for regex to work string must be in lexicographic order and
# card with highest value must be first (thats why AKQJT MLKJI remap)
# leave J in same place for part 2
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


# part 1
print(
    sum(
        bid * i
        for i, (_, bid) in enumerate(
            sorted(data, key=lambda d: (points(d[0]), d[0])), start=1
        )
    )
)

# part 2
# find best J variant by replacing it with each card and checking points
# for ties change J to 1
print(
    sum(
        i * bid
        for i, (_, bid) in enumerate(
            sorted(
                data,
                key=lambda d: (
                    max(points(d[0].replace("J", c)) for c in d[0]),
                    d[0].replace("J", "1"),
                ),
            ),
            1,
        )
    )
)
