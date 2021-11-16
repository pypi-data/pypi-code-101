"""
This module implements the main functionality of typePrint

Author: Atharva Bhandvalkar

Note:
    Speed reffer to sleep time after each write

Methods
-------

    typeNormal : Normal type with constant speed
    typeHuman : Type with speed decreasing with every letter
"""

__author__ = "Atharva Bhandvalkar"
__email__ = "atharv.bhandvalkar@gmail.com"
__status__ = "planning"

import sys
import time


# For version 0.0.2 ---
line1 = ['1','2','3','4','5','6','7','8','9','0','-','=']
line2 = ['q','w','e','r','t','y','u','i','o','p','[',']']
line3 = ['a','s','d','f','g','h','j','k','l',';']
line4 = ['z','x','c','v','b','n','m',',','.','/']
# ---

def typeNormal(string, speed=6./90):
    """
    typeNormal will print string with constant speed
    
    
    Parameters:
    -----------
    
    string : str
        string to print
    speed : float
        Sleep time after every letter
    """
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)


def typeHuman(string, start_speed=9./90, inc_speed=.08/90):
    """
    typeHuman will print string with constant speed at start of word and 
    after each letter speed will increase by inc_speed. The speed will reset 
    to start_speed when new word starts
    
    
    Parameters:
    -----------
    
    string : str
        string to print
    start_speed : float
        Sleep time of every word when the word starts
    inc_speed : float
        with every letter the speed will decrease with inc_speed 
    """
    speed = start_speed
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
        speed = speed + inc_speed
        if c == ' ':
            time.sleep(.008)
            speed = start_speed