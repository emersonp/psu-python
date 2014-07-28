# Copyright (c) 2014 Parker Harris Emerson
# Subject to the terms of the MIT License

# Plays the game "Coin War", based on an assignment by Bart Massey for PSU NB

import random

player1_coins = ""
player2_coins = ""
player1_prisoners = ""
player2_prisoners = ""

# Generate Values from Testing Files
TESTING = True

# Pull Values from Testing Files
if TESTING:
  input_file = open("test-8.txt", "r")
  player1_coins = input_file.readline().rstrip()
  player2_coins = input_file.readline().rstrip()
  expected_winner = input_file.readline().rstrip()

# Randomly Generate Values
if not TESTING:
  for i in range(5):
    if random.randrange(2) > 0:
      player1_coins += "H"
    else:
      player1_coins += "T"
  for i in range(5):
    if random.randrange(2) > 0:
      player2_coins += "H"
    else:
      player2_coins += "T"


while len(player1_coins) > 0 and len(player2_coins) > 0:
  print("Player 1 Coins:", player1_coins, "\tP:", player1_prisoners)
  print("Player 2 Coins:", player2_coins, "\tP:", player2_prisoners)
  if player1_coins[0] == player2_coins[0]:
    print("\nRound is a tie!")
    player1_prisoners += player1_coins[0]
    player1_coins = player1_coins[1:]
    if len(player1_coins) > 0:
      player1_prisoners += player1_coins[0]
      player1_coins = player1_coins[1:]
    player2_prisoners += player2_coins[0]
    player2_coins = player2_coins[1:]
    if len(player2_coins) > 0:
      player2_prisoners += player2_coins[0]
      player2_coins = player2_coins[1:]
  elif player2_coins[0] == "H":
    print("\nPlayer 2 wins the Round!")
    player2_coins = player2_coins[1:] + "TH" + player1_prisoners + player2_prisoners
    player1_coins = player1_coins[1:]
    player1_prisoners = ""
    player2_prisoners = ""
  else:
    print("\nPlayer 1 wins the Round!")
    player1_coins = player1_coins[1:] + "TH" + player2_prisoners + player1_prisoners
    player2_coins = player2_coins[1:]
    player1_prisoners = ""
    player2_prisoners = ""

print("Player 1 Coins:", player1_coins, "\tP:", player1_prisoners)
print("Player 2 Coins:", player2_coins, "\tP:", player2_prisoners)
if TESTING and expected_winner == "1":
  print("\nPlayer 1 was expected winner.")
elif TESTING and expected_winner == "2":
  print("\nPlayer 2 was expected winner.")
elif TESTING and expected_winner == "0":
  print("\nExpected winner was a tie.")

if player1_coins > player2_coins:
  print("\nPlayer 1 wins!")
elif player2_coins > player1_coins:
  print("\nPlayer 2 wins!")
else:
  if player1_coins.count("H") > player2_coins.count("H"):
    print("\nPlayer 1 wins with prisoners!")
  elif player1_coins.count("H") < player2_coins.count("H"):
    print("\nPlayer 2 wins with prisoners!")
  else:
    print("\nA tie!")
