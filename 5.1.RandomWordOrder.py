# Copyright (c) 2014 Parker Harris Emerson

# Exercise 5.1 from Dawson's "Python Programming for the Absolute Beginner (3d)"

import random

WORDS = ("first", "second", "third", "fourth", "fifth", "sixth")
random_order = []

while len(random_order) < len(WORDS):
  word = random.choice(WORDS)
  if word not in random_order:
    random_order.append(word)

for word in random_order:
  print(word)
