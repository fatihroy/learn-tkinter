from tkinter import *
import tkinter
from PIL import ImageTk,Image

window = Tk()
window.title("program pindah-pindah gambar")

#menambahkan gambar
gambarku1 = ImageTk.PhotoImage(Image.open("D:\TkInter python\Image\hutan.jpg"))
gambarku2 = ImageTk.PhotoImage(Image.open("D:\TkInter python\Image\PREMAN.jpg"))
gambarku3 = ImageTk.PhotoImage(Image.open("D:\TkInter python\Image\Fatih Di Jalan copy.png"))

#mengatur gambar
Labelku = Label(image=gambarku1) #supaya muncul gambar1 duluan
Labelku.grid(column=0, row=0, columnspan=3) #supaya ditengah
listgambar = [gambarku1, gambarku2, gambarku3]

#membuat status
status = Label(window, text="gambar 1 dari " + str(len(listgambar)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=E+W, pady=15)
#membuat fungsi next dan previous
def nex(no_gambar):
      global Labelku
      global tombol_next
      global tombol_prev
      Labelku.grid_forget()

      Labelku = Label(image=listgambar[no_gambar - 1])
      tombol_next = Button(window, text=">>", command=lambda:nex(no_gambar+1))
      tombol_prev = Button(window, text="<<", command=lambda:back(no_gambar-1))

    #supaya saat gambar terakhir tidak bisa diklik lagi
      if no_gambar == 3:
          tombol_next = Button(window, text=">>", state=DISABLED)

      Labelku.grid(row=0, column=0, columnspan=3)
      tombol_prev.grid(row=1, column=0)
      tombol_next.grid(row=1, column=2)
      
      #update status
      status = Label(window, text="gambar "+str(no_gambar)+" dari " + str(len(listgambar)), bd=1, relief=SUNKEN, anchor=E)
      status.grid(row=2, column=0, columnspan=3, sticky=E+W, pady=15)
     

def back(no_gambar):
    global Labelku
    global tombol_next
    global tombol_prev
    Labelku.grid_forget()
    
    
    Labelku = Label(image=listgambar[no_gambar - 1])
    tombol_next = Button(window, text=">>", command=lambda:nex(no_gambar+1))
    tombol_prev = Button(window, text="<<", command=lambda:back(no_gambar-1))

     #supaya saat gambar terakhir tidak bisa diklik lagi
    if no_gambar == 1:
        tombol_prev = Button(window, text="<<", state=DISABLED)

    Labelku.grid(row=0, column=0, columnspan=3)
    tombol_prev.grid(row=1, column=0)
    tombol_next.grid(row=1, column=2)

  #update status
    status = Label(window, text="gambar "+str(no_gambar)+" dari " + str(len(listgambar)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=E+W, pady=15)




#membuat tombol exit, << dan >> 
tombol_exit = Button(window, text="Exit", command= window.quit)
tombol_prev = Button(window, text="<<", command=back, state=DISABLED)
tombol_next = Button(window, text=">>", command=lambda:nex(2))

tombol_exit.grid(row=1, column=1)
tombol_prev.grid(row=1, column=0)
tombol_next.grid(row=1, column=2)
window.mainloop()