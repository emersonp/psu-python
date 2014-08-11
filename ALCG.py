# Copyright (c) 2014 Parker Harris Emerson
# Generates random numbers using ALCG.

s = 12
M = 251
A = 55
B = 47
N = 15

def randnum():
  global s, M, A, N

  r = s % N
  old_s = s
  s = (s * A + B) % M
  return r

def randrange(bound1, bound2 = None):
  global s, A, M

  if bound2 == None:
    lowbound = 0
    highbound = bound1
  else:
    lowbound = bound1
    highbound = bound2

  r = (s % (highbound - lowbound)) + lowbound
  s = (s * A + B) % M

  return r

for _ in range(10):
  print(randnum(), " ", end="", flush=True)
print()

for _ in range(20):
  print(randrange(0, 15), " ", end="", flush=True)
print()
