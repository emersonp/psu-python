# Copyright (c) 2014 Parker Harris Emerson

# Exercise 2.3 from Dawson's "Python Programming for the Absolute Beginner (3d)"

bill = float(raw_input("How much was the bill? $"))

print "15%: $" + str(format(bill * .15, '.2f')) + ", total = $" + str(format(bill * 1.15, '.2f'))
print "20%: $" + str(format(bill * .2, '.2f')) + ", total = $" + str(format(bill * 1.2, '.2f'))
raw_input("\n\nPress the enter key to exit.")
