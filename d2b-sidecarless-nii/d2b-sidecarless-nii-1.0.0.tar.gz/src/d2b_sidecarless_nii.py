from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

from d2b.hookspecs import hookimpl


if TYPE_CHECKING:
    from d2b.d2b import D2B

try:
    import pytest  # type: ignore
except ModuleNotFoundError:
    pytest = None

__version__ = "1.0.0"


@hookimpl(tryfirst=True)
def collect_files(
    d2b_dir: Path,
    d2b: D2B,
) -> list[Path] | None:
    # find the nii files which don't have sidecars
    sidecarless_niis = find_sidecarless_nii(d2b_dir)
    sidecars = [expected_sidecar(fp) for fp in sidecarless_niis]

    # do some logging
    _log_num_found_sidecarless_niis(d2b.logger, len(sidecarless_niis))
    _log_all_found_sidecarless_niis(d2b.logger, sidecarless_niis)

    # create empty sidecars
    for fp in sidecars:
        fp.write_text(json.dumps({}))

    # do some more logging
    _log_num_sidecars_created(d2b.logger, len(sidecars))
    _log_all_sidecars_created(d2b.logger, sidecars)

    # return the newly-created empty sidecars
    return sidecars


@hookimpl
def pre_run_logs(logger: logging.Logger):
    logger.info(f"d2b-sidecarless-nii:version: {__version__}")


def find_sidecarless_nii(root_dir: str | Path) -> list[Path]:
    _root_dir = Path(root_dir)
    return sorted(
        nii for nii in _root_dir.rglob("*.nii*") if not expected_sidecar(nii).exists()
    )


def expected_sidecar(fp: str | Path) -> Path:
    _fp = Path(fp)
    sidecar_name = re.sub(r".nii(.gz)?$", ".json", _fp.name)
    return _fp.parent / sidecar_name


def _log_num_found_sidecarless_niis(logger: logging.Logger, n_niis: int):
    logger.info(f"Found [{n_niis}] NIfTI files without associated sidecar files.")


def _log_all_found_sidecarless_niis(logger: logging.Logger, niis: list[Path]):
    for nii in niis:
        logger.debug(f"➖ File [{nii}] has no associated sidecar file.")


def _log_num_sidecars_created(logger: logging.Logger, n_sidecars: int):
    logger.info(f"Generated [{n_sidecars}] sidecar files.")


def _log_all_sidecars_created(logger: logging.Logger, sidecars: list[Path]):
    for sidecar in sidecars:
        logger.debug(f"➖ Generated sidecar file [{sidecar}]")


if pytest:

    @pytest.mark.parametrize(
        ("path", "expected"),
        [
            ("a.nii", Path("a.json")),
            ("a/b/c.nii", Path("a/b/c.json")),
            ("a.nii.gz", Path("a.json")),
            ("a/b/c.nii.gz", Path("a/b/c.json")),
            ("poorly.named.nii.file.nii", Path("poorly.named.nii.file.json")),
            ("a/b/poorly.named.nii.file.nii", Path("a/b/poorly.named.nii.file.json")),
            ("poorly.named.nii.file.nii.gz", Path("poorly.named.nii.file.json")),
            (
                "a/b/poorly.named.nii.file.nii.gz",
                Path("a/b/poorly.named.nii.file.json"),
            ),
        ],
    )
    def test_expected_sidecar(path: str, expected: Path):
        assert expected_sidecar(path) == expected

    @pytest.mark.parametrize(
        ("files", "expected"),
        [
            (
                ["a.nii", "a.json", "b.nii.gz", "b.json", "c.nii", "d.nii.gz"],
                [Path("c.nii"), Path("d.nii.gz")],
            ),
            (
                [
                    "subdir/a.nii",
                    "subdir/a.json",
                    "subdir/b.nii.gz",
                    "subdir/b.json",
                    "subdir/c.nii",
                    "subdir/d.nii.gz",
                ],
                [Path("subdir/c.nii"), Path("subdir/d.nii.gz")],
            ),
        ],
    )
    def test_find_sidecarless_nii(tmpdir: str, files: list[str], expected: list[Path]):
        _tmpdir = Path(tmpdir)

        # create the sample files
        for fp in map(lambda fn: _tmpdir / fn, files):
            fp.parent.mkdir(exist_ok=True, parents=True)
            fp.write_text("")

        rel_paths = [fp.relative_to(_tmpdir) for fp in find_sidecarless_nii(_tmpdir)]
        assert rel_paths == expected
