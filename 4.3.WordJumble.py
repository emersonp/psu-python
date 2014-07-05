# Copyright (c) 2014 Parker Harris Emerson

# Exercise 4.3 from Dawson's "Python Programming for the Absolute Beginner (3d)"

import random

# Create Variables

WORDS = ("elephant", "timetable", "elegant", "maplethorpe", "infantile")
word = random.choice(WORDS)
correct = word
score = "Gold"
jumble = ""

# Create Jumbled Word

while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

# Start the Game
print(
"""
        Welcome to the Word Jumble

  Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)
guess = input("\nYour guess: ")
while guess != correct and guess != "":
  if guess == "hint":
    score = "Silver"
    if correct == "elephant":
      print("Pachydermergawd! You need a hint?")
    elif correct == "timetable":
      print("Wow, you can't figure it out on my schedule?")
    elif correct == "elegant":
      print("Not a very... dignified solution.")
    elif correct == "maplethorpe":
      print("Robert. That's your hint.")
    elif correct == "infantile":
      print("Like a baby. But not merely childish.")
  else:
    print("Sorry, that's not it.")

  guess = input("Your guess: ")

if guess == correct:
  print("That's it! You guessed it! And you get a", score, "star!\n")

print("Thanks for playing.")
