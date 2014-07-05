# Copyright (c) 2014 [Redacted]

# Exercise 4.2 from Dawson's "Python Programming for the Absolute Beginner (3d)"

phrase = input("Enter a phrase to reverse: ")

for letter in range(len(phrase) - 1, -1, -1):
  print(phrase[letter], end="")

print()
