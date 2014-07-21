import random

tree_tuple = (5, {(0, 1), (0, 2), (2, 3), (2, 4)})
edge_tuples = tree_tuple[1]
DEBUG = True
depth_index = 0

def tree_depth(first_digit):
  global distance
  second_digit = -1
  for tuple in edge_tuples:
    if DEBUG:
      print("Tuple", tuple)
      print("First Digit:", first_digit)
    if tuple[0] == first_digit:
      if DEBUG:
        print("Tuple:", tuple)
      second_digit = tuple[1]
      if [] == [(x,y) for x, y in edge_tuples if x == second_digit]:
        del_tuple = tuple
        if DEBUG:
          print("Edge Tuples:", edge_tuples)
        break
      else:
        distance = tree_depth(second_digit)
  edge_tuples.discard(del_tuple)
  return distance + 1

print("\n\n\n")

while len(edge_tuples) != 0:
  sample_tuple = random.sample(edge_tuples, 1)[0]
  distance = 0
  distance = tree_depth(sample_tuple[0])
  print("Distance:", distance)
  if depth_index < distance:
    depth_index = distance

print("\n\nDepth:", depth_index)
