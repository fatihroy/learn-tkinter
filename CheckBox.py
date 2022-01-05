from tkinter import *
from types import TracebackType

window = Tk()
window.title("learn check box")

# show function
def show():
    lbl = Label(window, text=var.get()).pack()

# create checkbox :
var = StringVar()   
# akan tampil ketika klik = onvalue | akan tampil ketika tdk diklik = offvalue                        
check = Checkbutton(window, text="Check this box!!", variable=var, onvalue="On", offvalue="Off")
                                                   
check.deselect() #tidak akan langsung diceklis
check.pack()

# create button
btn = Button(window, text="Show Selection", command=show).pack()

window.mainloop()