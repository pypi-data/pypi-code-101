from pathlib import Path

from setuptools import find_packages, setup

from smartparams import __version__

setup(
    name='SmartParams',
    version=__version__,
    author='Mateusz Baran',
    author_email='mateusz.baran.sanok@gmail.com',
    maintainer='Mateusz Baran',
    maintainer_email='mateusz.baran.sanok@gmail.com',
    license='MIT',
    url='https://gitlab.com/mateusz.baran/smart-params',
    description='The tool for advanced project configuration with python object injection.',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.8, <4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'PyYAML>=5.4.1',
    ],
    extras_require=dict(
        dev=[
            'bump2version>=1.0.1',
            'black>=21.9b0',
            'pytest>=6.1.2',
            'pytest-cov>=3.0.0',
            'pytest-flake8>=1.0.7',
            'pytest-isort>=2.0.0',
            'pytest-mypy>=0.8.1',
            'types-PyYAML>=5.4.11',
        ],
    ),
)
