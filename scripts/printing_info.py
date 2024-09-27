import requests
import os


REPO = "JobPrac"
token = os.getenv("TOKEN")
OWNER = 'alsmk'
def fetch_commit_info():
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(f'https://api.github.com/repos/{OWNER}/{REPO}/commits/main', 
                            headers=headers)
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
    