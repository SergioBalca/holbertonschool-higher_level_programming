#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

from requests import get
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'

    try:
        response = get(url, auth=(username, passwd)).json()
        print(response['id'])
    except Exception:
        print('None')
