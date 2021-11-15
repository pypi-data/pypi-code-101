from distutils.core import setup
setup(
  name = 'pip_for_cmd',         # How you named your package folder (MyLib)
  packages = ['pip_for_cmd'],   # Chose the same as "name"
  version = '1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Pip for CMD is a small project, and with it you can use pip in python codes and in the cmd!',   # Give a short description about your library
  long_description = """**Welcome to the PIP for CMD project!**
**What is PIP for CMD?**

**PIP for CMD** is a Python package that helps you with the pip package.
Its main goal is to make the pip experience more **user-friendly**
and more updates are going to be published soon.

**Where to get it**
The source code is currently published on GitHub at
https://github.com/PipForCMD/PIP_for_CMD.

**First step** (in the CMD)
```
pip install pip_for_cmd
```
**Second step** (now in your IDE)
```
import pip_for_cmd
```
**Third step**
```
pip_version()
update_pip()
package_installer()
```
choose which function you want to use.

**Dependencies**
- [os - Connects to the operating system and to the CMD.](https://docs.python.org/3/library/os.html)
- [pip - Using the original pip package to check pip versions.](https://pypi.org/project/pip/)

**License**
MIT(https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)

**Contact us!**

General questions and discussions can take place on the [PIP for CMD mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydatahttps://groups.google.com/u/6/g/pipforcmd).

**Thats it!**""",
  author = 'Omer Yelin',                   # Type in your name
  author_email = 'pipforcmd@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/PipForCMD/PIP_for_CMD',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PipForCMD/PIP_for_CMD/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['pip', 'cmd', 'python', 'python 3'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
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
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)