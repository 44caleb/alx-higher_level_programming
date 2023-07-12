#!/usr/bin/python3
"""saves arguments to a file"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    list_obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_obj = []
for i in range(1, len(sys.argv)):
    list_obj.append(sys.argv[i])
save_to_json_file(list_obj, "add_item.json")
