#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter
    as a parameter.
"""

from requests import post
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

    response = post(url, data={'q': letter})
    header = response.headers['content-type']
    try:
        json = response.json()

        if header != 'application/json':
            print('Not a valid JSON')
        elif len(json) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except Exception:
        pass
