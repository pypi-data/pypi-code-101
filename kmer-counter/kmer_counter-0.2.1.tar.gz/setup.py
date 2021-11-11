# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kmer_counter']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0', 'py2bit>=0.3.0,<0.4.0']

entry_points = \
{'console_scripts': ['kmer_counter = kmer_counter.cli:main']}

setup_kwargs = {
    'name': 'kmer-counter',
    'version': '0.2.1',
    'description': 'Count kmers in regions or at SNVs or at indel breakpoints.',
    'long_description': '# kmer_counter\n\nCount kmers in regions or at SNVs or at indel breakpoints.\n\n## Requirements\n\nkmer_counter requires Python 3.7 or above.\n\n## Installation\n\nWith `pip`:\n```bash\npip install kmer_counter\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npipx install kmer_counter\n```\n\n## Usage \n\n### Counting k-mers at SNVs\nTo count the 3-mers at SNVs do:\n```bash\nkmer_counter snv {genome}.2bit {snv_file}\n```\nWhere the `{snv_file}` should be a vcf-like text file where the first four columns are: Chromosome, Position, Ref_Allele, Alt_Allele. Fx:\n\n```\nchr1  1000000  A G\nchr1  1000200  G C\nchr1  1000300  A T\nchr1  1000500  C G\n```\nComments or header lines starting with "#" are allowed and will be ignored and any additional columns are also allowed but ignored. So a vcf file is also a valid input file.\nThe Ref_Allele column should match the reference genome provided by the 2bit file. 2bit files can be downloaded from:\n`https://hgdownload.cse.ucsc.edu/goldenpath/{genome}/bigZips/{genome}.2bit` where `{genome}` is a valid UCSC genome assembly name (fx. "hg38").\n\n### Counting k-mers in genomic regions\nTo count all 5-mers in a bed file called {regions}.bed do:\n```\nkmer_counter background --bed {regions}.bed -radius 2 {genome}.2bit\n```\nBy default all k-mers where the middle base is not A or C will be reverse complemented before being counted. This behaviour can be changed using the "--reverse_complement_method".\nIf we instead wants to count 4-mers, we can use the "--before_after" option: \n```\nkmer_counter background --bed {regions}.bed --before_after 2 1 {genome}.2bit\n```\nWhen this option is used the default is not to reverse complement any of the k-mers but count all.\n\n### Counting k-mers at indels\nTo count one of the possible insertion breakpoint 4-mer for each insertion in a vcf-like file with variants do:\n```\nkmer_counter indel -r 2 --sample {genome}.2bit {variants} ins\n```\nAnd for deletion start breakpoints:\n```\nkmer_counter indel -r 2 --sample {genome}.2bit {variants} del_start\n```\nThis will produce 2 counts for each deletion; one for the start breakpoint and one for the reverse complement at the k-mer at end breakpoint.',
    'author': 'Søren Besenbacher',
    'author_email': 'besenbacher@clin.au.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/besenbacher/kmer_counter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
