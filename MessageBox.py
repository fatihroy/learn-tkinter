from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# different types of message box = showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


window = Tk()
window.title("Create Message Box")

def popup():
    response = messagebox.askquestion("This is my Popup","hello friend") #this is the message box
    # untuk ngecek return nya apa
    Label(window,text=response).pack()
    if response == "yes":
        Label(window,text="you're a good man").pack()
    else:
        Label(window,text="you're a bad man").pack()


# create button
Button(window, text="Popup", command=popup).pack()

window.mainloop()