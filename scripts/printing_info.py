import requests
import os


repo = "JobPrac"
token = os.getenv("TOKEN")
owner = 'alsmk'
def fetch_commit_info():
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits', headers=headers)
    response.raise_for_status()
    return response.json()


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
    