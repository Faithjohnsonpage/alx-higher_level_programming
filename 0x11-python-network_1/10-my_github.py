#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=basic)
    user_data = response.json()
    #print(user_data.get('id'))
    print(user_data)
