# Copyright (c) 2014 Parker Emerson

# Exercise 4.1 from Dawson's "Python Programming for the Absolute Beginner (3d)"

import random

correct = False
num_guesses = 0
print ("Guess a number between 1 and 10.")
secret_num = random.randrange(10) + 1

while not correct and num_guesses < 6:
  guess = int(input("Guess: "))
  if guess == secret_num: correct = True
  else: print("Wrong.")
  num_guesses += 1

if correct: print("Congrats!")
else : print("Herp de derp! It was " + str(secret_num))
