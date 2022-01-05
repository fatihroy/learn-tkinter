from tkinter import *
window = Tk()

#bikin judul di GUI
window.title("kalkulator simpel")

#bikin inputfield
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3, padx=10, pady=15)

#fungsi untuk menampilkan angka ketika diklik
def button_click(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

#fungsi clear
def clear():
    e.delete(0,END)
    return
#fungsi tambah, kurang, kali, bagi
def tambah():
    global tipe
    tipe = "pertambahan"
    global num1
    num1 = int(e.get())
    e.delete(0, END)

def kurang():
    global tipe
    tipe = "pengurangan"
    global num1
    num1 = int(e.get())
    e.delete(0, END)

def kali():
    global tipe
    tipe = "perkalian"
    global num1
    num1 = int(e.get())
    e.delete(0, END)

def bagi():
    global tipe
    tipe = "pembagian"
    global num1
    num1 = int(e.get())
    e.delete(0, END)

#fungsi hasil
def hasil():
    if tipe == "perkalian":
        Angka1 = num1
        Angka2 = int(e.get())
        hasil = Angka1*Angka2
        e.delete(0, END)
        e.insert(0, hasil)

    elif tipe == "pembagian":
        Angka1 = num1
        Angka2 = int(e.get())
        hasil = Angka1/Angka2
        e.delete(0, END)
        e.insert(0, hasil)

    elif tipe == "pertambahan":
        Angka1 = num1
        Angka2 = int(e.get())
        hasil = Angka1+Angka2
        e.delete(0, END)
        e.insert(0, hasil)

    elif tipe == "pengurangan":
        Angka1 = num1
        Angka2 = int(e.get())
        hasil = Angka1-Angka2
        e.delete(0, END)
        e.insert(0, hasil)

#bikin tombol angka
button_1 = Button(window, text="1", padx=35, pady=35,command=lambda:button_click(1))
button_2 = Button(window, text="2", padx=35, pady=35,command=lambda:button_click(2))
button_3 = Button(window, text="3", padx=35, pady=35,command=lambda:button_click(3))
button_4 = Button(window, text="4", padx=35, pady=35,command=lambda:button_click(4))
button_5 = Button(window, text="5", padx=35, pady=35,command=lambda:button_click(5))
button_6 = Button(window, text="6", padx=35, pady=35,command=lambda:button_click(6))
button_7 = Button(window, text="7", padx=35, pady=35,command=lambda:button_click(7))
button_8 = Button(window, text="8", padx=35, pady=35,command=lambda:button_click(8))
button_9 = Button(window, text="9", padx=35, pady=35,command=lambda:button_click(9))
button_0 = Button(window, text="0", padx=35, pady=35,command=lambda:button_click(0))

#bikin tombol =, clear
button_clear = Button(window, text="clear", padx=68,pady=35,command=clear)
button_equal = Button(window, text="=", padx=76.4, pady=35,command=hasil)

#bikin tombol +, -, :, x
button_plus = Button(window, text="+", padx=34, pady=35,command=tambah)
button_multiply = Button(window, text="x", padx=35, pady=35,command=kali)
button_divide = Button(window, text=":", padx=35, pady=35,command=bagi)
button_substract = Button(window, text="-", padx=36, pady=35,command=kurang)

#atur posisi
button_1.grid(row=3, column=0) 
button_2.grid(row=3, column=1) 
button_3.grid(row=3, column=2) 

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5,column=0)
button_substract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)

button_equal.grid(row=5, column=1, columnspan=3)
button_clear.grid(row=4, column=1, columnspan=2)
window.mainloop()