#!/usr/bin/python3
"""
Python script that takes a URL as an argument,
sends a request to the URL using the requests package,
and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get('X-Request-Id'))
