#!/usr/bin/env python3

from collections import defaultdict, deque

words = open('input.txt').read().split()

num_players = int(words[0])
last_marble = int(words[6])*100

players = deque(range(1, num_players + 1))

def main():
  scores = defaultdict(int)

  circle = deque()

  current_marble = 0
  circle.append(0)

  for num in range(1, last_marble + 1):
    player_id = get_player()

    if num % 23 == 0:
      scores[player_id] += num

      circle.rotate(7)
      removed = circle.pop()


      scores[player_id] += removed
      circle.rotate(-1)

    else:
      circle.rotate(-1)

      circle.append(num)

    current_marble = circle[-1]

  print('scores', max(scores.values()))

def get_player():
  global players

  current = players[0]
  players.rotate(-1)

  return current

if __name__ == '__main__':
  main()