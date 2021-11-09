from distutils.core import setup

from setuptools import find_packages, setup

long_description = u'\n\n'.join((
    open('README.rst').read(),
))

setup(
  name = 'pipenv_update_check',
  package_dir={"": "src"},
    packages=find_packages(
        where="src",
    ),         # How you named your package folder (MyLib)
  # Chose the same as "name"
  version = '0.2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Pip environment update check',   # Give a short description about your library
  author = 'cuneyt',                   # Type in your name
  author_email = 'cuneyt@3bfab.com',      # Type in your E-Mail
  url = 'https://github.com/CuneytTaha/pipenv-update-check',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CuneytTaha/pipenv-update-check/archive/refs/tags/v_0.2.2.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'terminaltables',
          'toml',
      ],
  classifiers=[
  ],
  package_data={},
    include_package_data=True,
    entry_points={'console_scripts': [
        'pipenv-update-check = pipenv_update_check:main',
    ]},
)
