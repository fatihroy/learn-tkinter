from tkinter import *

window = Tk()
window.title("Learn Dropdown menu")

# create list
options = [
    "monday","tuesday","wednesday","Thursday","friday","saturday"
]

# Create Drop Down Box
clicked = StringVar()
clicked.set(options[4])      #var
option = OptionMenu(window, clicked, *options)
option.pack()

def show():
    lbl = Label(window, text=clicked.get()).pack()

# create button
btn = Button(window, text="Show Selection",command=show).pack()
window.mainloop()

