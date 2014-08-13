import math
import copy

def merge_sort(full_array):
  if len(full_array) > 1:
    mid = len(full_array) // 2
    first_half = full_array[:mid]
    second_half = full_array[mid:]
    print("Full Arr:", full_array)
    print("First Half:", first_half)
    print("Second Half:", second_half)
    merge_sort(first_half)
    merge_sort(second_half)
    merge(first_half, second_half, full_array)

def merge(first_half, second_half, full_array):
  i = 0
  j = 0
  k = 0
  print("Merging:", full_array)
  while i < len(first_half) and j < len(second_half):
    if first_half[i] < second_half[j]:
      full_array[k] = first_half[i]
      i += 1
      print("Not here")
    else:
      full_array[k] = second_half[j]
      j += 1
      #print("Initial Here")
    k += 1
  full_array = full_array[:k]
  if i == len(first_half):
    full_arr += second_half[j:]
    print("Not here")
  else:
    print("Here")
    print("Full_Arr:", full_array)
    print("First Half:", first_half)
    full_array += first_half[i:]
    print("New Full_Arr:", full_array)

test_arr = [8, 2]

merge_sort(test_arr)
print(test_arr)
