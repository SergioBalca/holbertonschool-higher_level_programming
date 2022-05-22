#!/usr/bin/python3
""" takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
import urllib.parse
from sys import argv


url = argv[1]
email = argv[2]
headers = {}
headers['Content-type'] = 'appplication/email'

"""Post request encoded data"""
post_data = urllib.parse.urlencode({'email': email}).encode('utf-8')

"""Automatically calls POST method because request has data"""
with urlopen(url, data=post_data) as post_response:
    print(post_response.read())
