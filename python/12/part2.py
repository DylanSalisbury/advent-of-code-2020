def mysin(angle):
  if angle == 0 or angle == 180:
    return 0
  if angle == 90:
    return 1
  return -1

def solve(input_path):
  f = open(input_path)
  pos = [0, 0]
  waypoint = [10, 1]
  for l in f.readlines():
    ins = l[0]
    arg = int(l[1:])
    print (ins,arg)
    if ins == 'N':
      waypoint[1] += arg
    elif ins == 'S':
      waypoint[1] -= arg
    elif ins == 'W':
      waypoint[0] -= arg
    elif ins == 'E':
      waypoint[0] += arg
    elif ins == 'F':
      pos[0] += arg * waypoint[0]
      pos[1] += arg * waypoint[1]
    elif (ins == 'L' and arg == 90) or (ins == 'R' and arg == 270):
      waypoint = [0 - waypoint[1],waypoint[0]]
    elif (ins == 'R' and arg == 90) or (ins == 'L' and arg == 270):
      waypoint = [waypoint[1],0 - waypoint[0]]
    elif arg == 180 and (ins == 'L' or ins == 'R'):
      waypoint = [0 - waypoint[0], 0 - waypoint[1]]
    else:
      raise AssertionError('Unknown instruction ' + ins + str(arg))
    print(pos, waypoint)
  return abs(pos[0]) + abs(pos[1])

if __name__ == '__main__':
    print(solve('input.txt'))