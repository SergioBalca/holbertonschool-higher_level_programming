#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError


if __name__ == "__main__":

    url = argv[1]

    try:
        with urlopen(url) as response:
            print(response.read())
    except HTTPError as err:
        print('Error code:', err.code)
