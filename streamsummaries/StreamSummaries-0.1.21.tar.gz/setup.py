from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'StreamSummaries',         # How you named your package folder (MyLib)
  packages = ['StreamSummaries'],   # Chose the same as "name"
  version = '0.1.21',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Algorithms for Stream Summary.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Cristiano Garcia',                   # Type in your name
  author_email = 'cristianooo@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/cristianomg10/StreamSummaries',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/cristianomg10/StreamSummaries/archive/refs/tags/v0.1.21.tar.gz',    # I explain this later on
  keywords = ['stream', 'summary'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          #'validators',
          #'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)