"""
work clone <github-repo>
work checkout <branch>
"""

import sys

from os import makedirs, path
from posixpath import basename, expanduser
from subprocess import run
from typing import Optional

import click

from worktree_manager.config import load_config
from worktree_manager.utils import find_worktree_root


@click.group()
def cli():
    pass


@cli.command(help="clone a new repository")
@click.argument("repo", required=True)
def clone(repo: str):
    config = load_config()
    repo_name = repo.split("/")[-1].replace(".git", "")
    clone_dir = expanduser(config["clone.path"])
    project_dir = expanduser(config["projects.path"])

    dest_name = path.join(clone_dir, repo_name)
    git_command = f"git clone --bare {repo} {dest_name}"

    makedirs(clone_dir, exist_ok=True)
    run(git_command.split(" "), stdout=sys.stdout)

    # create an empty directory in projects dir
    makedirs(path.join(project_dir, repo_name))

    with open(path.join(project_dir, repo_name, ".worktree"), "w") as f:
        f.write("")

@cli.command(help="checkout a new branch")
@click.argument("branch", required=True)
@click.argument("project", required=False)
def checkout(branch: str, project: Optional[str]):
    config = load_config()
    worktree_root = find_worktree_root()

    if not worktree_root and not project:
        click.echo(
            "please run this command in a git worktree directory or pass `project param`, aborting."
        )
        return 1

    repo = basename(project or worktree_root or "")

    # create a new worktree entry
    clone_dir = expanduser(config["clone.path"])
    projects_dir = expanduser(config["projects.path"])

    repo_dir = path.join(clone_dir, repo)
    branch_path = path.join(repo_dir, branch)
    project_branch_path = path.join(projects_dir, repo, branch)

    run(f"git -C {repo_dir} worktree add {branch}".split(" "), stdout=sys.stdout)
    run(f"ln -s {branch_path} {project_branch_path}".split(" "), stdout=sys.stdout)


if __name__ == "__main__":
    cli()
