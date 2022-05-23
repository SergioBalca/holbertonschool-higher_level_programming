#!/usr/bin/python3
""" takes two arguments to list last 10 commits of the
    repository "rails" by the use of r "rails"
"""

from requests import get
from sys import argv


if __name__ == "__main__":

    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = get(url).json()
    """response is a list of dictionaries"""

    for dic in r[:10]:
        print('{}: {}'.format(dic.get('sha'),
                              dic.get('commit').get('author').get('name')))
