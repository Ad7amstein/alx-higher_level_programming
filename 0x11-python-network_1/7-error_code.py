#!/usr/bin/python3
"""Error code
"""

import sys
import requests


def main():
    """Main program
    """
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)


if __name__ == "__main__":
    main()
