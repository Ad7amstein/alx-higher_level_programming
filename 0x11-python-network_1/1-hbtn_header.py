#!/usr/bin/python3
"""Response header
"""

import urllib.request
import sys


def main():
    """Main Program
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
