import os


def push_repo(remote_url: str, branch: str = 'main', push: bool = False):
    """set remote url and push to remote if push is true"""
    os.system(f'git remote add origin {remote_url}')
    if push:
        os.system(f'git push -u origin {branch}')