#!/usr/bin/env python3

from collections import defaultdict, deque

words = open('input.txt').read().split()

num_players = int(words[0])
last_marble = int(words[6])

players = deque(range(1, num_players + 1))

def main():
  get_score(last_marble)
  get_score(last_marble * 100)

def get_score(num_marbes):
  scores = defaultdict(int)

  circle = deque()
  circle.append(0)

  for num in range(1, num_marbes + 1):
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

  print('max score for', num_marbes, 'marbles and', num_players, 'players =', max(scores.values()))

def get_player():
  global players

  current = players[0]
  players.rotate(-1)

  return current

if __name__ == '__main__':
  main()