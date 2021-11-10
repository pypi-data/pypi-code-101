import argparse
import csv
import requests
import subprocess
import sys

from typing import List, Optional
from urllib.parse import urlparse


def download_file(file_url, md5):
    file_name = file_url.split("/")[-1]
    sys.stdout.write(f"Downloading and verifying {file_name}... ")
    sys.stdout.flush()
    subprocess.check_output(["wget", file_url], stderr=subprocess.PIPE)
    h = subprocess.check_output(["md5sum", file_name])
    assert h == md5
    sys.stdout.write("done.")
    sys.stdout.flush()


def main(args: Optional[List[str]] = None):
    parser = argparse.ArgumentParser(
        description="Utility Python package to download Genome-in-a-Bottle data from their index files.")

    parser.add_argument("index", help="Index file or URL to get data links and hashes from.")

    p_args = parser.parse_args(args or sys.argv[1:])

    index = p_args.index
    index_parts = urlparse(index)

    if index_parts.scheme in ("http", "https") and index_parts.netloc == "github.com":
        path_parts = index_parts.path.split("/")
        if path_parts[3] == "blob":  # Non-raw GH content
            index = index_parts.scheme + "://" + index_parts.netloc + \
                "/".join(path_parts[:3]) + "/raw/" + "/".join(path_parts[4:])

        index_res = requests.get(index, allow_redirects=True)

        if index_res.status_code >= 300:
            print(f"Error: index request returned non-2XX status code: {index_res.status_code}")
            exit(1)

        index_contents = index_res.content.decode("utf-8").split("\n")

    else:
        with open(index, "r") as fh:
            index_contents = fh.read()

    index_reader = csv.DictReader(index_contents, delimiter="\t")

    for row in index_reader:
        if "FASTQ" in row:
            download_file(row["FASTQ"], row["FASTQ_MD5"])

        if "PAIRED_FASTQ" in row:
            download_file(row["PAIRED_FASTQ"], row["PAIRED_FASTQ_MD5"])


if __name__ == "__main__":
    main()
