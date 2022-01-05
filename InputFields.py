from tkinter import *
window = Tk()



#creating inputfields
e = Entry(window, width=50, fg="black", bg="yellow", borderwidth=5)
e.pack()
#supaya ada tulisan di inputfields
e.insert(0, "enter your nama")

#create fuction
def clicked():
    salam = "Assalamualaikum " + e.get() #e.get() adalah hasil dari ketikan di input fields
    label1 = Label(window, text=salam)
    label1.pack()

button = Button(window, text="Enter Your Name", command=clicked, pady=5, padx=50, bg="white", fg="black")
button.pack()
window.mainloop()