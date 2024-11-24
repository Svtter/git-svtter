import typer
import os

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
        os.system(f'git remote add origin {remote_url}')
        if push:
            os.system('git push -u origin main')

if __name__ == '__main__':
    app()
