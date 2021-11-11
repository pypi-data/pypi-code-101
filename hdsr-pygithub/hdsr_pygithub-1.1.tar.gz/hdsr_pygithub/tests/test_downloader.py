from datetime import timedelta
from github import BadCredentialsException
from github import Github
from github.ContentFile import ContentFile
from github.Repository import Repository
from hdsr_pygithub import exceptions
from hdsr_pygithub.downloader import GithubFileDownloader
from pathlib import Path

import pytest


def test_wrong_token():
    repo_name = "startenddate"
    target_file = Path("data/output/results/mwm_peilschalen_short.csv")
    with pytest.raises(BadCredentialsException):
        GithubFileDownloader(repo_name=repo_name, target_file=target_file, personal_access_token="xxx")


def test_repo_does_not_exist():
    repo_name = "xxx"
    target_file = Path("xxx")
    with pytest.raises(exceptions.GithubRepoInstanceError):
        GithubFileDownloader(repo_name=repo_name, target_file=target_file)


def test_wrong_file_does_not_exist():
    repo_name = "startenddate"
    target_file = Path("xxx")
    with pytest.raises(exceptions.GithubFileNotFoundError):
        GithubFileDownloader(repo_name=repo_name, target_file=target_file)


def test_download_works():
    repo_name = "startenddate"
    target_file = Path("data/output/results/mwm_peilschalen_short.csv")
    github = GithubFileDownloader(repo_name=repo_name, target_file=target_file)

    # test github instance
    assert isinstance(github.github_instance, Github)

    # test repo
    assert isinstance(github.repo_instance, Repository)
    assert github.repo_instance.name == repo_name

    # test target_file
    assert github.target_file == target_file

    # test target_file content
    assert isinstance(github.target_file_content, ContentFile)
    assert github.target_file_content.name == target_file.name
    assert github.target_file_content.content

    # test download_url exists
    assert github.target_file_content.download_url


def test_file_download_too_old():
    repo_name = "startenddate"
    target_file = Path("data/output/results/mwm_peilschalen_short.csv")
    short_timedelta = timedelta(minutes=1)  # the file is too old for sure
    with pytest.raises(exceptions.GithubFileTooOldError):
        GithubFileDownloader(
            repo_name=repo_name, target_file=target_file, target_file_allowed_period_no_updates=short_timedelta
        )
