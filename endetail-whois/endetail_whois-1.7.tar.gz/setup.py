from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent

long_description = (this_directory / "README.rst").read_text()

setup(
    name='endetail_whois',
    packages=['endetail_whois'],
    version='1.7',
    license='MIT',
    description='Simple WHOIS function in Python for getting any domain information.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Petr Zachrdla',
    author_email='petr@zachrdla.cz',
    # url='https://github.com/zachrdlapetr/endetail_whois',
    keywords=['whois'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
