from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Generating Python Discord bots'
LONG_DESCRIPTION = 'Helps is generating ready-made discord bots in python easily.'

# Setting up
setup(
    name="ascord",
    version=VERSION,
    author="Kavin Jindal",
    author_email="kavinsjindal@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= '''
    
# AsCord 1.0.0

![AsCord](https://img.shields.io/badge/AsCord-1.0.0-blue)


---

# Update log

**Update 0.0.7**: Fixed the bot presence bug

**Update 0.0.4**: Fixed the cogs generation.

**Update 0.0.3**: Fixed a bug.

**Update 0.0.2**: Fixed the `__init__.py` file.

**Update 0.0.1**: Initial release of AsCord.

---

# Info: 

* This package makes it easy for python developers to generate `discord.py` bots. 
* With not more than `3 lines of code`, you will be able to generate fully functional discord bots. 
* You are also provided with an option of either generating discord bots WITH cogs or WITHOUT cogs.

# Installation

Type the following command to install the package

```python
pip install ascord
```
* or

```python
pip3 install ascord
```
# Usage

* Importing the module

```python
 import ascord
 ```

* Generate a bot without cogs

```python 
ascord.as_cord("BOT_NAME", "BOT_PREFIX", "BOT_TOKEN")
```

* Generate a bot with cogs

```python
ascord.as_cogs("BOT_NAME", "BOT_PREFIX", "BOT_TOKEN")
```

--> After the script is generated, you can run the bot.


# Credits

**Developed by: Kavin Jindal**


    ''',
    packages=find_packages(),
    install_requires=['discord'],
    keywords=['python','discord', 'discord.py', 'discord bots', 'discord python', 'bots'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)