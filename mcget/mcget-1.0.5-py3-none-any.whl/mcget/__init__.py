#!/usr/bin/env python3
"""Download Minecraft server and launcher latest release."""

# Copyright (C) 2019 J.Goutin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser as _ArgumentParser
from hashlib import sha1 as _sha1
from json import loads as _loads
from lzma import decompress as _decompress
from os.path import join as _join, isfile as _isfile, basename as _basename
from concurrent.futures import ThreadPoolExecutor as _ThreadPoolExecutor
from urllib.request import urlopen as _urlopen

_MOJANG_BASE_URL = "https://launchermeta.mojang.com/mc"
_MANIFEST_URL = f"{_MOJANG_BASE_URL}/game/version_manifest.json"
_LAUNCHER_JSON_URL = f"{_MOJANG_BASE_URL}/launcher.json"
__version__ = "1.0.5"


def get_server(out_dir=".", quiet=False):
    """
    Download latest release of Minecraft server ("server.jar").

    Parameters
    ----------
    out_dir: str
        "server.jar" destination directory.
    quiet: bool
        If True, does not print output.
    """
    out_file = _join(out_dir, "server.jar")

    with _urlopen(_MANIFEST_URL) as manifest_json:
        manifest = _loads(manifest_json.read())

    latest = manifest["latest"]["release"]

    for version in manifest["versions"]:
        if version["id"] == latest:
            version_json_url = version["url"]
            break
    else:
        raise RuntimeError(f"Server version {latest} not found in versions list.")

    with _urlopen(version_json_url) as version_json:
        server = _loads(version_json.read())["downloads"]["server"]

    checksum = server["sha1"]
    if _already_exists(out_file, checksum, quiet):
        return

    with _urlopen(server["url"]) as server_file:
        server_bytes = server_file.read()

    _verify_and_save(out_file, server_bytes, checksum, quiet)


def get_launcher(out_dir=".", quiet=False):
    """
    Download latest release of Minecraft Java launcher ("launcher.jar").

    Parameters
    ----------
    out_dir: str
        "server.jar" destination directory.
    quiet: bool
        If True, does not print output.
    """
    out_file = _join(out_dir, "launcher.jar")

    with _urlopen(_LAUNCHER_JSON_URL) as launcher_json:
        launcher_java = _loads(launcher_json.read())["java"]

    checksum = launcher_java["sha1"]
    if _already_exists(out_file, checksum, quiet):
        return

    with _urlopen(launcher_java["lzma"]["url"]) as lzma_file:
        launcher_bytes = _decompress(lzma_file.read())

    _verify_and_save(out_file, launcher_bytes, checksum, quiet)


def _verify_and_save(out_file, data, sha1_sum, quiet):
    """
    Verify checksum and save file locally.

    Parameters
    ----------
    out_file : str
        File destination.
    data : bytes
        File content
    sha1_sum : str
        SHA1 sum Hex digest to verify.
    """
    checksum = _sha1()
    checksum.update(data)
    if checksum.hexdigest() != sha1_sum:
        raise RuntimeError(f'"{_basename(out_file)}" checksum does not match.')

    updated = _isfile(out_file)
    with open(out_file, "wb") as file:
        file.write(data)

    if not quiet:
        print(
            f'"{_basename(out_file)}" has been {"updated" if updated else "installed"}.'
        )


def _already_exists(file_name, sha1_sum, quiet):
    """
    Checks if file with same name and checksum already exists.

    Parameters
    ----------
    file_name : str:
        File name to verify.
    sha1_sum : str
        SHA1 sum Hex digest to verify.

    Returns
    -------
    not_exists: bool
        True if file with same version already exist.
    """
    if _isfile(file_name):
        checksum = _sha1()
        with open(file_name, "rb") as file:
            checksum.update(file.read())

        if checksum.hexdigest() == sha1_sum:
            if not quiet:
                print(f'"{_basename(file_name)}" is up to date.')
            return True

    return False


def _run_command():
    """
    Command line interface
    """
    parser = _ArgumentParser(
        prog="mcget",
        description='"mcget" is a simple tool to download or update Minecraft Java '
        'server ("server.jar") and launcher ("launcher.jar") in a specified '
        "directory.",
    )
    parser.add_argument(
        "--launcher", "-l", action="store_true", help="Download or update launcher."
    )
    parser.add_argument(
        "--server", "-s", action="store_true", help="Download or update server."
    )
    parser.add_argument("--out_dir", "-o", default=".", help="Destination directory.")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode.")
    parser.add_argument(
        "--version", action="store_true", help="Print version and exit."
    )

    try:
        args = parser.parse_args()

        if args.version:
            parser.exit(message=f"mcget {__version__}\n")

        elif not args.launcher and not args.server:
            parser.error(
                'Require at least one of "--launcher" or "--server" arguments.'
            )

        kwargs = dict(out_dir=args.out_dir, quiet=args.quiet)
        futures = []
        success = True
        with _ThreadPoolExecutor() as executor:
            if args.launcher:
                futures.append(executor.submit(get_launcher, **kwargs))

            if args.server:
                futures.append(executor.submit(get_server, **kwargs))

            for future in futures:
                try:
                    future.result()
                except RuntimeError as error:
                    print(f"Error: {error}")
                    success = False

        if not success:
            parser.error("Operation failed")

    except KeyboardInterrupt:
        parser.exit(message="User interruption")


if __name__ == "__main__":
    _run_command()
