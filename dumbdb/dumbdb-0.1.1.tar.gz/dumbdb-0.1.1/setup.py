from setuptools import setup

README = open('README.md').read()

setup(
    name='dumbdb',
    # packages=['dumbdb'],
    version='0.1.1',
    license='MIT',
    description=' A super easy, but really really bad DBMS ',
    # long_description=README,
    long_description_content_type="text/markdown",
    author='Elias Amha',
    author_email='oxecho@wearehackerone.com',
    url='https://github.com/0xecho/dumbdb',
    download_url='https://github.com/0xecho/dumbdb/archive/v_01.tar.gz',
    keywords=["db", "database", "python", "peewee", "sqlite", "mysql", "postgresql", "mongo", "orm"],
    classifiers=[
        'Development Status :: 3 - Alpha',
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