#!/usr/bin/python3
"""posts an email to a url and retrieves response body"""


import urllib.request
import sys
import urllib.parse


url = sys.argv[1]
email = sys.argv[2]

value = {"email": email}
value = urllib.parse.urlencode(value)
value = value.encode("ascii")
req = urllib.request.Request(url, value)
with urllib.request.urlopen(req) as response:
    data = response.read()
    print(data.decode())
