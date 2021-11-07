from datetime import datetime, timedelta, timezone
from os import makedirs
from os.path import abspath, exists
from re import compile
from shutil import rmtree
from tempfile import mkdtemp
from typing import Callable, Iterator, Optional, Pattern

from git import Head, InvalidGitRepositoryError, Remote, Repo

from .exc import GitCleanerInitError, GitCleanerInvalidPathError, \
    GitCleanerInvalidUrlError

__all__ = [
    'GitBranchCleaner',
    'EXCLUDE_PATTERN',
    'OVER_DAYS',
]


EXCLUDE_PATTERN = compile(
    r'^master|develop(?:ment)?|latest|release(?:[/-_]\w+)?|version[/-_]\w+$',
)
OVER_DAYS = 180


class GitBranchCleaner:

    def __init__(
        self,
        *,
        repo_url: Optional[str] = None,
        repo_dirpath: Optional[str] = None,
        over_days: int = OVER_DAYS,
        exclude_pattern: Pattern = EXCLUDE_PATTERN,
    ) -> None:
        if not (repo_url or repo_dirpath):
            raise GitCleanerInitError(
                'You must declare repo remote url or repo local dirpath.',
            )

        self._url = repo_url
        self._dirpath = abspath(repo_dirpath) if repo_dirpath else None

        # Check if over_days is int and abs
        self._over_days = abs(over_days) if isinstance(
            over_days, int,
        ) else OVER_DAYS

        # Check if master is in pattern
        self._exclude_pattern = exclude_pattern if 'master' in getattr(
            exclude_pattern, 'pattern', '',
        ) else EXCLUDE_PATTERN

        self._dirpath_is_temp = False
        self._dirpath_is_git = False

        self._repo: Optional[Repo] = None

    def _get_repo(self) -> Repo:
        """Get git.Repo object, searching with initial attributes."""
        if self._dirpath:
            try:
                repo = Repo(self._dirpath)
                self._dirpath_is_git = True
                return repo

            except InvalidGitRepositoryError:
                pass

            if exists(self._dirpath):
                raise GitCleanerInvalidPathError(self._dirpath)

            makedirs(self._dirpath)

        else:
            self._dirpath = mkdtemp()
            self._dirpath_is_temp = True

        try:
            return Repo.clone_from(self._url, self._dirpath)

        except Exception as err:
            raise GitCleanerInvalidUrlError(self._url) from err

    def _clean_remotes(self) -> None:
        local_heads = self._repo.heads

        for remote in self._repo.remotes:

            for remote_branch_name in self._find_remote_refs(remote):

                # remove remote branch
                remote.push(f':{remote_branch_name}')
                print(f'Remote {remote_branch_name!r} has been removed.')

                if not self._dirpath_is_git:
                    continue

                try:
                    local_head = local_heads[remote_branch_name]
                except IndexError:
                    continue

                # remove local branch with equal name
                Head.delete(self._repo, local_head)
                print(f'Local {remote_branch_name!r} has been removed.')

    def _find_remote_refs(self, remote: Remote) -> Iterator[str]:
        """Find remote refs, that are over by their last commit."""
        utcnow = datetime.utcnow().replace(tzinfo=timezone.utc)
        over_delta = timedelta(days=self._over_days)

        prefix_len = len(remote.name) + 1

        head_branch_name = self._repo.head.ref.name

        for ref in remote.refs:
            delta = utcnow - ref.commit.committed_datetime

            if delta <= over_delta:
                continue

            branch_name = ref.name[prefix_len:]

            if head_branch_name == branch_name:
                continue

            if self._exclude_pattern.match(branch_name):
                continue

            yield branch_name

    def clean(self) -> None:
        try:
            self._repo = self._get_repo()
            self._clean_remotes()

        finally:
            if self._dirpath_is_temp:
                rmtree(self._dirpath)

    __call__: Callable[['GitBranchCleaner'], None] = clean
