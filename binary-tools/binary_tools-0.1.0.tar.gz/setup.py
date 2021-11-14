import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='binary_tools',
    version='0.1.0',
    author='Guilherme Borges',
    author_email='guilherme@guilhermeborges.net',
    description='Pyhton tools for binary data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sgtpepperpt/binary_tools',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9'
)
