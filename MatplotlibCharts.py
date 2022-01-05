from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

window = Tk()
window.title("Learn Matplotlib")
window.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()

btn = Button(window, text="Graph It!", command=graph)
btn.pack()

window.mainloop()