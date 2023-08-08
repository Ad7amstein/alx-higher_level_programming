#!/usr/bin/python3
def islower(c):
    if ord(c) not in range(ord('a'), ord('z') + 1):
        return False
    else:
        return True
