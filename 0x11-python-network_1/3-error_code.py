#!/usr/bin/python3
"""sends a request to a url and displays possible errors"""


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print(data.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

