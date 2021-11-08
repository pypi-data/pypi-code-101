from tkinter import *
from tkinter.ttk import *
from time import strftime

def init():
    root = Tk()
    root.title("PyClockQ | Main")
    root.configure(bg='black')
    root.iconbitmap(r"clock.ico")
    root.resizable(False, False)
    root.geometry("650x430")

def clock():
    def timel():
        string = strftime("%H:%M:%S %p")
        pa = strftime("%p")
        label4.config(text=string)
        label4.after(1000, timel)
        if pa == "PM":
            label3.config(foreground="gold")
            label4.config(foreground="gold")
        elif pa == "AM":
            label3.config(foreground="dodgerblue")
            label4.config(foreground="dodgerblue")
    def datel():
        string = strftime("%d/%m/%Y")
        pa = strftime("%p")
        label2.config(text=string)
        label2.after(1000, datel)
        if pa == "PM":
            label.config(foreground="dodgerblue")
            label2.config(foreground="dodgerblue")
        elif pa == "AM":
            label.config(foreground="gold")
            label2.config(foreground="gold")
    label = Label(root, font=("ds-digital", 35), text="DATE", foreground="white", background="black")
    label.pack(anchor="center")
    label2 = Label(root, font=("ds-digital", 80), foreground="white", background="black")
    label2.pack(anchor="center")
    label3 = Label(root, font=("ds-digital", 35), text="TIME", foreground="white", background="black")
    label3.pack(anchor="center")
    label4 = Label(root, font=("ds-digital", 80), foreground="white", background="black")
    label4.pack(anchor="center")
    timel()
    datel()
    mainloop()
