from distutils.core import setup

setup(
    name = 'speako',
    version = '0.1.0',
    author = 'OTTAA Dev Team',
    author_email = 'info@ottaaproject.com',
    packages = ['speako', 'speako.source'],
    scripts = ['ipy-nbs/basic_use.ipynb',
                'ipy-nbs/interactive_prediction.ipynb',
                'ipy-nbs/mult_train.ipynb',
                'ipy-nbs/saving_cache.ipynb',               
                ],
    data_files = ['speako/lang/es-verbs.txt',
                  'speako/lang/en-verbs.txt',
                  ],
    url = 'https://ottaa-project.github.io/PictogramsPredictionsLibrary/',
    license = '',
    description = 'package for language prediction used by OTTAA apps',
    long_description = open('README.txt').read(),
    install_requires=[],
)    