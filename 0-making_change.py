#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    check = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while total > 0:
        if coin_index >= n:
            return -1
        if check - sorted_coins[coin_index] >= 0:
            check -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count
