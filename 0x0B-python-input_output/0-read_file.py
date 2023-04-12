#!/usr/bin/python3
"""This here contains the read_file function for this task"""

def read_file(filename=""):
    """for reading a text file in (UTF8) and prints ti the stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
