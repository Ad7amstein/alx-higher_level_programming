#!/usr/bin/python3
"""Fetch a url
"""

import urllib.request


def main():
    """Main program"""
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf8')}")


if __name__ == "__main__":
    main()
