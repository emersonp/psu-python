# Copyright (c) 2014 Parker Harris Emerson and Kainoa Gaddis
# Block Copy

def block_copy(input_array, i1, j1, i2):
  if j1 == i1:
    return
  if i1 == i2:
    return

  import copy
  array = copy.deepcopy(input_array)

  copy_length = j1 - i1 + 1
  temp_arr = []

  for index in range(i1, j1 + 1):
    temp_arr.append(array[index])

  for index in range(copy_length):
    array[index + i2] = temp_arr[index]

  return array

test_arr = list(range(11))
print(block_copy(test_arr, 1, 4, 7))
#test_arr = list(range(11))
print(block_copy(test_arr, 2, 4, 5))
#test_arr = list(range(11))
print(block_copy(test_arr, 0, 2, 4))
#test_arr = list(range(11))
print(block_copy(test_arr, 1, 1, 5))
#test_arr = list(range(11))
print(block_copy(test_arr, 6, 8, 1))
