#!/usr/bin/python3
"""
This here Contains the function "wrtie_file"
"""

def write_file(filename="", text=""):
    """this here returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
