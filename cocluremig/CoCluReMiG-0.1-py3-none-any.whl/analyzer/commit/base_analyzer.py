"""
Base classes for commit analytics
"""
import functools
import logging
from typing import Callable, cast, List, Optional, TypeVar, Union

import git

from cocluremig.utils import tweaks

T = TypeVar('T')
"""Single Blob metric result"""

V = TypeVar('V')
"""Aggregated repo metric"""


class RepoFileMetricAnalyzer:
    """
        Analyses the given Repo for a given metric

        On consecuting commit-calls works incrementally
        by caching and working on the commits' diffs
    """

    def __init__(self,
                 repo: git.Repo,
                 metric_func: Callable[[git.Object], T],
                 aggregator_func: Optional[Callable[[Union[T, V], Union[T, V]], V]] = None,
                 aggregator_init: Optional[Union[T, V]] = None,
                 path_filter: Optional[Callable[[str], bool]] = None):
        """
        Initalizes the analyzer

        @param repo: the git repository to work on
        @param metric_func:
                a metric to retrieve from the repository's files
        @param aggregator_func:
                a function to aggregate the metric values
                (default: list of results creation)
        @param aggregator_init:
                the neutral element of the aggregation function
        @param path_filter: path/file skipping filter
        """
        logging.debug("Creating Analyzer")
        self.__repo = repo
        self.__metric_func = metric_func
        if aggregator_func:
            self.__aggregator_func = aggregator_func
            self.__aggregator_init = aggregator_init
        # if no aggregation function is given use list concatenation
        else:
            self.__aggregator_func = lambda x, y: x + y if isinstance(y, list) else x + [y]
            self.__aggregator_init = []
        self.__path_filter = path_filter
        # per instance cache
        cache_size = tweaks.get_cache_size()
        logging.debug("Cache size: %i", cache_size)
        self._apply_metric = \
            functools.lru_cache(maxsize=cache_size)(self._apply_metric)  # type: ignore

    def apply_metric(self, sha: Union[str, git.Object]) -> V:
        """
        calculates the metric for given commit

        @param sha: the commit to analyze
        @return: metric
        """
        if isinstance(sha, str):
            sha = self.__repo.commit(sha)
        if sha.type == "tag":
            # recursive call because tag-object can point to other tag-object
            return self.apply_metric(sha.object)
        if sha.type == "commit":
            logging.debug("analyzing commit %s", sha.hexsha)
            return self._apply_metric(sha.tree)
        raise ValueError("Illegal Object Type", (self.__repo, sha))

    def _apply_metric(self, sha: git.Object) -> Union[T, V]:
        logging.log(logging.DEBUG - 5, "Processing %s", (sha.type, sha.hexsha))
        try:
            if sha.type == "blob":
                return self.__metric_func(sha)
            if sha.type == "tree":
                cast(git.Tree, sha)
                if self.__path_filter:
                    if not self.__path_filter(sha.path):
                        return self.__aggregator_init
                # Error in gitPython documentation so iterate over blobs and trees seperately
                vals: List[Union[T, V]] = [self._apply_metric(gitobject) for gitobject in sha.blobs]
                vals += [self._apply_metric(gitobject) for gitobject in sha.trees]
                if None in vals:
                    logging.warning("None Value detected: %i", vals.index(None))
                return functools.reduce(self.__aggregator_func, vals, self.__aggregator_init)
            # somehow sha can also become a submodule, ignore those
            raise ValueError("Illegal Object Type", (self.__repo, sha.path, sha.hexsha, sha.type))
        except RecursionError as error:
            raise ValueError((self.__repo, sha)) from error
