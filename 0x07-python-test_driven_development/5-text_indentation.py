#!/usr/bin/python
"""Defines a text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines
       after each of these characters: ., ? and :

    Args:
        text (str): Text to be printed.

    Raises:
        TypeError: If the text in not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in text:
        print(c, end='')
        if c in ['.', '?', ':']:
            print("\n\n", end='')
