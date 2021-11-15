#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Easy functions have been developed by grouping frequently used operations with Tkinter.
"""

__author__ = 'ibrahim CÖRÜT'
__email__ = 'ibrhmcorut@gmail.com'

import tkinter
from tkinter import messagebox, simpledialog, ttk, font


def ask_question(title, message, question='yesno', icon='warning', timeout=None):
    print('\n\n\n######### %s #########: %s\n\n\n' % (title, message))
    reply = 'yes'
    tk = tkinter.Tk()
    tk.title(title)
    tk.withdraw()
    if timeout is not None:
        tk.after(timeout * 1000, tk.destroy)
        print('If no selection is made, True will be selected after %s sec.' % timeout)
    try:
        if question == 'yesno':
            reply = tkinter.messagebox.askquestion(title, message, icon=icon)
        elif question == 'info':
            reply = tkinter.messagebox.showinfo(title, message, icon=icon)
    except tkinter.EXCEPTION:
        pass
    if reply == '':
        reply = 'yes'
        print('True selected and in progress...')
    if timeout is None:
        tk.destroy()
    tk.quit()
    print('Received Reply:##%s##' % str(reply).lower())
    if str(reply).lower() == 'yes':
        return True
    elif str(reply).lower() == 'no':
        return False


def dialog_input(title, question):
    tk = tkinter.Tk()
    tk.title(title)
    tk.withdraw()
    reply = tkinter.simpledialog.askstring(title=title, prompt=question)
    tk.quit()
    print('Received Reply:##%s##' % str(reply))
    return str(reply)


def dialog_combobox(title, message, values):
    class TkSelectValues:
        def __init__(self):
            self.select_value = ''

        def select_values(self):
            self.select_value = combo.get()
            tk.destroy()

    tk = tkinter.Tk()
    font_style = tkinter.font.Font(family="arial black", size=21)
    tk.title(title)
    label = tkinter.ttk.Label(tk, text=message, font=font_style)
    label.pack()
    combo = tkinter.ttk.Combobox(tk, values=values, font=font_style)
    combo.pack()
    combo.set(values[0])
    select_combo = TkSelectValues()
    button = tkinter.Button(text='Select', command=select_combo.select_values, font=font_style)
    button.pack()
    tk.wait_window(tk)
    tk.quit()
    print('Returned Value:##%s##' % select_combo.select_value)
    return select_combo.select_value


class Tkinter:
    ask_question = staticmethod(ask_question)
    dialog_combobox = staticmethod(dialog_combobox)
    dialog_input = staticmethod(dialog_input)
