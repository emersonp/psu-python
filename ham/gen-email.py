# Copyright (c) 2014 Parker Harris Emerson
# Creates a table of spam probability and ham probability.

import random

# Variables
LINES = 273
HAM_CHANCE = .66
HAM_EXCL = .2
SPAM_EXCL = .9
FILE_NAME = "hamtable.txt"

table_file = open(FILE_NAME, "w")

for _ in range(LINES):
  is_ham = random.randrange(1, 101)
  has_excl = random.randrange(1, 101)
  if is_ham <= HAM_CHANCE * 100:
    if has_excl <= HAM_EXCL * 100:
      temp_line = "01"
    else:
      temp_line = "00"
  else:
    if has_excl <= SPAM_EXCL * 100:
      temp_line = "11"
    else:
      temp_line = "10"
  temp_line = temp_line + "\n"
  table_file.write(temp_line)
