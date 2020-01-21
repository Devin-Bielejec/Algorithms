#!/usr/bin/python

import sys
import functools
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

#He can eat 0, 1, 2, 3 cookies at a time

#Recursive
# cache = {"0":1, "1": 1, "2": 2}
# def eating_cookies(amount, cache=cache):
#     if f"{amount}" in cache:
#         return cache[f"{amount}"]
    
#     total = 0
#     for val in range(amount - 1, amount - 4, -1):
#         cache_value = eating_cookies(val, cache=cache)
#         total += cache_value
#         cache[f"{val}"] = cache_value

#     return total

#old iterative
# def eating_cookies(amount, cache=None):
#     queue = [amount]
#     total = 0
#     while queue:
#         current = queue.pop(0)

#         if current == 0:
#             total += 1
#         if current - 3 >= 0:
#             queue.append(current-3)
#         if current - 2 >= 0:
#             queue.append(current-2)
#         if current - 1 >= 0:
#             queue.append(current-1)
#     return total

def eating_cookies(amount, cache=None):
    seq = {"0": 1, "1": 1, "2": 2}
    if amount == 0:
        return seq["0"]
    elif amount == 1:
        return seq["1"]
    elif amount == 2:
        return seq["2"]
    else:
        for i in range(3, amount +1):
            seq[str(i)] = seq[str(i-1)] + seq[str(i-2)] + seq[str(i-3)]  
    
    return seq[str(amount)]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


