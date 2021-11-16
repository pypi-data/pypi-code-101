# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multidirectorycorpusreader']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'multidirectorycorpusreader',
    'version': '0.2.1',
    'description': '',
    'long_description': "# MultiDirectoryCorpusReader\n\nMultiDirectoryCorpusReader provides an easy iterator for multi directory source globbing of raw\ntext files which can be used either streaming or in memory.\n\n## Installation\n\nIt can be installed directly from github using:\n\n```sh\n#> python -m pip install git+https://github.com/blackplague/multidirectorycorpusreader.git\n```\n\n## Usage example\n\nThe minimum viable usage is to supply a list of source directories and a list of globbing filters.\n\n```python\nmdcr = MultiDirectoryCorpusReader(\n    source_directories=['data/source1', 'data/source2'],\n    glob_filters=['*.txt', '*.msg', '*.doc', '*.text'])\n```\n\nIt is possible to pass a preprocess function to the script, this could for example be the\n*simple_preprocess* function from the [Gensim][gensim-url] library. This will also print the progress\nduring the streaming of the files.\n\n```python\nfrom gensim.utils import simple_preprocess\n\nmdcr = MultiDirectoryCorpusReader(\n    source_directories=['data/source1', 'data/source2'],\n    glob_filters=['*.txt', '*.msg', '*.doc', '*.text'],\n    preprocess_function=simple_preprocess,\n    print_progress=True)\n```\n\nThis example shows how to supply a preprocess function that you have written yourself. In addition\nthis will also read all files into memory and print progress during.\n\n```python\ndef preprocessor_tokenize_remove_a(s: str) -> List[str]:\n    return s.replace('a', '').split(' ')\n\nmdcr = MultiDirectoryCorpusReader(\n    source_directories=['data/source1', 'data/source2'],\n    glob_filters=['*.txt', '*.msg', '*.doc', '*.text'],\n    preprocess_function=preprocessor_tokenize_remove_a,\n    in_memory=True,\n    print_progress=True)\n```\n\n## Release History\n\n* 0.2.1\n  * Makes the MultiDirectoryCorpusReader available through ```from multidirectorycorpusreader import MultiDirectoryCorpusReader```\n* 0.2.0\n  * The first proper release\n\n## Meta\n\nMichael Andersen - michael10andersen+mdcr -[at]- gmail.com - [Github](https://github.com/blackplague/)\n\nDistributed under the LGPL3 license. See ``LICENSE`` for more information.\n\n<!-- Markdown link & img dfn's -->\n[gensim-url]: https://radimrehurek.com/gensim/\n",
    'author': 'Michael Andersen',
    'author_email': 'michael10andersen+mdcr@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
