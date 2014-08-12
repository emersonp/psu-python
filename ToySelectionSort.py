FILE_NAME = "selection_sort_input.txt"

file_input = open(FILE_NAME, "r")

unsorted_arr = []

for line in file_input:
  unsorted_arr.append(line.rstrip())

for i in range(0, (len(unsorted_arr) - 1)):
  minimum_val = i
  for j in range(i + 1, len(unsorted_arr)):
    if unsorted_arr[j] < unsorted_arr[minimum_val]:
      minimum_val = j
  temp_val = unsorted_arr[minimum_val]
  unsorted_arr[minimum_val] = unsorted_arr[i]
  unsorted_arr[i] = temp_val

for val in unsorted_arr:
  print(val, end='')

print("\n" * 3)
