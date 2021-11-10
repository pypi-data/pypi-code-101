import fnmatch
from typing import Any, Dict, List


class GitHubChangeset:

    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data

    @property
    def filenames(self) -> List[str]:
        filenames: List[str] = []
        # return["Directory.Build.targets"]
        for item in self._data.get("files", []):
            filenames.append(item["filename"])
        return filenames

    def find_relevant_changes(self, dependencies: List[str]) -> List[str]:
        relevant_changes: List[str] = []

        dependencies = list(filter(None, dependencies))
        matches: List[str] = []
        for pattern in [x for x in dependencies if x[0] != "!"]:
            for match in fnmatch.filter(self.filenames, pattern):
                matches.append(match)

        unmatch: List[str] = []
        for pattern in [x[1:] for x in dependencies if x[0] == "!"]:
            for match in fnmatch.filter(matches, pattern):
                unmatch.append(match)

        relevant_changes = list(set(matches).difference(set(unmatch)))
        relevant_changes.sort()
        return relevant_changes
