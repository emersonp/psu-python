import turtle
import random

turtle.colormode(255)

def leg():
  turtle.forward(50)
  turtle.back(100)
  turtle.forward(50)

def rand_color():
  str_color1 = random.randrange(255)
  str_color2 = random.randrange(255)
  str_color3 = random.randrange(255)
  turtle.color(str_color1, str_color2, str_color3)

def circle_check(rand_dir):
  if rand_dir > 150:
    turtle.width(3)
    turtle.circle(50)
    turtle.width(1)


for j in range(15):
  rand_dir = random.randrange(15,180)
  rand_orient = random.randrange(2)
  if rand_orient == 0:
    rand_orient = -1
  for i in range(0, 185 * rand_orient, 5 * rand_orient):
    leg()
    turtle.setheading(i)
    if abs(i) > rand_dir:
      print(rand_dir)
      if rand_dir % 2 == 0:
        turtle.forward(rand_dir / 2)
      else:
        turtle.back(rand_dir / 2)
      rand_color()
      circle_check(rand_dir)
      break


input("Press enter to end.")
