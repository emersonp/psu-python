def perms(set):
  print("Set:", set)
  if len(set) == 0:
    return [[]]

  result = []

  for each in set:
    print("Result:", result)
    tail = set.difference({each})
    permu_of_tail = perms(tail)
    for permu in permu_of_tail:
      result += [[each] + permu]
  return result

set = {3, 4, 5}

print(perms(set))
# perms(set)
