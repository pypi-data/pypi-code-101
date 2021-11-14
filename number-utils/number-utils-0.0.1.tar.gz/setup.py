import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='number-utils',
    version='0.0.1',
    author='Debashish Palit',
    author_email='dpalit17@outlook.com',
    description='A library of functions related to prime numbers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/deb17/number-utils',
    packages=['number_utils'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)
