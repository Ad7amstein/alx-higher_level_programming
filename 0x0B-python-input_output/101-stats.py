#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_info(size, d):
    """Prints information."""
    print("File size: {}".format(size))
    for k, v in sorted(d.items()):
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0,
                    "400": 0, "401": 0,
                    "403": 0, "404": 0,
                    "405": 0, "500": 0}

    counter = 1
    total_size = 0
    for line_in in sys.stdin:
        line = line_in.split()
        total_size += int(line[-1])
        code = line[-2]

        status_codes[code] += 1

        if counter == 10:
            print_info(total_size, status_codes)
            counter = 0

        counter += 1

    print_info(total_size, status_codes)
