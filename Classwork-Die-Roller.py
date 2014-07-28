# Copyright © 2014 Bart Massey
# Display a die roll

from random import *
from tkinter import *
from tkinter.font import Font

class DieRoller(Frame):

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
    self.rolld8.grid(row = 1, column = 2, sticky = E + W)
    # Roll d10
    self.rolld10 = Button(self, text = "Roll d10", command = self.do_roll_d10)
    self.rolld10.grid(row = 1, column = 3, sticky = E + W)
    # Roll d20
    self.rolld20 = Button(self, text = "Roll d20", command = self.do_roll_d20)
    self.rolld20.grid(row = 1, column = 4, sticky = E + W)

    # Number of Dice
    self.num_lbl = Label(self, text = "Num Dice:")
    self.num_lbl.grid(row = 2, column = 0, sticky = W)



    # Quit
    self.quit = Button(self, text = "Quit", command = self.quit)
    self.quit.grid(row = 3, column = 0, columnspan = 5, sticky = E + W)

  def do_roll_d4(self):
    roll = randrange(4) + 1
    self.display.configure(text = str(roll))

  def do_roll_d6(self):
    roll = randrange(6) + 1
    self.display.configure(text = str(roll))

  def do_roll_d8(self):
    roll = randrange(8) + 1
    self.display.configure(text = str(roll))

  def do_roll_d10(self):
    roll = randrange(10) + 1
    self.display.configure(text = str(roll))

  def do_roll_d20(self):
    roll = randrange(20) + 1
    self.display.configure(text = str(roll))

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
