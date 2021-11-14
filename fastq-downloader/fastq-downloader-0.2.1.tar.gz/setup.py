# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastq_downloader', 'fastq_downloader.helper', 'fastq_downloader.snakemake']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4', 'click', 'httpx', 'lxml']

setup_kwargs = {
    'name': 'fastq-downloader',
    'version': '0.2.1',
    'description': '',
    'long_description': "# Fastq Downloader (WIP)\nuse this [snakemake script](https://gist.github.com/TTTPOB/1a8a960474a6a784f2da215b03ab3cc9) to get more fluent experience.\n\nThis python package let you download fastq files from ena.\nIt can automatic merge and rename fastq files based on the input file provided.\n\n## How to use\nauto merge multiple files of paired end reads are not tested now, but should be usable\n```bash\nconda create --name fastq-download -c conda-forge -c hcc -c bioconda aspera-cli snakemake httpx lxml click beautifulsoup4 python=3.9\n## use what ever you want to download the gist mentioned above to thisname.smk\n## download whl file from github release of this project to thisname.whl\nconda activate fastq-download\npip install thisname.whl\n## make sure to create an infotsv before, you can just copy from the geo website,\n## then go to vim, type :set paste to get into paste mode, paste the table into vim,\n## save the file as whatever name you want, then exit vim\n## the white space will be auto convert to underscore\n## refresh_acc need to be False if you don't want to query again the accesion number,\n## or due to the recreation of the link file, all files are to be downloaded.\npython3 -m fastq_download --infotsv thisname.tsv --outdir thisname --refresh_acc False\n```\n\n## todo\n  - [ ] test for paired-end reads run merge\n  - [ ] publish to bioconda\n  - [x] if fail, retry\n  - [x] use dag to run the pipeline (sort of, implemented by using snakemake)\n  - [x] option to resume download when md5 not match\n  - [x] option to continue from last time download\n  - [x] implement second level parallelization\n",
    'author': 'tpob',
    'author_email': 'tpob@tpob.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
