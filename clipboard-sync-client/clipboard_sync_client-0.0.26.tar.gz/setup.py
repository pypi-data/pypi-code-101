from pathlib import Path
import re
from setuptools import setup

setup_dir = Path(__file__).resolve().parent
version = re.search(
    r'__version__ = "(.*)"',
    Path(setup_dir, 'clipboard_sync_client.py').open().read()
)
if version is None:
    raise SystemExit("Could not determine version to use")
version = version.group(1)

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='clipboard_sync_client',
    author='zkytech',
    author_email='zhangkunyuan@hotmail.com',
    url='https://github.com/zkytech/cross_platform_clipboard_sync',
    description='client for sync clipboard between different computers',
    long_description=Path(setup_dir, '../README.md').open().read(),
    long_description_content_type='text/markdown',
    license='MIT',
    py_modules=['clipboard_sync_client'],
    entry_points={
        "console_scripts": [
            "clipboard_sync_client = clipboard_sync_client:cli"
        ]
    },
    install_requires=required,
    version=version,
    python_requires='~=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: SunOS/Solaris",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "Topic :: System"
    ]
)