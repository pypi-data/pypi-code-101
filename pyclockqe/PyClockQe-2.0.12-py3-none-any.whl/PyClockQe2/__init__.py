from tkinter import *
from tkinter.ttk import *
from time import strftime, sleep
import random
import string

def init():
    print("[PyClockQe2] Booting PyClockQe..")
    sleep(2)
    print("[PyClockQe2] Booted Successfuly!")
    ctoken = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    clength = 15
    random.shuffle(ctoken)
    gtoken = []
    for i in range(clength):
        gtoken.append(random.choice(ctoken))
    random.shuffle(gtoken)
    print("[PyClockQe2] Generating Window Token..")
    sleep(5)
    print("[PyClockQe2] Generated Token!")
    print("[PyClockQe2] This is your token: ")
    
    token = "PyClock-" + "".join(gtoken)
    print(token)
    print(f'[PyClockQe2] Use clock("{token}") to run the clock')
    

def clock(token):
    if len(token) == 23 and token[0] == "P" and token[1] == "y" and token[2] == "C" and token[3] == "l" and token[4] == "o" and token[5] == "c" and token[6] == "k" and token[7] == "-":
        root = Tk()
        root.title("PyClockQe2 | Main")
        root.configure(bg='black')
        root.resizable(False, False)
        root.geometry("650x430")
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
        label = Label(root, font=("arial", 35), text="DATE", foreground="white", background="black")
        label.pack(anchor="center")
        label2 = Label(root, font=("arial", 80), foreground="white", background="black")
        label2.pack(anchor="center")
        label3 = Label(root, font=("arial", 35), text="TIME", foreground="white", background="black")
        label3.pack(anchor="center")
        label4 = Label(root, font=("arial", 80), foreground="white", background="black")
        label4.pack(anchor="center")
        timel()
        datel()
        mainloop()
    elif len(token) != 23 and token[0] != "P" and token[1] != "y" and token[2] != "C" or len(token) != 23 and token[0] != "P" and token[1] != "y" or len(token)!= 23 and token[0] != "P" or len(token) != 23:
        print("[PyClockQe2] Token Is InValid!")
        itoken = input("[PyClockQe2] Do you wanna regenerate token? (y/n): ")
        if itoken == "y":
            sleep(5)
            ctoken = list(string.ascii_letters + string.digits + "!@#$%^&*()")
            clength = 15
            random.shuffle(ctoken)
            gtoken = []
            for i in range(clength):
                gtoken.append(random.choice(ctoken))
            random.shuffle(gtoken)
            token = "PyClock-" + "".join(gtoken)
            print("[PyClockQe2] This is your new token:")
            print(token)
        if itoken == "n":
            print("[PyClockQe2] Ok, to remind you can do clock() again!")
