# Copyright (c) 2014 Parker Harris Emerson
# Reads a table of spam probability and exclamation point presence and calculates odds of future likelihood of spam.

FILE_NAME = "hamtable.txt"
num_ham = 0
ham_excl = 0
num_spam = 0
spam_excl = 0

file_table = open(FILE_NAME, "r")

for line in file_table:
  if line[0] == "0":
    num_ham += 1
    if line[1] == "1":
      ham_excl += 1
  else:
    num_spam += 1
    if line[1] == "1":
      spam_excl += 1

print("Ham messages:", num_ham)
print("Ham with !:", ham_excl)
print("Frequency of Ham:", format((num_ham / (num_ham + num_spam)), ".2f"))
print("Spam messages:", num_spam)
print("Spam with !:", spam_excl)
print("Frequency of Spam:", format((num_spam / (num_ham + num_spam)), ".2f"))
print()
freq_ham_excl = ham_excl / num_ham
print("Frequency of ! within Ham:", format(freq_ham_excl, ".2f"))
freq_spam_excl = spam_excl / num_spam
print("Frequency of ! within Spam:", format(freq_spam_excl, ".2f"))
print()
prob_spam = spam_excl / (spam_excl + ham_excl)
print("Probability of spam given !:", format(prob_spam, ".2f"))
print()

# Bart-preferred Output
print("\t\t  N\t  E")
print("\tH\t" + str(format(1 - freq_ham_excl, ".2f")) + "\t" + str(format(1 - freq_spam_excl, ".2f"))  )
print("\tS\t" + str(format(freq_ham_excl, ".2f")) + "\t" + str(format(freq_spam_excl, ".2f"))  )
