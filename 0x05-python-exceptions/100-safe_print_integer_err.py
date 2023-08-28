#!/usr/bin/python3
import os
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        os.write(sys.stderr.fileno(), f"Exception: {err.args[0]}\n".encode())
        return False
