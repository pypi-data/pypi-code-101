#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pytest
import numpy as np
import pandas as pd


# In[6]:


def cipher(text, shift, encrypt=True):
    """
    One type of cipher that each letter within the text is 'shifted' a certain number of places down the alphabet.
    Parameters
    ----------
    text : str
      The text that will be encrypted/decrypted.
    shift : int
      The number of positions that letters should be shift
     encrypt : bool
      Boolean that defines if is encrypting or decrypting text here. 
    Returns
    -------
    str
      The resulted version will be a string
    Examples
    --------
    >>> from cipher_jiachen_guov import cipher_jiachen_guov
    >>> cipher_jiachen_guov.cipher('nice',shift = 5, encrypt = True)
    'snhj'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

