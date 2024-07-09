#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import sys
import requests
import json


def main():
    """Main program"""
    url = "https://api.github.com/repos/" +\
        sys.argv[2] + "/" + sys.argv[1] + "/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in sorted(
        commits,
        key=lambda commit: commit["commit"]["author"]["date"], reverse=True
    ):
        print("{}: {}".format(
            commit["sha"], commit["commit"]["author"]["name"]))


if __name__ == "__main__":
    main()
