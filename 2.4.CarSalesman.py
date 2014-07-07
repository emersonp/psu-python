# Copyright (c) 2014 Parker Harris Emerson

# Exercise 2.4 from Dawson's "Python Programming for the Absolute Beginner (3d)"

cost = float(raw_input("How much did the car cost? $").replace(',', ''))
print
print("Base Cost:\t\t$") + str(cost)
license = 500
print("License Fee:\t\t$") + str(license)
destination = 100
print("Destination Charge:\t$") + str(destination)
dealer = 115
print("Dealer Prep Charge:\t$") + str(dealer)
print("Total Cost:\t\t$") + str(format(cost + license + destination + dealer, '.2f'))
