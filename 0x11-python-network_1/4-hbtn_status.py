#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

from requests import get

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.content)
