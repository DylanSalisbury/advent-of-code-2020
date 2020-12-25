import util

def solve(input_path):
  f = open(input_path)
  player1, player2 = util.parse(f)
  winner_number = util.play_part2_game(player1, player2, 0)
  winner = player1
  if winner_number == 2:
    winner = player2
  return util.score(winner)

if __name__ == '__main__':
    print(solve('input.txt'))