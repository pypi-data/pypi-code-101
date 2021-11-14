import setuptools

setuptools.setup(
    name='binary_tools',
    version='0.0.0',
    author='Guilherme Borges',
    author_email='guilherme@guilhermeborges.net',
    description='Pyhton tools for binary data',
    long_description='Suite of tools for binary operations '
                     'over standard Python types. Allows for byte or bit-wise granularity.',
    long_description_content_type='text/markdown',
    url='https://github.com/sgtpepperpt/binary_tools',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)
