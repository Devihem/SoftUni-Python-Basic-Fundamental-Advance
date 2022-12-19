from time import strftime
from tkinter import *

root = Tk()
root.title("Devihem basic Clock")


def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)


label = Label(root, font=("sans", 200), background="white", foreground="grey")
label.pack(anchor="center")

clock()
mainloop()
