# Copyright (c) 2014 Parker Harris Emerson

from tkinter import *
import random

class CoinWar(Frame):

  def __init__(self, root):
    super().__init__(root)

    # Set Up Widgets
    self.grid()
    self.player1_coins = ""
    self.player2_coins = ""
    self.player1_prisoners = ""
    self.player2_prisoners = ""
    self.game_play_text = ""

    # Play Button
    self.bttn_play = Button(self, text = "Play", command = self.do_play)
    self.bttn_play.grid(row = 0, column = 0, sticky = E + W)

    # Display Player1 Coins
    self.player1_label = Label(self, text = "Player 1:")
    self.player1_label.grid(row = 0, column = 1, sticky = E)

    self.player1_enter = Entry(self)
    self.player1_enter.grid(row = 0, column = 2, sticky = E + W)

    self.player1_display = Label(self)
    self.player1_display.grid(row = 0, column = 3, sticky = E + W)

    # Display Player1 Coins
    self.player2_label = Label(self, text = "Player 2:")
    self.player2_label.grid(row = 1, column = 1, sticky = E)

    self.player2_enter = Entry(self)
    self.player2_enter.grid(row = 1, column = 2, sticky = E + W)

    self.player2_display = Label(self)
    self.player2_display.grid(row = 1, column = 3, sticky = E + W)

    # Game Display Label
    self.game_display = Label(self, justify = LEFT)
    self.game_display.grid(row = 2, column = 0, columnspan = 8, stick = E + W)

  def do_play(self):
    # Reset Variables
    self.player1_coins = ""
    self.player2_coins = ""
    self.player1_prisoners = ""
    self.player2_prisoners = ""
    self.game_play_text = ""

    # Test Text Entry Boxes for Validity, and If Valid Accept Text
    self.temp_coins = self.player1_enter.get().upper()
    self.temp_coins_count = self.temp_coins.count("H") + self.temp_coins.count("T")
    if self.temp_coins_count >= 5 and len(self.temp_coins) == self.temp_coins_count:
      self.player1_coins = self.temp_coins

    self.temp_coins = self.player2_enter.get().upper()
    self.temp_coins_count = self.temp_coins.count("H") + self.temp_coins.count("T")
    if self.temp_coins_count >= 5 and len(self.temp_coins) == self.temp_coins_count:
      self.player2_coins = self.temp_coin

    # If No Text Entered, Randomly Generate Heads/Tails
    if len(self.player1_coins) == 0:
      for i in range(5):
        if random.randrange(2) > 0:
          self.player1_coins += "H"
        else:
          self.player1_coins += "T"
    if len(self.player2_coins) == 0:
      for i in range(5):
        if random.randrange(2) > 0:
          self.player2_coins += "H"
        else:
          self.player2_coins += "T"

    # Play Game
    while len(self.player1_coins) > 0 and len(self.player2_coins) > 0:
      self.game_play_text += "\nPlayer 1 Coins: " + self.player1_coins +  "\tP: " + self.player1_prisoners
      self.game_play_text += "\nPlayer 2 Coins: " + self.player2_coins +  "\tP: " + self.player2_prisoners

      # If Player First Coins are the Same...
      if self.player1_coins[0] == self.player2_coins[0]:
        self.game_play_text += "\nRound is a tie!"
        self.player1_prisoners += self.player1_coins[0]
        self.player1_coins = self.player1_coins[1:]
        if len(self.player1_coins) > 0:
          self.player1_prisoners += self.player1_coins[0]
          self.player1_coins = self.player1_coins[1:]
        self.player2_prisoners += self.player2_coins[0]
        self.player2_coins = self.player2_coins[1:]
        if len(self.player2_coins) > 0:
          self.player2_prisoners += self.player2_coins[0]
          self.player2_coins = self.player2_coins[1:]

      # Else, If Each Player Has Heads...
      elif self.player2_coins[0] == "H":
        self.game_play_text += "\nPlayer 2 wins the Round!"
        self.player2_coins = self.player2_coins[1:] + "TH" + self.player1_prisoners + self.player2_prisoners
        self.player1_coins = self.player1_coins[1:]
        self.player1_prisoners = ""
        self.player2_prisoners = ""
      else:
        self.game_play_text += "\nPlayer 1 wins the Round!"
        self.player1_coins = self.player1_coins[1:] + "TH" + self.player2_prisoners + self.player1_prisoners
        self.player2_coins = self.player2_coins[1:]
        self.player1_prisoners = ""
        self.player2_prisoners = ""

    # Display Game Text
    self.game_display.configure(text = self.game_play_text)

    # Evaluate For Win Conditions
    self.game_play_text += "\nPlayer 1 Coins: " + self.player1_coins + "\tP:" + self.player1_prisoners
    self.game_play_text += "\nPlayer 2 Coins: " + self.player2_coins + "\tP:" + self.player2_prisoners
    if self.player1_coins > self.player2_coins:
      self.game_play_text += "\nPlayer 1 wins!"
    elif self.player2_coins > self.player1_coins:
      self.game_play_text += "\nPlayer 2 wins!"
    else:
      if self.player1_prisoners.count("H") > self.player2_prisoners.count("H"):
        self.game_play_text += "\nPlayer 1 wins with prisoners!"
      elif self.player1_prisoners.count("H") < self.player2_prisoners.count("H"):
        self.game_play_text += "\nPlayer 2 wins with prisoners!"
      else:
        self.game_play_text += "\nA tie!"
    self.game_display.configure(text = self.game_play_text)


# Kick off the window's event loop
root = Tk()
root.title("Coin War")
root.geometry("700x500")
_ = CoinWar(root)
root.mainloop()
