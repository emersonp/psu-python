# Copyright (c) 2014 Parker Harris Emerson

# Exercise 5.2 from Dawson's "Python Programming for the Absolute Beginner (3d)"

# INITIATE PROGRAM

stats = {"POOL" : 30, "STR" : 0, "HEA" : 0, "WIS" : 0, "DEX" : 0}
user_choice = 5
stat_choice = 5


# RUN PROGRAM

while user_choice != 0:
  # PRINT MENU
  print("\n" * 100)
  print(
  """
  #######################################################
  #                                                     #
  #                                                     #
  #                   RPG HERO STATS                    #
  #                                                     #
  #                                                     #
  #######################################################
  """
  )
  print("\n\nSTATS:\n\tStrength:\t", stats["STR"], "\n\tHealth:\t\t", stats["HEA"],
    "\n\tWisdom:\t\t", stats["WIS"], "\n\tDexterity:\t", stats["DEX"])
  print("\n\nWhat would you like to do? (You have", stats["POOL"],
    "points left to spend.)\n\t(0)\tQuit\n\t(1)\tRaise a Stat\n\t(2)\tLower a Stat")

  # GET USER CHOICE
  user_choice = input("\n")
  if not user_choice.isdigit():
    print("Please enter a single numerical digit matching the menu.")
  else:
    user_choice = int(user_choice[0])

  # ADD TO STAT

  if user_choice == 1:
    while True:
      print("\n\n\n\n\nWhich stat would you like to raise? You have", stats["POOL"],
        "points in your pool.")
      print("\t(1) Strength\n\t(2) Health\n\t(3) Wisdom\n\t(4) Dexterity")
      stat_choice = input("\n\n")
      if not stat_choice.isdigit():
        print("Please choose a valid number.")
        continue
      if int(stat_choice) > 4 or int(stat_choice) < 1:
        print("Please choose a valid number.")
        continue
      stat_choice = int(stat_choice)
      stat_value = 100
      while True:
        stat_value = input("\nIncrease it by how much? ")
        if not stat_value.isdigit():
          print("Please enter a numerical value.")
          continue
        stat_value = int(stat_value)
        if stat_value > stats["POOL"]:
          print("You only have", stats["POOL"], "points to spend.\n")
        elif stat_value < 1:
          print("Please pick a positive integer.")
        else:
          stats["POOL"] -= stat_value
          if stat_choice == 1:
            stats["STR"] += stat_value
          elif stat_choice == 2:
            stats["HEA"] += stat_value
          elif stat_choice == 3:
            stats["WIS"] += stat_value
          elif stat_choice == 4:
            stats["DEX"] += stat_value
          break
      break


  # SUBTRACT FROM STAT
  # Not as much input validation as adding.

  if user_choice == 2:
    stat_choice = 5
    while not int(stat_choice) < 5 or int(stat_choice) > 0:
      print("\n\n\n\n\nWhich stat would you like to lower?")
      print("\t(1) Strength\t", stats["STR"], "\n\t(2) Health\t", stats["HEA"],
        "\n\t(3) Wisdom\t", stats["WIS"], "\n\t(4) Dexterity\t", stats["DEX"])
      stat_choice = int(input("\n\n"))
      stat_value = 100
      while stat_value > stats["POOL"]:
        stat_value = int(input("\nIncrease it by how much? "))
        if stat_value > stats["POOL"]:
          print("You only have", stats["POOL"], "points to spend.")
        else:
          stats["POOL"] += stat_value
          if stat_choice == 1:
            #if stat_value
            stats["STR"] -= stat_value
          elif stat_choice == 2:
            stats["HEA"] -= stat_value
          elif stat_choice == 3:
            stats["WIS"] -= stat_value
          elif stat_choice == 4:
            stats["DEX"] -= stat_value
        stat_value = 0
      break
