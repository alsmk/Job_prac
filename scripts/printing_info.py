"""information about repo with api"""
import os
import requests






def fetch_commit_info():
    """fetching commits information from github.com"""

    API_URL = "https://api.github.com"
    REPO = os.getenv('GITHUB_REPOSITORY')  
    TOKEN = os.getenv('TOKEN')
    headers = {
        'Authorization': f'token {TOKEN}'
    }
    url = f"{API_URL}/repos/{REPO}/commits"
    # print(f'url: {url}')
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()



def print_commit_info():
    """This module fetches and prints information from a GitHub repository's commits"""
    commit_info = fetch_commit_info()
    print('Commit Information:')
    for commit in commit_info:
        print(f'Commit: {commit["sha"][:7]}')
        print(f'Author: {commit["commit"]["author"]["name"]}')
        print(f'Date: {commit["commit"]["author"]["date"]}')
        print('----------------------------------------')
    print(f'Total commits: {len(commit_info)}')




if __name__ == '__main__':
    print_commit_info()
    