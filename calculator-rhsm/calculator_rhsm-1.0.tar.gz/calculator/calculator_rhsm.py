from tkinter import *


class Calc:

    def __init__(self):
        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)  # Travamos o tamanho da janela conforme os widgets.

        self.screen_numbers = Entry(self.window, justify="center", font="arial 20 bold", bg="#D9525E", fg="white", width=26)
        self.screen_numbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        color_button_number = "#175073"
        color_function_number = "#2E8C83"
        self.button_1 = Button(self.frame, bg=color_button_number, bd=0, text="1", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("1"))

        self.button_2 = Button(self.frame, bg=color_button_number, bd=0, text="2", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("2"))

        self.button_3 = Button(self.frame, bg=color_button_number, bd=0, text="3", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("3"))

        self.button_4 = Button(self.frame, bg=color_button_number, bd=0, text="4", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("4"))

        self.button_5 = Button(self.frame, bg=color_button_number, bd=0, text="5", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("5"))

        self.button_6 = Button(self.frame, bg=color_button_number, bd=0, text="6", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("6"))

        self.button_7 = Button(self.frame, bg=color_button_number, bd=0, text="7", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("7"))

        self.button_8 = Button(self.frame, bg=color_button_number, bd=0, text="8", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("8"))

        self.button_9 = Button(self.frame, bg=color_button_number, bd=0, text="9", font="arial 20 bold", fg="white",
                               width=5, height=3, command=lambda: self.touch("9"))

        self.button_increase = Button(self.frame, bg=color_function_number, bd=0, text="+", font="arial 20 bold",
                                      fg="white", width=5, height=3, command=lambda: self.touch("+"))

        self.button_decrease = Button(self.frame, bg=color_function_number, bd=0, text="-", font="arial 20 bold",
                                        fg="white", width=5, height=3, command=lambda: self.touch("-"))

        self.button_division = Button(self.frame, bg=color_function_number, bd=0, text="/", font="arial 20 bold",
                                      fg="white", width=5, height=3, command=lambda: self.touch("/"))

        self.button_multi = Button(self.frame, bg=color_function_number, bd=0, text="x", font="arial 20 bold",
                                   fg="white", width=5, height=3, command=lambda: self.touch("*"))

        self.button_equal = Button(self.frame, bg=color_function_number, bd=0, text="=", font="arial 20 bold",
                                   fg="white", width=12, height=3, command=self.button_total)

        self.button_clean = Button(self.frame, bg=color_function_number, bd=0, text="C", font="arial 20 bold",
                                   fg="white", width=5, height=3, command=self.button_clean)

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_division.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_multi.grid(row=1, column=3)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_decrease.grid(row=2, column=3)
        self.button_increase.grid(row=3, column=3)
        self.button_clean.grid(row=3, column=2)
        self.button_equal.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def touch(self, num):
        self.screen_numbers.insert(END, num)

    def button_clean(self):
        self.screen_numbers.delete(0, END)

    def button_total(self):
        t = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(t))

Calc()
