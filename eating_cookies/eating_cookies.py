#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(amount, cache=None):
    if amount == 0:
        return 1
    ways = 0
    currentSolution = ["", "", ""]

    def makeCookiesRecursive(amount, denominations):
        nonlocal ways
        nonlocal currentSolution
        # Base Case
        currentDenom = denominations[0]
        if len(denominations) == 1:
            if amount % currentDenom == 0:
                currentSolution[3 - len(denominations)] = amount//currentDenom
                print("current solution", currentSolution)

                # Permutation logic
                ways = ways + 1

        # Recursive Case
        else:
            for item in range(amount//currentDenom+1):
                newAmount = amount - item*currentDenom
                # removing the first denomination
                newDenominations = denominations[1:]
                currentSolution[3 - len(denominations)] = item
                makeCookiesRecursive(newAmount, newDenominations)

    makeCookiesRecursive(amount, denominations=[3, 2, 1])

    if ways == 0:
        return 1
    else:
        return ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


"""
[3, 2, 1]

3

0 0 3
0 1 1
1 0 0

[1, 2, 3]

0 0 1  -1
1 1 0  -2
3 0 0

5

[3, 2, 1]

0 0 5   - 1
0 1 3   - 4   4!/3!
0 2 1   - 3
1 0 2   - 3
1 1 0   - 2

0 2 2 - 4!/2!2!





"""
