# Copyright (c) 2014 Parker Harris Emerson
# Exercise 4.3 from Dawson's "Python Programming for the Absolute Beginner (3d)"

# SETUP PROGRAM

import random

WORDS = ("elephant", "timetable", "elegant", "ephemeral", "infantile")
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
word = random.choice(WORDS)
letter_guesses = 0
word_letters = ""
word_not_letters = ""

# GET LETTER GUESSES FROM USER

print("\n" * 4)
print("####################################################")
print("#                                                  #")
print("#                                                  #")
print("#                  WORD GUESSER                    #")
print("#                                                  #")
print("#                                                  #")
print("####################################################")
print()
print("I'm thinking of a secret word. There are", len(word),
  "letters in my secret word.")

while letter_guesses < 5:
  print("Guess a letter! You have", 5 - letter_guesses, "guesses left! ", end="")
  if word_letters != "":
    print("The letter" + (" '" if len(word_letters) < 2 else "s '") + word_letters + ("' is" if len(word_letters) < 2 else "' are"), "in the secret word" +
    (". " if word_not_letters == "" else ","), end="")
  if word_not_letters != "":
      print(("The" if word_letters == "" else " the"), "letter" + (" '" if len(word_not_letters) < 2 else "s '") + word_not_letters +
      ("' is" if len(word_not_letters) < 2 else "' are"), "not" + (" in the secret word. " if word_letters == "" else ". "), end="")
  user_guess = input()
  user_guess = user_guess[0].lower()
  if user_guess in word:
    print("Good guess!", user_guess, "is in the secret word!")
    word_letters += user_guess
    letter_guesses += 1
  elif user_guess not in ALPHABET:
    print("Hey! Only guess letters!")
  else: #user_guess not in word:
    print("Doh!", user_guess, "is not in the secret word!")
    letter_guesses += 1
    word_not_letters += user_guess

# GET WORD GUESS FROM USER

print()
print("Okay! Time to guess the secret word! It has",
  len(word), "letters. ", end="")
word_guess = input()

if word_guess.lower() == word:
  print("Huzzah! You guessed the secret word!")
else:
  print("Wah wah. You didn't guess the secret word!")
