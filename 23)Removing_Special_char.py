""" Remove all special characters other than alphabets and digits."""

import re

def remove_special_char(string):
    """Remove special characters from string."""
    string = re.sub('[^A-Za-z0-9]+', '', string)
    return string

string = """H!@#$e%^&*()_+{l}|:"<>?l`~-=[]\;'o,./"""
print('Original String: ', string)
string = remove_special_char(string)
print(string)