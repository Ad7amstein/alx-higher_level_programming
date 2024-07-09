#!/usr/bin/python3
"""POST request
"""

import sys
import requests


def main():
    """Main program
    """
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)


if __name__ == "__main__":
    main()
