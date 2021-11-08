# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/
from setuptools import setup

setup(
  name = 'TwentyOneCardGame',         # How you named your package folder (MyLib)
  packages = ['TwentyOneCardGame'],   # Chose the same as "name"
  version = '1.21',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Basic game of Black Jack/21',
  author = 'Patrick Löwe',
  author_email = 'patricklowe33@gmail.com',
  #url = 'https://github.com/user/reponame',
  #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['GAME', '21', 'BLACK JACK'],
  #install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'],
)