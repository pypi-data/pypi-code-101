from setuptools import find_packages, setup

setup(
    name='CQHDimensionalPhenotyper',
    packages=find_packages(include = ['CQHDimensionalPhenotyper']),
    version='0.1.3',
    description='Score EHR based on NIMH RDoC',
    author='Tom McCoy, modified by Daisy Dan',
    author_email = 'sdan@mclean.harvard.edu',
    license='MIT',
    install_requires = ['pytest-runner','pytest == 4.4.1'],
    long_description = 'Modified based on Tom McCoy code to score electronic health records',
    # package_dir = {"": "CQHDimensionalPhenotyper"},
    python_requires = ">=2.7",
)
