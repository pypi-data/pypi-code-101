#!/usr/bin/env python

import json
import re
import subprocess
import sys
from collections import OrderedDict
from distutils.version import LooseVersion

import terminaltables
import toml

pipfile_packages = list(toml.load("Pipfile").get("packages").keys())


def get_package_versions(package_type='--uptodate'):
    """
    Retrieve a list of outdated packages from pip. Calls:
        pip list [--outdated|--uptodate] --format=json [--not-required] [--user] [--local]
    """
    cmd = f"pip list {package_type} --retries=1 --disable-pip-version-check --format=json --local"
    try:
        cmd_response = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    except subprocess.CalledProcessError as e:
        print("The pip command did not succeed: {stderr}".format(stderr=e.stderr.decode("utf-8")))
        sys.exit(1)

    # The pip command exited with 0 but we have stderr content:
    if cmd_response.stderr:
        if "NewConnectionError" in cmd_response.stderr.decode("utf-8").strip():
            print("\npip indicated that it has connection problems. " "Please check your network.")
            sys.exit(1)

    cmd_response_string = cmd_response.stdout.decode("utf-8").strip()

    if not cmd_response_string:
        print("No outdated packages. \\o/")
        sys.exit(0)

    try:
        return json.loads(cmd_response_string)
    except Exception:  # Py2 raises ValueError, Py3 JSONEexception
        print("Unable to parse the version list from pip. " "Does `pip list --format=json` work for you?")
        sys.exit(1)


if __name__ == "__main__":

    print("Loading package versions...\n")

    # Unchanged Packages
    unchanged = get_package_versions(package_type='--uptodate')

    packages = {
        "major": [],
        "minor": [],
        "unknown": [],
        "unchanged": unchanged,
    }

    # Fetch all outdated packages and sort them into major/minor/unknown.
    for package in get_package_versions(package_type='--outdated'):
        if not package["name"] in pipfile_packages:
            continue
        # No version info
        if "latest_version" not in package or "version" not in package:
            packages["unknown"].append(package)
            continue

        try:
            latest = LooseVersion(package["latest_version"])
            current = LooseVersion(package["version"])
        except ValueError:
            # Unable to parse the version into anything useful
            packages["unknown"].append(package)
            continue

        if current > latest:
            packages["unknown"].append(package)
            continue

        # Current and latest package version is the same. If this happens,
        # it's likely a bug with the version parsing.
        if current == latest:
            packages["unchanged"].append(package)
            continue

        # Major upgrade (first version number)
        if latest.version[0] > current.version[0]:
            packages["major"].append(package)
            continue
        # Minor upgrade (second version number)
        elif latest.version[1] > current.version[1]:
            packages["minor"].append(package)
            continue

    table_data = OrderedDict()

    def columns(package):
        # Generate the columsn for the table(s) for each package
        # Name | Current Version | Latest Version | pypi String

        name = package.get("name")
        current_version = package.get("version", None)
        latest_version = package.get("latest_version", None)
        help_string = "https://pypi.python.org/pypi/{}".format(package["name"])

        return [
            name,
            current_version or "Unknown",
            latest_version or current_version or "Unknown",
            help_string,
        ]

    for key, label in [
        ("major", "Major Release Update"),
        ("minor", "Minor Release Update"),
        ("unchanged", "Current Packages"),
        ("unknown", "Unknown Package Release Status"),
    ]:
        if packages[key]:
            if key not in table_data:
                table_data[key] = []

            table_data[key].append([label, "Version", "Latest"]),
            for package in packages[key]:
                if not package["name"] in pipfile_packages:
                    continue
                table_data[key].append(columns(package))

    # Table output class
    for key, data in table_data.items():
        table = terminaltables.AsciiTable(data)
        print(table.table)
