'''Library converting Text to IPA'''
from typing import Any

def get_IPA(text:str,language:str,proxy:Any=None) -> str:
    '''Convert Text to IPA\n
    Parameters:\n
    - `text` : the content for converting to IPA
    - `language`: must be "am" or "br" (US English or UK English)
    - `proxy` : Optional parameter using for hide ip 
    '''
    ...

def get_IPAs(bulk:list,language:str,proxy:Any=None) -> list:
    '''Convert a list of text to IPA\n
    Parameters:\n
    - `bulk` : the list of contents for converting to IPA
    - `language`: must be "am" or "br" (US English or UK English)
    - `proxy` : Optional parameter using for hide ip 
    '''
    ...

from .text2ipa import *
__all__ = ['get_IPA','get_IPAs']
