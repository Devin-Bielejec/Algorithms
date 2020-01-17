#!/usr/bin/python

import sys
import copy

#recursive
def rock_paper_scissors(n):
    # Recursive Base Solution
    if n == 0:
        return [[]]
    # Recursive else solution
    sol = []
    prev = rock_paper_scissors(n-1)
    for play in prev:
        sol.append([*play, "rock"])
        sol.append([*play, "paper"])
        sol.append([*play, "scissors"])

    return sol

#iterative
def rock_paper_scissors(n):
    queue = []
    queue.append([])
    while len(queue) > 0:
        current = queue.pop(0)

        if len(current) == n:
            queue.insert(0, current)
            break

        queue.append([*current, "rock"])
        queue.append([*current, "paper"])
        queue.append([*current, "scissors"])
    
    return queue

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
