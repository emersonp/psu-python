# Copyright © 2014 Bart Massey
# Display a die roll

from random import *
from tkinter import *
from tkinter.font import Font

class DieRoller(Frame):

  global numdie
  numdie = 1

  def __init__(self, root):
    super().__init__(root)

    # Set up widgets.
    self.grid()
    dieFont = Font(size=20)
    # Display
    self.display = Label(self, width = 1, font = dieFont)
    self.display.grid(row = 0, column = 0, columnspan = 5, sticky = E + W)
    # Roll d4
    self.rolld4 = Button(self, text = "Roll d4", command = self.do_roll_d4)
    self.rolld4.grid(row = 1, column = 0, sticky = E + W)
    # Roll d6
    self.rolld6 = Button(self, text = "Roll d6", command = self.do_roll_d6)
    self.rolld6.grid(row = 1, column = 1, sticky = E + W)
    # Roll d8
    self.rolld8 = Button(self, text = "Roll d8", command = self.do_roll_d8)
    self.rolld8.grid(row = 2, column = 2, sticky = E + W)
    # Roll d10
    self.rolld10 = Button(self, text = "Roll d10", command = self.do_roll_d10)
    self.rolld10.grid(row = 1, column = 3, sticky = E + W)
    # Roll d20
    self.rolld20 = Button(self, text = "Roll d20", command = self.do_roll_d20)
    self.rolld20.grid(row = 1, column = 4, sticky = E + W)

    # Number of Dice
    self.num_lbl = Label(self, text = "Num Dice:")
    self.num_lbl.grid(row = 3, column = 0, sticky = W)

    self.num_display = Label(self, text = numdie)
    self.num_display.grid(row = 3, column = 2, columnspan = 2, sticky = E + W)

    self.bttn_minus_die = Button(self, text = "<<", command = self.do_minus_die)
    self.bttn_minus_die.grid(row = 3, column = 1, sticky = E + W)
    self.bttn_plus_die = Button(self, text = ">>", command = self.do_plus_die)
    self.bttn_plus_die.grid(row = 3, column = 4, sticky = E + W)

    # Quit
    self.quit = Button(self, text = "Quit", command = self.quit)
    self.quit.grid(row = 4, column = 0, columnspan = 5, sticky = E + W)

  def do_roll_d4(self):
    roll = 0
    for x in range(numdie):
      roll += randrange(4) + 1
    self.display.configure(text = str(roll))

  def do_roll_d6(self):
    roll = 0
    for x in range(numdie):
      roll += randrange(6) + 1
    self.display.configure(text = str(roll))

  def do_roll_d8(self):
    roll = 0
    for x in range(numdie):
      roll += randrange(8) + 1
    self.display.configure(text = str(roll))

  def do_roll_d10(self):
    roll = 0
    for x in range(numdie):
      roll += randrange(10) + 1
    self.display.configure(text = str(roll))

  def do_roll_d20(self):
    roll = 0
    for x in range(numdie):
      roll += randrange(20) + 1
    self.display.configure(text = str(roll))

  def do_plus_die(self):
    global numdie
    numdie += 1
    self.num_display.configure(text = numdie)

  def do_minus_die(self):
    global numdie
    numdie -= 1
    if numdie < 1:
      numdie = 1
    self.num_display.configure(text = numdie)

  def quit(self):
    sys.exit()

# Seed the PRNG.
seed()

# Start the app.
root = Tk()
root.title("Die Roller")
root.geometry("360x200")
_ = DieRoller(root)
root.mainloop()
