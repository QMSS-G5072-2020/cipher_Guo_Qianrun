from cipher_qg2196 import __version__
from cipher_qg2196.cipher_qg2196 import cipher

def test_version():
    assert __version__ == '0.1.0'

import pytest

def test_1a():
    text = 'guys'
    shift = 1
    expected = 'hvzt'
    actual = cipher(text, shift)
    assert actual == expected
    
def test_1b():
    text = 'guys'
    shift = -1
    expected = 'ftxr'
    actual = cipher(text,shift)
    assert actual == expected
    
def test_1c():
    text = 'guys!'
    shift = 1
    expected = 'hvzt!'
    actual = cipher(text, shift)
    assert actual == expected