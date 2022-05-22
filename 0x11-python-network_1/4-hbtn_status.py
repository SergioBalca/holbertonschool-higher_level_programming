#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

from requests import get

if __name__ == "__main__":
    response = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
