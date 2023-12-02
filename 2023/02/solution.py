#!/usr/bin/env python
import re

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


with open("input.txt") as f:
    print(sum(valid_game_id(record) for record in l))
