# Copyright (c) Parker Harris Emerson 2014
# Finds earliest modal number in a sequence.
# Challenge issued by Bart Massey

def earliest_modal(sequence):
  assert sequence
  seq_dict = {}
  max_index = 0
  for key in sequence:
    if key in seq_dict:
      seq_dict[key] += 1
    else:
      seq_dict[key] = 1

    if seq_dict[key] > max_index:
      max_index = seq_dict[key]

  for key in sequence:
    if max_index == seq_dict[key]:
      return key

print(5 == earliest_modal([1, 5, 7, 3, 3, 7, 5]))
print(3 == earliest_modal([1, 3, 3, 4, 4, 5, 5, 3, 1]))
print(2 == earliest_modal([1, 2, 3, 4, 5, 6, 2]))
