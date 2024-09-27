"""information about repo with api"""
import os
import requests



REPO = "JobPrac"
token = os.getenv("TOKEN")
OWNER = 'alsmk'


"""
fetching commits information from github.com
"""
def fetch_commit_info():
    headers = {
        'Authorization': f'token {token}'
    }
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/commits/main'
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


"""
This module fetches and prints information from a GitHub repository's  commits.
"""
def print_commit_info():
    commit_info = fetch_commit_info()
    for commit in commit_info:
        print(f'Commit: {commit["sha"][:7]}')
        print(f'Author: {commit["commit"]["author"]["name"]}')
        print(f'Date: {commit["commit"]["author"]["date"]}')
        print('----------------------------------------')
    print(f'Total commits: {len(commit_info)}')




if __name__ == '__main__':
    print_commit_info()
    