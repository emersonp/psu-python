# Copyright (c) 2014 Parker Harris Emerson

def switcharoo(array, index1, index2):
  temp = array[index1]
  array[index1] = array[index2]
  array[index2] = temp
  return array

import random


for _ in range(6):
  testarr1 = list(range(random.randrange(6, 16)))
  index1 = random.randrange(len(testarr1))
  index2 = random.randrange(len(testarr1))

  print(switcharoo(testarr1, index1, index2))
