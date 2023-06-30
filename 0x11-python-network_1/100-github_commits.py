#!/usr/bin/python3
"""
Python script that lists 10 commits of a repository using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits_data = response.json()
        for commit in commits_data[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
