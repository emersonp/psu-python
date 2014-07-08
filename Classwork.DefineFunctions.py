import math

def square(num):
  return num**2

def gauss_sum(num):
  return int((1 + num) * (num / 2))

def euclid_distance(start_x, start_y, end_x, end_y):
  x_distance = start_x - end_x
  y_distance = start_y - end_y
  return math.sqrt(x_distance**2 + y_distance**2)
