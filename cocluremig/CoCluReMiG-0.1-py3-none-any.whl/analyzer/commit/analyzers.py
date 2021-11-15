"""
Concrete Commit analytics
"""
from collections import Counter
from typing import Dict, Iterable, Set, Union

import git

from cocluremig.analyzer.commit import aggregators, blob_inspectors
from cocluremig.analyzer.commit.base_analyzer import RepoFileMetricAnalyzer


def get_basic_commit_data(commit: git.Commit) -> Dict[str, Union[int, str, bool]]:
    """
    gets all data directly stored in commits

    @param commit: a git commit
    @return: a dictionary of commit info
    """
    data = dict(sha=commit.hexsha,
                date_committed=commit.committed_date,
                date_authored=commit.authored_date,
                signed=bool(commit.gpgsig),
                author_name=commit.author.name,
                author_mail=commit.author.email,
                committer_name=commit.committer.name,
                committer_mail=commit.committer.email)
    return data


def get_file_number_per_extension_analyzer(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets an analyzer for file number per extension (which returns a dictionary)

    @param repo: a git repository
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  lambda x: {blob_inspectors.get_file_extension(x): int(1)},
                                  aggregators.additive_dict_merge, {})


def get_file_number_analyzer(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets an analyzer for file number (which returns an integer)
    @param repo: a git repository
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  lambda x: 1,
                                  lambda x, y: x + y,
                                  0)


def get_lizard_analyzer(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets an analyzer for lizard (http://lizard.ws) metrics (a list of lizard results)

    @param repo: a git repository
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  blob_inspectors.get_code_metrics_lizard)


def get_lizard_analyzer_avg(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets an analyzer for lizard metrics on average (which returns a dictionary of average elements)

    @param repo: a git repository
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  blob_inspectors.get_lizard_metrics_avarageable,
                                  aggregators.additive_dict_merge,
                                  {})


def get_lines_of_text_analyzer(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets an analyzer for lines of text (which returns an int)

    @param repo: a git repository
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  blob_inspectors.get_lines_of_text,
                                  lambda x, y: x + y,
                                  0)


def get_file_text_size_analyzer(repo: git.Repo) -> RepoFileMetricAnalyzer:
    """
    Gets the text or file size per file-type
    lines of text for text-based files and file size for binary files

    @param repo: a git repo
    @return: the analyzer-object
    """
    return RepoFileMetricAnalyzer(repo,
                                  blob_inspectors._get_mixed_size_per_extension,
                                  aggregators.additive_dict_merge,
                                  {})


def get_files(sha: git.objects.Commit) -> Set[str]:
    """
    gets all file-paths available in given commit

    @param sha: the commit
    @return: a list of paths
    """
    return {blob.path for blob in sha.tree.traverse() if blob.type == "blob"}


def get_all_commits(repo: git.Repo) -> Iterable[git.objects.Commit]:
    """
    Gets all commits for given repo

    @param repo: a git repository
    @return: the set of all commits
    """
    return {commit for starting_point in repo.heads
            for commit in repo.iter_commits(starting_point.commit)}


def get_dominating_language(repo: git.Repo) -> str:
    """
    Gets dominating (most commonly used) language for repository across all commits

    @param repo: a git repository
    @return: the file extension
    """
    extension_getter = lambda x: x.split(".")[-1]
    ext_cnt = Counter([extension_getter(f)
                       for commit in get_all_commits(repo)
                       for f in get_files(commit)])
    return ext_cnt.most_common(1)[0][0]
