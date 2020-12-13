def mycos(angle):
  if angle == 0:
    return 1
  if angle == 90 or angle == 270:
    return 0
  if angle == 180:
    return -1
  raise AssertionError('Unexpected angle ' + angle)

def mysin(angle):
  if angle == 0 or angle == 180:
    return 0
  if angle == 90:
    return 1
  return -1

def solve(input_path):
  f = open(input_path)
  angle = 0
  pos = [0, 0]
  for l in f.readlines():
    ins = l[0]
    arg = int(l[1:])
    print (ins,arg)
    if ins == 'N':
      pos[1] += arg
    elif ins == 'S':
      pos[1] -= arg
    elif ins == 'W':
      pos[0] -= arg
    elif ins == 'E':
      pos[0] += arg
    elif ins == 'F':
      pos[0] += arg * mycos(angle)
      pos[1] += arg * mysin(angle)
    elif ins == 'L':
      angle = (angle + arg) % 360
    elif ins == 'R':
      angle = (angle - arg) % 360
    else:
      raise AssertionError('Unknown instruction ' + ins)
    print(pos[0], pos[1], angle)
  return abs(pos[0]) + abs(pos[1])

if __name__ == '__main__':
    print(solve('input.txt'))