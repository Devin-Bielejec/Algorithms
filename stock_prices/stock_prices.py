#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxProfit = prices[1] - prices[0]
  currentMin = prices[0]
  for price in prices[1:]:
    if price < currentMin:
      currentMin = price
    elif price - currentMin > maxProfit:
      maxProfit = price - currentMin
  return maxProfit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print(f"A profit of ${find_max_profit(args.integers)} can be made from the stock prices {args.itegers}.")