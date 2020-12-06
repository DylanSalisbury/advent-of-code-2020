import util

def solve(input_path):
  result = 0

  f = open(input_path)

  while (True):
    record_lines = []
    l = ''
    while (True):
      l = f.readline()
      if not l or not l.rstrip():
        break
      record_lines.append(l)
      record_text = ''.join(record_lines)
      record_text = record_text.rstrip()
    print('>', record_text, '<')
    sets = util.group_to_set(record_text, True)
    result = result + len(sets)
    if not l:
      break
  return result

if __name__ == '__main__':
    print(solve('input.txt'))