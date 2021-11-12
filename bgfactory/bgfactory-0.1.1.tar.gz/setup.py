#!/usr/bin/env python

from distutils.core import setup

# from pathlib import Path
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text()

setup(name='bgfactory',
      version='0.1.1',
      description='Board Game Factory - a framework for creating and scaling up production of  vector graphics assets,'
                  ' e.g. for board games.',
      long_description='file: README.md',
      long_description_content_type='text/markdown',
      author='Adam Volný',
      author_email='adam.volny@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=['bgfactory', 'bgfactory.common', 'bgfactory.components'],
      package_dir = {'': 'src'},
      url='https://github.com/avolny/board-game-factory',  # Provide either the link to your github or to your website
      # download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
      keywords=['board', 'game', 'factory', 'bgf', 'vector', 'graphics'],  # Keywords that define your package best
      install_requires=[  # I get to this in a second
            'cairocffi',
            'pangocffi',
            'pillow',
      ],
      classifiers=[
            'Development Status :: 3 - Alpha',
            # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
            'Intended Audience :: Developers',  # Define that your audience are developers
            'Topic :: Multimedia :: Graphics',
            'License :: OSI Approved :: MIT License',  # Again, pick a license
            'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
            # 'Programming Language :: Python :: 3.4',
            # 'Programming Language :: Python :: 3.5',
            # 'Programming Language :: Python :: 3.6',
      ],
     )