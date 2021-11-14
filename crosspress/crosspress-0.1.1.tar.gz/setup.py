import crosspress
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='crosspress',
    version=crosspress.version,
    author='Vadimhtml',
    author_email='i@vadimhtml.ru',
    packages=['crosspress'],
    url='https://gitlab.com/Vadimhtml/crosspress',
    license='MIT',
    description='Cross-platform lightweight keyboard simulator',
    keywords='keyboard simulator Windows Linux macOS',  # todo simulator, emulator, tap, press?

    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=["pyobjc-framework-Quartz; sys_platform=='darwin'"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',  # todo Supported?
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',  # todo Python 2?
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    entry_points={
        'console_scripts': ['crosspress=crosspress.crosspress:main'],
    },
)
