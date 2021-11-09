import pyautogui
import time

def pyautotype(wait_time):
    text = input('Typed Text:')
    time.sleep(wait_time)
    for c in text:
        time.sleep(0.1)
        pyautogui.press(c)
