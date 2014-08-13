import math
import copy

def merge_sort(full_array):
  if len(full_array) > 0:
    mid = len(full_array) // 2
    first_half = full_array[mid:]
    second_half = full_array[:mid]
    
    merge_sort(first_half)
    merge_sort(second_half)
    merge(first_half, second_half, full_array)

def merge(first_half, second_half, full_arr):
  i = 0
  j = 0
  k = 0
  while i < len(first_half) and j < len(second_half):
    if first_half[i] <= second_half[j]:
      full_arr[k] = first_half[i]
      i += 1
    else:
      full_arr[k] = second_half[j]
      j += 1
    k += 1
  if i == len(first_half):
    full_arr += second_half
  else:
    full_arr += first_half

test_arr = [8, 3, 2, 9, 7, 1, 5, 4]

print(merge_sort(test_arr))
