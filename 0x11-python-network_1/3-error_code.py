#!/usr/bin/python3
"""Error code
"""

import sys
import urllib.request
import urllib.error


def main():
    """Main Program
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
