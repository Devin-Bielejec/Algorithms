#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


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
def knapsack_solver(items, capacity):
    print(items)
    combinations = [0] * (len(capacity)+1)
    combinations[0] = 0

    for item in items:
        for i in range(1, amount+1):
            if i >= denom:
                combinations[i] += combinations[i - denom]


    return combinations[amount]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
