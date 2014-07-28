# Copyright (c) 2014 Parker Harris Emerson

from tkinter import *

# Create the root window
root = Tk()

# Modify the window
root.title("Coin War")
root.geometry("500x250")

# Create Frame
app = Frame(root)
app.grid()

# Create a Label
lbl = Label(app, text = "I'm a label!")
lbl.grid()

# Create Some Buttons
bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"





# Kick off the window's event loop
root.mainloop()
