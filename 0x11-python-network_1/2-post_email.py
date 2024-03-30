#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    data = {}
    data['email'] = sys.argv[2]
    url = sys.argv[1]
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
