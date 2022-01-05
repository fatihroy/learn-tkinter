from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("menambahkan gambar")

#add images
gambarku = ImageTk.PhotoImage(Image.open("D:\TkInter python\Image\hutan.jpg"))
Label1 = Label(image=gambarku)
Label1.grid(row=0, column=0, columnspan=3)

#create exit button
button_exit = Button(window, text = "exit", command = window.quit)
button_exit.grid(row=1, column=1)

window.mainloop()