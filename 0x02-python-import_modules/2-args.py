#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    print("{} {}".format(length, "argument" if length == 1
        else "arguments"), end='')
    if length == 0:
        print(".")
    else:
        print(":")
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
