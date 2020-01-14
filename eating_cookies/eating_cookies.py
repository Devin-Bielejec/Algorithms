#!/usr/bin/python

import sys
import functools
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(amount, denominations=[3, 2, 1], cache=None):

    if amount == 0:
        return 1

    totalPermus = 0

    # Creating an empty list equal to the size of denominations
    currentSolution = ["" for x in range(len(denominations))]

    def helper(amount, denominations):
        nonlocal totalPermus
        nonlocal currentSolution
        currentDenom = denominations[0]

        # Base Case
        if len(denominations) == 1:
            # Check solution is viable, ie no more remainders
            if amount % currentDenom == 0:
                # replace currentSolution at denomination index with correct amount
                currentSolution[len(currentSolution) -
                                len(denominations)] = amount//currentDenom
                print(currentSolution)
                # Permutation logic
                solSum = functools.reduce(lambda a,b: (a if a != "" else 0)+(b if b != "" else 0), currentSolution)
                currentPermus = math.factorial(solSum)
                
                for num in currentSolution:
                    currentPermus = currentPermus // math.factorial(num)

                totalPermus += currentPermus
        # Recursive Case
        else:
            for item in range(amount//currentDenom+1):
                newAmount = amount - item*currentDenom

                # removing the first denomination
                newDenominations = denominations[1:]

                # replace currentSolution at denomination index with correct amount
                currentSolution[len(currentSolution) -
                                len(denominations)] = item
                helper(newAmount, newDenominations)

    helper(amount, denominations=[3, 2, 1])

    if totalPermus == 0:
        return 1
    else:
        return totalPermus


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
