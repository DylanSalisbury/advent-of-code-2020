import util

def solve(input_path):
  f = open(input_path)
  player1, player2 = util.parse(f)
  while (player1 and player2):
    util.play_round(player1, player2)
  winner = player1
  if player2:
    winner = player2
  return util.score(winner)

if __name__ == '__main__':
    print(solve('input.txt'))