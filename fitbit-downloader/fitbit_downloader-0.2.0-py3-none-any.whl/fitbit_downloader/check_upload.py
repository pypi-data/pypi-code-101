import datetime

from fs import open_fs, path

from fitbit_downloader.config import Dataset, Config
from fitbit_downloader.constants import DATE_FORMAT


def last_full_upload(config: Config) -> datetime.date:
    fs = open_fs(config.download.fs_url)
    if not fs.exists(config.download.fs_folder):
        # No existing data at all, start from begin date
        return config.download.data_begin_date
    dates = [_last_uploaded(dataset, config) for dataset in config.download.datasets]
    if not dates:
        # Folder existed but no downloaded data, start from begin date
        return config.download.data_begin_date
    return min(dates)


def _last_uploaded(dataset: Dataset, config: Config) -> datetime.date:
    fs = open_fs(config.download.fs_url)
    out_folder = path.join(config.download.fs_folder, dataset.value)
    if not fs.exists(out_folder):
        # No existing data at all, start from begin date
        return config.download.data_begin_date
    dates = [_file_to_date(file) for file in fs.listdir(out_folder)]
    return max(dates)


def _file_to_date(file: str) -> datetime.date:
    name, ext = file.split(".")
    if ext != "json":
        raise ValueError(f"got unexpected file {file}")
    dt = datetime.datetime.strptime(name, DATE_FORMAT)
    return dt.date()
