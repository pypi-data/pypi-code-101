import os

from pathlib import Path
from posix import listdir
from posixpath import expanduser

from click.shell_completion import CompletionItem
from click.types import ParamType

from worktree_manager.config import load_config


def find_worktree_root():
    user_home = Path.home()
    current_dir = Path(os.curdir)

    while current_dir != user_home:
        worktree_path = current_dir / ".worktree"
        if worktree_path.exists() and worktree_path.is_file():
            return str(worktree_path.parent.resolve())

        current_dir = current_dir.parent

    return None


class ProjectType(ParamType):
    def shell_complete(self, ctx, param, incomplete):
        config = load_config()
        projects_path = config["projects.path"]
        projects = listdir(expanduser(projects_path))
        return [CompletionItem(project) for project in projects]
