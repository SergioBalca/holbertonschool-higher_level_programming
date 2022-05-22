#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
    and displays the body of the response.
"""

from requests import get
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    response = get(url)
    """ if status code is between 200 and 400 the if statement
        returns True, and False otherwise
    """
    if response:
        print(response.text)
    else:
        print('Error code:', response.status_code)
