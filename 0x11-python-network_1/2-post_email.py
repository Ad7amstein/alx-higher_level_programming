#!/usr/bin/python3
"""POST an email
"""

import sys
import urllib.request


def main():
    """Main program
    """
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))


if __name__ == "__main__":
    main()
