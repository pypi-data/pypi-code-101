import datetime

from fitbit_downloader.check_upload import last_full_upload
from fitbit_downloader.config import Config
from fitbit_downloader.dateutils import yesterday
from fitbit_downloader.download import download_data


def sync_data(config: Config):
    last_uploaded = last_full_upload(config)
    delta = yesterday() - last_uploaded

    for i in range(1, delta.days + 1):
        day = last_uploaded + datetime.timedelta(days=i)
        download_data(config, day)


def main():
    config = Config.load_recursive()
    sync_data(config)


if __name__ == "__main__":
    main()
