def cipher(text, shift, encrypt=True):
    """
    encrypt or decrypt text according to shift number of user's choice
    
    Parameters
    -------------
    text: a string that represents text that user wants to encrypt or decrypt
    shift: number of shifts the user want to encrypt or decrypt the text
    encrypt: whether the user wants to encrypt or decrypt text
    
    Returns
    ----------
    a string that respresent the encryption or decryption of the text
    
    Examples 
    -----------
    >>> from cipher_qg2196.cipher_qg2196 import cipher
    >>> text = 'cool!'
    >>> shift = 1
    >>> encrypt = True
    >>> cipher('cool!', shift = 1, encrypt = True)
    'dppm!'
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