from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


window = Tk()
window.title("learn open files dialog box")


# membuat fungsi spy tidak langsung membuka folder gambar
def open_image():
    global img
    # membuat program spy membuka folder apa 
    window_filename = filedialog.askopenfilename(initialdir="D:\TkInter python\Image", title="select a file",filetypes=(("semua file","*.*"),("file png", "*.png"),("file jpg","*.jpg")))
                                                                # the directory                                        #yang langsung muncul         #muncul ketika diganti    
    # mereturn alamat file
    my_label = Label(window, text=window_filename).pack()

    # membuat program membuka gambar ketika di open
    img = ImageTk.PhotoImage(Image.open(window_filename))
    imglbl = Label(image= img).pack()         
                                                                                                  


# create button
btn = Button(window, text="open image", command=open_image).pack()
window.mainloop()