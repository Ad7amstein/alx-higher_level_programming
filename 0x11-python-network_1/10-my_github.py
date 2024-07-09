#!/usr/bin/python3
"""My GitHub!
"""

import sys
import requests


def main():
    """Main program"""
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")


if __name__ == "__main__":
    main()
