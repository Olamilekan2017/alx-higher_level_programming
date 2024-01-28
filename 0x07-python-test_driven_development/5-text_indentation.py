#!/usr/bin/python3
""" This function prints a text """


def text_indentation(text):
    """ Prints text with 2 new lines """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c_line = 0
    while c_line < len(text) and text[c_line] == ' ':
        c_line += 1

    while c_line < len(text):
        print(text[c_line], end="")
        if text[c_line] == "\n" or text[c_line] in ".?:":
            if text[c_line] in ".?:":
                print("\n")
            c_line += 1
            while c_line < len(text) and text[c_line] == ' ':
                c_line += 1
            continue
        c_line += 1
