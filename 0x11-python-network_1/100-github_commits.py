#!/usr/bin/python3
"""This script fetches the commits of a repository by a specific
user using the GitHub API"""
import requests
import sys

if __name__ == "__main__":
    # Extract repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the URL for fetching commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to fetch the commits
    response = requests.get(url)

    # Parse the response JSON
    commits = response.json()

    # Print the commits (from the most recent to oldest)
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
