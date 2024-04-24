#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=data)
    try:
        req_json = r.json()
        if req_json:
            print("[{}] {}".format(req_json.get('id'), req_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
