# Copyright (c) 2014 Parker Harris Emerson
# Celsius to Fahrenheit, in class exercise given by Bart Massey

# Gather Choice
print("Hello! This program converts from either Celsius to Fahrenheit, or Fahrenheit to Celsius.")
user_input = input("Would you temperature would you like to convert? (e.g., 32F, 100C, 211C) ")
degree = int(user_input[:-1])
convention = user_input[-1]

# Calculate Degrees
if convention.upper() == "C":
  output = int(round((9 * degree) / 5 + 32))
  output_convention = "Celsius"
elif convention.upper() == "F":
  output = int(round((degree - 32) * 5 / 9))
  output_convention = "Fahrenheit"
else:
  print("Please use proper convention.")
  quit()

# Return Output

print("The temperature in", output_convention, "is", output, "degrees.")
