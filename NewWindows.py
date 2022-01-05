import builtins
from tkinter import *
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("old window")

# create command
def open():
    global my_img #supaya bisa menampilkan gambar
    new_window = Toplevel() #create a new window
    my_img = ImageTk.PhotoImage(Image.open("Image/hutan.jpg"))
    imglbl = Label(new_window, image=my_img).pack()
    btn2 = Button(new_window, text="Exit", command=new_window.destroy).pack() #membuat button exit untuk new_window


# create button supaya hanya muncul saat buttonnya diklik
Button(window, text="Open a new window", command=open).pack()



mainloop()