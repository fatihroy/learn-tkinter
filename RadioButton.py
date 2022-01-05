from tkinter import *
from types import TracebackType
from PIL import ImageTk, Image

window = Tk()
window.title("Learn How to Create Radio Button")

# membuat command
def clicked(val):
      labelku = Label(window, text=val).pack()

# membuat list untuk opsi
rasa = [
     ("Coklat", "Coklat"),
     ("Vanila", "Vanila"),
     ("Stroberry", "Stroberry"),
     ("Banana", "Banana"),
 ]     #text      #mode

EsKrim = StringVar()
EsKrim.set("Vanilla")

# membuat looping dan radio button
for text, mode in rasa:
     Radiobutton(window, text=text, variable=EsKrim, value=mode).pack(anchor=W)

# membuat perintah untuk langsung menampilkan rasa default
labelku = Label(window, text=EsKrim.get())
labelku.pack()

# membuat button
tombol = Button(window, text="enter", command=lambda:clicked(EsKrim.get())).pack()


window.mainloop()

