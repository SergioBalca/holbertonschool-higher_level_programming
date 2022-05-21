#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response
"""

from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as r:
        body = r.info()
        print(body['X-Request-Id'])
