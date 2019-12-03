#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if amount == 0:
        return 1
    ways = 0

    def makeChangeRecursive(amount, denominations):
        denominations.sort()
        nonlocal ways
        # Base Case
        currentDenom = denominations[0]
        if len(denominations) == 1:
            if amount % currentDenom == 0:
                ways = ways + 1
            else:
                ways = ways + 0
        # Recursive Case
        else:
            for item in range(amount//currentDenom+1):
                newAmount = amount - item*currentDenom
                # removing the first denomination
                newDenominations = denominations[1:]

                makeChangeRecursive(newAmount, newDenominations)

    makeChangeRecursive(amount, denominations)

    if ways == 0:
        return 1
    else:
        return ways


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
