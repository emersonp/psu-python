# Copyright (c) 2014 Parker Harris Emerson

# Exercise 4.3 from Dawson's "Python Programming for the Absolute Beginner (3d)"

import random

coin_flips = 0
heads = 0
tails = 0

while coin_flips < 100:
  flip = random.randrange(2)
  if flip == 0: heads+= 1
  else: tails += 1
  coin_flips += 1

print ("Heads: " + str(heads) + " / Tails: " + str(tails))
