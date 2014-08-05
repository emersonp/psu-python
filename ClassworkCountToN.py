# Copyright (c) 2014 Parker Harris Emerson
# Count To N, in class exercise given by Bart Massey

counter_var = int(input("Please input a positive integer: "))
total_var = 0

for index in range(1, counter_var + 1, 1):
  total_var += index
  print("total_var:", total_var)
  print("index:", index)

print("Grand Total of", counter_var, "+", str(counter_var) + "-1 ... 1:", total_var)
