#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status"""

from urllib.request import urlopen, Request

with urlopen('https://intranet.hbtn.io/status') as r:
    body = r.read()
    print('Body response:')
    print('\t- type:', type(body))
    print('\t- content:', body)
    print('\t- utf8 content:', body.decode('utf-8'))
