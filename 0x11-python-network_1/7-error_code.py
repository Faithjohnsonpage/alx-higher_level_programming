#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and
displays the body of the response."""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code:', r.status_code)
