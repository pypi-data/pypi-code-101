import pyautogui
import time

def pyautotype(wait_time):
    text = input('Typed Text:')
    time.sleep(wait_time)
    for c in text:
        pyautogui.press(c)
