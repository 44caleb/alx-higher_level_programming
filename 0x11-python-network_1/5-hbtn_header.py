#!/usr/bin/python3
"""fetches data from a url and displays a header value"""


import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
