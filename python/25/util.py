"""Helper functions."""

def transform(initial_value, subject_number, loop_size):
  value = initial_value
  for _ in range(loop_size):
    value = (value * subject_number) % 20201227
  return value

def find_transformations(subject_number, target_value):
  value = 1
  loops = 0
  while (value != target_value):
    loops += 1
    value = (value * subject_number) % 20201227
  return loops

def find_encryption_key(subject_number, public1, public2):
  print(public1, public2)
  loops1 = find_transformations(subject_number, public1)
  loops2 = find_transformations(subject_number, public2)
  print(loops1, loops2)
  result1 = transform(1, public2, loops1)
  result2 = transform(1, public1, loops2)
  print(result1, result2)
  assert result1 == result2, 'different results'
  return result1
