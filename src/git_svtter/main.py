import typer
import os
from git_svtter import libs

app = typer.Typer()


@app.command()
def create_repo(filepath: str, remote_url: str = None, push: bool = False):
    """create a new repository, with lfs enabled"""
    os.makedirs(filepath, exist_ok=True)
    os.chdir(filepath)
    os.system('git init')
    os.system('git lfs install')
    os.system('git lfs track "*.zip"')
    os.system('git add .gitattributes')
    os.system('git commit -m "init project and enable lfs"')
    os.system('git branch -M main')
    if remote_url:
        libs.push_repo(remote_url, 'main', push)


@app.command()
def init_repo(filepath: str, remote_url: str = None, push: bool = False):
    """init a existing repo, with lfs enabled"""
    os.chdir(filepath)
    os.system('git init')
    os.system('git lfs install')
    os.system('git lfs track "*.zip"')
    os.system('git add .gitattributes')
    os.system('git commit -m "init project and enable lfs"')
    os.system('git branch -M main')
    if remote_url:
        libs.push_repo(remote_url, 'main', push)

@app.command()
def search_command(keyword: str):
    """search command from git-svtter"""
    print('not implemented')

if __name__ == '__main__':
    app()
