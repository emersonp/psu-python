# Copyright (c) 2014 Naomi Dickerson, Parker Harris Emerson, Steven Huynh
# Based on problem presented by Bart Massey in PSU NB Program

# Package module that allows for the drawing of lines and rectangles in ASCII
# graphics based on user input.

EMPTY = "."
FILL = "#"

def initialize_screen(width, height):
  screen = []
  for row in range(height):
    screen += [[]]
    for column in range(width):
      screen[row] += EMPTY
  return screen


def display_screen(screen):
  for row in reversed(screen):
    for column in row:
      print(column, end="")
    print()

#def draw_line(screen, start_x, start_y, end_x, end_y):


def draw_point(screen, point_x, point_y):
  screen[point_y][point_x] = FILL
  return screen


def draw_rect(screen, start_x, start_y, end_x, end_y, fill = False):
  if start_y > end_y:
    rectangle_count = -1
  else:
    rectangle_count = 1
  for row in range(start_y, end_y + rectangle_count, rectangle_count):
    for column in range(start_x, end_x + 1, 1):
      if row == start_y or row == end_y:
        screen[row][column] = FILL
      else:
        if column == start_x or column == end_x:
          screen[row][column] = FILL
  return screen


#def draw_square(screen, start_x, start_y, length):


#def draw_circ():


frank = initialize_screen(20, 10)
#frank = draw_point(frank, 2, 10)
frank = draw_rect(frank, 2, 2, 7, 7)
display_screen(frank)
