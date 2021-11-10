
def cipher(text, shift, encrypt=True):
    
    """This cipher takes string data and 'ciphers' it by shifting each letter by the number of positions specified in the alphabet. 

    Args:
        text: Input string data to be encrypted / ciphered 
        shift: Number of positions in the alphabet to shift in the right direction
        encrypt: True/False indicator defining whether or not the string is to be encrypted by this function
    Returns:
      Ciphered text with input string data 'text' shifted the number of units defined by 'shift' input. 
      
    Typical usage example:
        >>> print([cipher('coding',5)])
        'htinsl'
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
