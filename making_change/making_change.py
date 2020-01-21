#!/usr/bin/python

import sys
import random

#Recursive
# def making_change(amount, denominations, cache=None):
#     if amount == 0:
#         return 1
#     if amount < 0:
#         return 0
#     if len(denominations) <= 0:
#         return 0

#     return making_change(amount, denominations[:-1]) + making_change(amount - denominations[-1], denominations)


#Iterative
def making_change(amount, denominations, cache=None):
    combinations = [0] * (amount+1)

    combinations[0] = 1

    for denom in denominations:
        for i in range(1, amount+1):
            if i >= denom:
                combinations[i] += combinations[i - denom]


    return combinations[amount]


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {combos} combos to make {amount} cents.".format(
            combos=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
