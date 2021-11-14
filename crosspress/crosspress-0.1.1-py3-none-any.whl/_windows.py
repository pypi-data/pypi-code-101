import ctypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)


def action(code, mod):
    [sc, vk] = code[:2]
    if sc > 128:
        sc = sc - 128
        mod += 1
    user32.keybd_event(vk, sc, mod, 0)
    return


def press(code):
    action(code, 0)
    return


def release(code):
    action(code, 2)
    return


def sequence(codes, delay):
    for code in codes:
        press(code)
        time.sleep(delay)
    codes.reverse()
    for code in codes:
        release(code)
        time.sleep(delay)
    return
