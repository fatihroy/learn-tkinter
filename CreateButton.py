from tkinter import *
window = Tk()


#bikin fungsi untuk button
def clicked():
    label1 = Label(window, text="I've told you don't do that")
    label1.pack()

#bikin button
button = Button(window, text="don't click here!!", command=clicked, pady=5, padx=50, bg="red", fg="black")
button.pack()
window.mainloop()

