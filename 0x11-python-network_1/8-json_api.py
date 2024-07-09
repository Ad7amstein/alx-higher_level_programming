#!/usr/bin/python3
"""Search API
"""

import sys
import requests


def main():
    """Main program
    """
    url = "http://0.0.0.0:5000/search_user"
    try:
        val = sys.argv[1]
    except IndexError:
        val = ""

    req = requests.post(url, data={'q': val})
    try:
        data = req.json()
    except (requests.exceptions.JSONDecodeError, ValueError):
        if req.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
    if req.headers.get('Content-Type') != 'application/json':
        print("Not a valid JSON")
    elif not data or len(data) < 1:
        print("No result")
    else:
        print(f"[{data['id']}] {data['name']}")


if __name__ == "__main__":
    main()
