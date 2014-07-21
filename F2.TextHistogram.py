# Copyright (c) [Redacted]] 2014
# Finds earliest modal number in a sequence.
# Challenge issued by Bart Massey

def text_histogram(sequence):
  assert sequence
  graph_peak = 0
  GRAPH_ASCII = "#" # set to '*' if you want to follow Bart's express character
  # choice; I chose '#' because I prefer the line spacing
  histogram = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

  # fill the histogram; no need to use 'if' since populated with 1..9 sequence
  for index in sequence:
    histogram[index] += 1
    if histogram[index] > graph_peak: # set highest point on graph
      graph_peak = histogram[index]

  # print each row, starting with graph peak and going down to 1
  for row in range(graph_peak, 0, -1):
    print("\t", end="")

    # for each row, print each column, either '*' or ' ' depending
    for column in range(1, 10):
      if histogram[column] >= row:
        print(GRAPH_ASCII, end="")
      else:
        print(" ", end="")
    print("")

  print("\t123456789") # print footer

text_histogram([1,2,3,4,5,4,4,3])
print("" * 3)
text_histogram([1,4,4,7,7,7,7,7,8,8,9,5,6,3,3,4,1,6])
