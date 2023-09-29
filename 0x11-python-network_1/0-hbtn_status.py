#!/usr/bin/python3
"""retrieves the content of a url"""


import urllib.request


req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

with urllib.request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode()))
