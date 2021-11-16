"""Tests for the module :mod:`jarpyvscode.usersettings`."""

# Standard library:
import os
import typing as t
from pathlib import Path

# 3rd party:
import pytest
from pytest import MonkeyPatch

# local:
import jarpyvscode.constants as c
import jarpyvscode.environment
import jarpyvscode.paths
import jarpyvscode.usersettings

test_data_set = [
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": "jarmac", "os": None},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": ["jarmac", "dbmac"], "os": None},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": "jarmac", "os": "osx"},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": ["jarmac", "dbmac"], "os": "osx"},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": "jarmac", "os": ["osx", "linux"]},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": ["jarmac", "dbmac"], "os": ["osx", "linux"]},
        100,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": None, "os": "osx"},
        50,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": "dbmac", "os": "osx"},
        50,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {
            "hosts": [
                "dbmac",
            ],
            "os": "osx",
        },
        50,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": "dbmac", "os": ["osx", "linux"]},
        50,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": ["dbmac", "dbmac"], "os": ["osx", "linux"]},
        50,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": None, "os": None},
        10,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {},
        0,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"hosts": None},
        0,
    ),
    pytest.param(
        "jarmac",
        "osx",
        {"os": None},
        0,
    ),
]


@pytest.mark.parametrize("hostname, os, host_setting, expected", test_data_set)
def test_determine_applicability_score(
    hostname: str,
    os: str,
    host_setting: t.Dict[str, t.Any],
    expected: int,
    monkeypatch: MonkeyPatch,
):
    """Test :func:`jarpyvscode.usersettings.determine_applicability_score`.

    Parameters
    ----------
    hostname
        Monkey patched host name
    os
        Monkey patched operating system
    host_setting
        Test object
    expected
        Expected applicability score
    monkeypatch
        Helper to conveniently monkeypatch host name and operating system.

    """
    monkeypatch.setattr(c, "HOSTNAME", hostname)  # type: ignore
    monkeypatch.setattr("jarpyvscode.environment.operating_system", lambda: os)
    result: int = jarpyvscode.usersettings.determine_applicability_score(host_setting)
    assert expected == result


test_data_set = [
    pytest.param(
        "jarmac",
        "osx",
        [{}],
        Path(str(os.getenv("JARROOT"))) if os.getenv("JARROOT", "") else Path.home(),
        id="jarmac w/o host_settings.json",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": None,
                "os": None,
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set w/o hosts/ os limitation",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": None,
                "os": "windows",
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path(str(os.getenv("JARROOT"))) if os.getenv("JARROOT", "") else Path.home(),
        id="jarmac with jarroot not set",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": None,
                "os": "osx",
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set and os limitation",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": "jarmac",
                "os": "osx",
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set and host & os limitation",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": ["jarmac", "dbmac"],
                "os": "osx",
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set and hosts & os limitation",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": "jarmac",
                "os": None,
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set and host limitation",
    ),
    pytest.param(
        "jarmac",
        "osx",
        [
            {
                "hosts": ["jarmac", "dbmac"],
                "os": None,
                "key": "jarpyvscode.jarroot",
                "val": "/Users/jamil",
            }
        ],
        Path("/Users/jamil"),
        id="jarmac with jarroot set and hosts limitation",
    ),
]


@pytest.mark.parametrize("hostname, os, host_settings, expected", test_data_set)
def test_jarroot(
    hostname: str,
    os: str,
    host_settings: t.List[t.Dict[str, t.Any]],
    expected: int,
    monkeypatch: MonkeyPatch,
):
    """Test :func:`jarpyvscode.paths.jarroot`.

    Parameters
    ----------
    hostname
        Monkey patched host name
    os
        Monkey patched operating system
    host_settings
        Monkey patched host settings
    expected
        Expected jarroot
    monkeypatch
        Helper to conveniently monkeypatch host name, operating system and
        host settings.

    """
    monkeypatch.setattr(c, "HOSTNAME", hostname)  # type: ignore
    monkeypatch.setattr("jarpyvscode.environment.operating_system", lambda: os)
    if not jarpyvscode.paths.host_settings_path().is_file():
        if not jarpyvscode.paths.host_settings_path().parent.is_dir():
            jarpyvscode.paths.host_settings_path().parent.mkdir(
                parents=True, exist_ok=True
            )
            jarpyvscode.paths.host_settings_path().touch()
    monkeypatch.setattr(
        "jarpyvscode.usersettings.read_host_settings", lambda: host_settings
    )
    result: Path = jarpyvscode.usersettings.jarroot()
    assert expected == result
