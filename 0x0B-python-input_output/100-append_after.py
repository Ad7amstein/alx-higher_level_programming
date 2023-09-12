#!/usr/bin/python3
"""Defines an append after function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string."""
    with open(filename, mode="r+", encoding="utf-8") as MyFile:
        lines = MyFile.readlines()

        index = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(index + 1, new_string)
            index += 1

        MyFile.seek(0)
        MyFile.writelines(lines)
