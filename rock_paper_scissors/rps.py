#!/usr/bin/python

import sys
import copy


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    # rock paper scissors
    sol = []
    # Recursive Base Solution
    if n == 1:
        sol.append(["rock"])
        sol.append(["paper"])
        sol.append(["scissors"])
        return sol
    # Recursive else solution
    else:
        prev = rock_paper_scissors(n-1)
        for play in prev:
            for move in ["rock", "paper", "scissors"]:
                copyPlay = copy.copy(play)
                copyPlay.append(move)
                sol.append(copyPlay)

    return sol


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
