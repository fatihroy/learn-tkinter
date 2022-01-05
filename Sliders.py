from tkinter import *

window = Tk()
window.title("learn slider")
# create  size of window
window.geometry("400x400")

# create sliders
geser_vertikal = Scale(window, from_=0, to=400)
geser_vertikal.pack()

geser_horizontal = Scale(window, from_=0, to=400, orient=HORIZONTAL)
geser_horizontal.pack()

# sliders function
def resize():
    lbl = Label(window, text=geser_horizontal.get()).pack()
    window.geometry(str(geser_horizontal.get()) + "x" + str(geser_vertikal.get()))

btn = Button(window, text="click", command=resize).pack()

window.mainloop()