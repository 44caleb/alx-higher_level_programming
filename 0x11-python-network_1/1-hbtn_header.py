#!/usr/bin/python3
"""retrieves a header from a url response"""


import urllib.request
import sys


url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    header = response.getheader("X-Request-Id")
    print(header)
