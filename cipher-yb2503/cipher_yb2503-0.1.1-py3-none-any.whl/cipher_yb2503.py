def cipher(text, shift, encrypt = True):
    """
    encrypting and decrypting with Caesar Cipher.
    Parameters
    ----------
    text : str
      A string that you wish to encrypt or decrypt  
    shift : int
      A integer that you wish to shift the text 
    encrypt : bool
      A boolean standing for encrypting or decrypting. Encrypt by default
    Returns
    -------
    str
      The new text after encrypting or decrypting
    Examples
    --------
    >>> cipher('test', 1, encrypt = True)
    'uftu'
    >>> cipher('test', 1, encrypt = False)
    'sdrs'
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