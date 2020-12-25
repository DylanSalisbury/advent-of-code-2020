"""Helper functions."""

from collections import deque

def play_round(player1, player2):
  winner = player1
  loser = player2
  if player2[0] > player1[0]:
    winner = player2
    loser = player1

  winner.append(winner.popleft())
  winner.append(loser.popleft())

def parse(f):
  player1 = deque()
  player2 = deque()
  next(f)
  while (True):
    l = next(f).rstrip()
    if not l:
      break
    player1.append(int(l))
  next(f)
  for l in f:
    player2.append(int(l))
  return (player1, player2)

def score(winner):
  return sum([(len(winner) - i) * winner[i] for i in range(len(winner))])

part2_cache = dict()

# Returns 1 if player 1 wins, 2 if player 2 wins.
def play_part2_game(player1, player2, recursion_level):
  seen_states = set()
  while (player1 and player2):
    if (recursion_level == 0):
      print('player1: ' + str(player1))
      print('player2: ' + str(player2))
    seen_states_index = ((tuple(player1), tuple(player2)))
    if (seen_states_index) in seen_states:
      print('State was already seen! ' + str(seen_states_index))
      return 1  # Player 1 wins instantly
    seen_states.add(seen_states_index)

    winner = player1
    loser = player2
    if player1[0] >= len(player1)  or player2[0] >= len(player2):
      if player2[0] > player1[0]:
        winner = player2
        loser = player1
    else:
      new1 = deque(list(player1)[1:1+player1[0]])
      new2 = deque(list(player2)[1:1+player2[0]])
      # print('Starting new game.')
      inner_result = None
      if seen_states_index in part2_cache:
        inner_result = part2_cache[seen_states_index]
        print('part2_cache hit: ' + str(inner_result) + ' ' + str(seen_states_index))
      else:
        inner_result = play_part2_game(new1, new2, recursion_level + 1)
        part2_cache[seen_states_index] = inner_result
      # print('Winner of game was player' + str(inner_result))
      if inner_result == 2:
        winner = player2
        loser = player1

    winner.append(winner.popleft())
    winner.append(loser.popleft())

  if player1:
    return 1
  return 2
