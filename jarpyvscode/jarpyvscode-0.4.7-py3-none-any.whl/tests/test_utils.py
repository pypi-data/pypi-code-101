"""Test module :mod:`jarpyvscode.utils`."""

# Standard library:
import os
from pathlib import Path

# 3rd party:
import pytest

# local:
import jarpyvscode.usersettings
import jarpyvscode.utils

test_data_set = [
    pytest.param(
        Path("C:/Users/DUMMY/bla/blubs"),
        Path("C:/Users/DUMMY/bla/blubs"),
        id="no adaption needed",
    ),
    pytest.param(
        Path("C:/Users/jamil/repos/jar"),
        jarpyvscode.usersettings.jarroot() / "repos/jar",
        id="jarpc path forward slashs",
    ),
    pytest.param(
        Path(r"C:\Users\jamil\repos/jar"),
        jarpyvscode.usersettings.jarroot() / "repos/jar",
        id="jarpc path backslashs",
    ),
    pytest.param(
        Path(r"C:\\Users\\jamil\\repos/jar"),
        jarpyvscode.usersettings.jarroot() / "repos/jar",
        id="jarpc path double backslashs",
    ),
    pytest.param(
        Path(jarpyvscode.usersettings.jarroot()),
        jarpyvscode.usersettings.jarroot(),
        id="Current JARROOT to be untouched",
    ),
    pytest.param(
        jarpyvscode.usersettings.jarroot() / "repos/jar",
        jarpyvscode.usersettings.jarroot() / "repos/jar",
        id="Child of current JARROOT to be untouched",
    ),
    pytest.param(
        Path("C:/Users/JamilRaichouni2/repos/assets"),
        jarpyvscode.usersettings.jarroot() / "repos/assets",
        id="T4C server path with forward slashs",
    ),
    pytest.param(
        Path(
            "file:///home/jamil/"
            "Library/Application%20Support/Code/User/globalStorage/"
            "jamilraichouni.jarpyvscode/workspaces/jarpyvscode.code-workspace"
        ),
        Path(
            f"file://{jarpyvscode.usersettings.jarroot()}/"
            "Library/Application%20Support/Code/User/globalStorage/"
            "jamilraichouni.jarpyvscode/workspaces/jarpyvscode.code-workspace"
        ),
        id="openedPathsList / workspace / configPath",
    ),
]


@pytest.mark.skipif(  # type: ignore
    os.getenv("CI", "false") == "true", reason="Cannot run this test on GitLab"
)
@pytest.mark.parametrize("input_data, expected", test_data_set)
def test_adapt_jarroot_in_path(input_data: str, expected: str):
    result = Path(jarpyvscode.utils.adapt_jarroot_in_path(old_path=input_data, sep="/"))
    assert expected == result
