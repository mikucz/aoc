#!/usr/bin/env python
import math
import re
from collections import defaultdict

max_vals = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def valid_game_id(record):
    """returns game id if game is valid is otherwise 0"""
    game, data = record.split(": ")
    game_id = game.split()[1]
    for count in re.split(",|;", data):
        amount, color = count.split()
        if int(amount) > max_vals[color]:
            return 0
    return int(game_id)


def game_set_pow(record):
    cnt = defaultdict(lambda: 0)
    for count in re.split(",|;", record.split(": ")[1]):
        amount, color = count.split()
        cnt[color] = max(cnt[color], int(amount))
    return math.prod(cnt.values())


with open("input.txt") as f:
    print(sum(valid_game_id(record) for record in f))
    f.seek(0)
    print(sum(game_set_pow(record) for record in f))
