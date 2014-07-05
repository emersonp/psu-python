# Copyright (c) 2014 Parker Harris Emerson

# Exercise 4.1 from Dawson's "Python Programming for the Absolute Beginner (3d)"

low_num = int(input("Start counting at what number? "))
high_num = int(input("Start counting at what number? "))

for index in range (low_num, high_num + 1, 1):
  print(index)
