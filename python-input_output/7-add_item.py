#!/usr/bin/python3
"""Function that adds all arguments to a Python list,
and then saves them to a file"""

import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"
"""Loads existing list or create new one"""

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
"""Adds command line arguments"""

items.extend(sys.argv[1:])
"""Saves updated list back to file"""

save_to_json_file(items, filename)
