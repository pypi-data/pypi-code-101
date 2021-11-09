def cipher(text, shift, encrypt=True):
    
    """
    Function Description:
    ----------
    The Caesar cipher is one of the simplest and most widely known encryption techniques. In short, each letter is replaced by a letter some fixed number of positions down the alphabet.	
    
    Parameters:
    ----------
    text :  String
        A string format as word or sentece to be encrypted or decrypted
    shift : Integer
        An integer that decided the location and direction the str to be encrypted or decrypted       
    encrypt : Boolean
        True - encrypted False - decrypted

    Returns:
    -------
    string
        The string after encrypted pr decrypted
        
    Examples:
    --------
    >>> from cipher_yw3760 import cipher
    >>> cipher("ceasar",1, True)
    bdZrZq
    >>> cipher("bdZrZq",1, False)
    ceasar
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