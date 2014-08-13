# Copyright (c) 2014 Justin Blackmon, Parker Harris Emerson, Savannah Naffziger
# Creates and implements a circular queue.

from queuetest import *

class Cirque:
  def __init__(self, size):
    self.queue = [None] * (size + 1)
    self.size = size + 1
    self.add_pointer = 0
    self.remove_pointer = 0
    self.enqueue = self.push
    self.dequeue = self.pop

  def print_queue(self):
    for item in self.queue:
      print(item, end=" ")
    print()

  def bump_pointer(self, pointer):
    if pointer == "add":
      if self.add_pointer < len(self.queue) - 1:
        self.add_pointer += 1
      else:
        self.add_pointer = 0
    elif pointer == "remove":
      if self.remove_pointer < len(self.queue) - 1:
        self.remove_pointer += 1
      else:
        self.remove_pointer = 0
    else:
      print("Pointer movement error.")

  def is_empty(self):
    return self.add_pointer == self.remove_pointer

  def is_full(self):
    if self.is_empty():
      return False
    elif self.add_pointer == self.remove_pointer - 1:
      return True
    elif self.remove_pointer == 0 and self.add_pointer == len(self.queue) - 1:
      return True
    else:
      return False

  def pop(self):
    if self.queue[self.remove_pointer] == None:
      print("Queue is empty.")
    else:
      temp_item = self.queue[self.remove_pointer]
      self.queue[self.remove_pointer] = None
      self.bump_pointer("remove")
      return temp_item

  def push(self, item):
    if self.is_full():
      print("Queue is full.")
    else:
      self.queue[self.add_pointer] = item
      self.bump_pointer("add")

  def where_pointers(self):
    print("Push pointer at index", self.add_pointer)
    print("Pop pointer at index", self.remove_pointer)


if __name__ == "__main__":
  arrayqueuetest(Cirque)
