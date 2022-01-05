from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Create Frame")

#Create Frame/bingkai
bingkai = LabelFrame(window, padx=105, pady=105)
bingkai.pack(padx=100, pady=100)

#create button untuk dibingkai
b = Button(bingkai, text="click here!!")
b.grid(row=0, column=0)#tidak akan error kalau pakai frame
b2 = Button(bingkai, text="or here!!")
b2.grid(row=1, column=1)#tidak akan error kalau pakai frame

window.mainloop()