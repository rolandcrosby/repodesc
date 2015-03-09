#!/usr/bin/env python
import requests
import argparse
import sys
import os
import re
import json

def get_auth_data():
    auth_data = ()
    cred_path = '~/etc/github_creds.json'
    if 'GITHUB_CRED_PATH' in os.environ:
        cred_path = os_environ['GITHUB_CRED_PATH']
    if os.path.exists(os.path.expanduser(cred_path)):
        with open(os.path.expanduser(cred_path)) as f:
            json_auth = json.load(f)
            auth_data = (json_auth['username'], json_auth['password'])
    return auth_data

def get_repo_info(repo):
    resp = requests.get('https://api.github.com/repos/' + repo, auth=get_auth_data())
    if resp.status_code == 200:
        return resp.json()
    else:
        match = re.search(r'(.*)\.git$', repo)
        if match:
            return get_repo_info(match.group(1))
        return None

def main():
    if sys.stdin.isatty():
        parser = argparse.ArgumentParser(description='Get the description of a Github repo')
        parser.add_argument('repo', action='store', help='Github repo name, formatted as "user/repo"')
        args = parser.parse_args()
        info = get_repo_info(args.repo)
        if info:
            print info['description']
    else:
        for line in sys.stdin:
            info = get_repo_info(line.strip())
            if info:
                print info['description']

if __name__ == "__main__":
    main()
