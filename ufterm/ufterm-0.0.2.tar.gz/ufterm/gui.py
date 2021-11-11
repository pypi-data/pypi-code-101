import sys
import os
import atexit
import tkinter as tk
import themed_tkinter as ttk
import signal

from typing import Optional, Type, Callable
from ctypes import c_bool
from threading import Thread
from multiprocessing import Process, Queue, Value
from queue import Empty as EmptyQueue

from .exception import ValidationError, ConversionError
from .constant import *
from .register import Register
from .utils import convert_str_to_type


# Parent process globals
_g_started = False
_g_input_queue: Optional[Queue] = None
_g_output_queue: Optional[Queue] = None


# Child process globals
_g_root_window: Optional[ttk.Tk] = None
_g_text_area: Optional[ttk.ScrollableText] = None
_g_popup: Optional[ttk.Toplevel] = None


# Tkinter classes
class Tk(ttk.Tk):

    def __init__(self):
        self.__inner_width = None
        self.__inner_height = None
        self.__x = None
        self.__y = None
        self.__geometry_updated_id = None
        super().__init__()
        self.after(50, self.reset_to_last_geometry)

    @property
    def inner_width(self) -> int:
        if self.__inner_width is None:
            self.__inner_width = self.winfo_width()
        return self.__inner_width

    @property
    def inner_height(self) -> int:
        if self.__inner_height is None:
            self.__inner_height = self.winfo_height()
        return self.__inner_height

    @property
    def x(self) -> int:
        if self.__x is None:
            self.__x = self.winfo_x()
        return self.__x

    @property
    def y(self) -> int:
        if self.__y is None:
            self.__y = self.winfo_y()
        return self.__y

    def on_configure(self, event):
        class DummyException(Exception):
            pass
        super().on_configure(event)
        if event.widget == self:
            try:
                if self.inner_width != event.width:
                    self.__inner_width = None
                    raise DummyException
                elif self.inner_height != event.height:
                    self.__inner_height = None
                    raise DummyException
                elif self.x != event.x:
                    self.__x = None
                    raise DummyException
                elif self.y != event.y:
                    self.__y = None
                    raise DummyException
            except DummyException:
                if self.__geometry_updated_id is not None:
                    self.after_cancel(self.__geometry_updated_id)
                self.__geometry_updated_id = self.after(1000, self.on_geometry_updated)

    def reset_to_last_geometry(self):
        geometry = Register.get('last_geometry', None)
        if geometry is None:
            self.geometry(geometry)

    def on_geometry_updated(self):
        Register['last_geometry'] = self.geometry()
        print(self.geometry(), Register['last_geometry'])


class PopupWindow(ttk.Toplevel):
    def __init__(self, master: tk.Wm, label: str, history_id: str, default_value: ValueType, error_msg: str, **kw):
        ttk.Toplevel.__init__(self, master, **kw)
        self.result = default_value
        self.minsize(420, 250)
        self.bind("<Return>", lambda _: self.ok())

        self.label = ttk.Label(self, text=label)
        self.label.pack()

        self.entry = ttk.EntryWithChoices(self, Register.get("history", {}).get(history_id, []))
        self.entry.insert(tk.END, default_value)
        self.entry.pack()

        self.error_label = ttk.Label(self, text=error_msg, fg='red')
        self.error_label.pack()

        self.button = ttk.PrimaryButton(self, text="OK", command=self.ok)
        self.button.pack(fill=tk.X, expand=True)
        self.update_theme()

    def ok(self):
        self.result = self.entry.get()
        self.destroy()

    @property
    def theme(self):
        return self.master.theme


# Functions
def show(text: str, msg_type: str):
    _g_input_queue.put((CMD_SHOW, text, msg_type))


def ask(label: str,
        history_id: str,
        type_: Type[ValueType],
        default_value: ValueType,
        validator: Callable[[ValueType], bool]) -> ValueType:

    _g_input_queue.put((CMD_ASK, label, history_id, type_, default_value))
    while _g_started:
        result = _g_output_queue.get()
        try:
            if validator(result):
                return result
            else:
                err = "The value isn't right"
                _g_input_queue.put((CMD_SHOW_ERR, label, history_id, type_, result, err))
        except ValidationError as error:
            _g_input_queue.put((CMD_SHOW_ERR, label, history_id, type_, result, str(error)))


def insert_text(text: str, msg_type: str):
    if not text.endswith('\n'):
        text += "\n"
    _g_text_area.text.configure(state='normal')
    _g_text_area.text.insert(tk.END, text, msg_type)
    _g_text_area.text.configure(state='disabled')
    _g_text_area.text.see(tk.END)


def show_dialog(gui_closed: Value,
                label: str,
                history_id: str,
                type_: Type[ValueType],
                default_value: ValueType,
                error_msg: str) -> ValueType:

    while not gui_closed.value:
        dialog = PopupWindow(_g_root_window, label, history_id, default_value, error_msg)
        _g_root_window.wait_window(dialog)
        try:
            return convert_str_to_type(dialog.result, type_)
        except ConversionError as error:
            error_msg = str(error)
            default_value = dialog.result


def watch_cmd(gui_closed: Value, in_queue: Queue, out_queue: Queue):
    while not gui_closed.value:
        tmp = in_queue.get()
        if tmp[0] == GUI_MAINLOOP_FINISH:
            break
        elif tmp[0] == CMD_SHOW:
            _, text, msg_type = tmp
            insert_text(text, msg_type)
        elif tmp[0] == CMD_ASK:
            _, label, history_id, type_, default_value = tmp
            out_queue.put(show_dialog(gui_closed, label, history_id, type_, default_value, ""))
        elif tmp[0] == CMD_SHOW_ERR:
            _, label, history_id, type_, default_value, error_msg = tmp
            out_queue.put(show_dialog(gui_closed, label, history_id, type_, default_value, error_msg))


def loop(win_title: str, gui_closed: Value, in_queue: Queue, out_queue: Queue, except_queue: Queue):
    global _g_root_window
    global _g_text_area

    _g_root_window = Tk()
    _g_root_window.title(win_title)
    _g_root_window.center()
    _g_root_window.minsize(750, 420)
    _g_text_area = ttk.ScrollableText(_g_root_window)
    _g_text_area.text.configure(state='disabled')
    _g_text_area.text.tag_configure(WARNING_MSG.name, foreground="red")
    _g_text_area.text.tag_configure(ERROR_MSG.name, foreground="orange")
    _g_text_area.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

    watching_cmd_thread = Thread(target=watch_cmd, args=(gui_closed, in_queue, out_queue))

    # When the window appear we wait 1 second to start processing the commands
    _g_root_window.after(1000, watching_cmd_thread.start)
    out_queue.put(GUI_MAINLOOP_STARTED)
    _g_root_window.mainloop()
    with gui_closed.get_lock():
        gui_closed.value = True
    try:
        except_queue.get_nowait()
    except EmptyQueue:
        print("The GUI have been close before the end of the program", file=sys.stderr)
        Register.commit()
        Register.wait_commit_to_finish()
        os.kill(os.getppid(), signal.SIGTERM)

    in_queue.put(GUI_MAINLOOP_FINISH)
    if watching_cmd_thread.is_alive():
        watching_cmd_thread.join()


def start(title: str):
    def program_end():
        exception_queue.put(PROGRAM_FINISH)

    global _g_started
    global _g_input_queue
    global _g_output_queue

    _g_started = False
    _g_input_queue = Queue()
    _g_output_queue = Queue()
    gui_closed = Value(c_bool, False)
    exception_queue = Queue()
    loop_process = Process(target=loop, args=(title, gui_closed, _g_input_queue, _g_output_queue, exception_queue))

    atexit.register(program_end)
    loop_process.start()

    # Wait that the process started and initialized
    if _g_output_queue.get() == GUI_MAINLOOP_STARTED:
        _g_started = True
    else:
        raise RuntimeError("Error while starting the GUI")


def is_started():
    return _g_started
