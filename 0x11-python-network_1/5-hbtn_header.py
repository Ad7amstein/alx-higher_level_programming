#!/usr/bin/python3
"""Response header value 1
"""

import sys
import requests


def main():
    """Main program
    """
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
