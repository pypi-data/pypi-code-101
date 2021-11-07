from setuptools import setup, find_packages

requirements = [l.strip() for l in open('requirements.txt').readlines()]
requirements.append('pytest')

setup(
    name='liveisstracker',
    url='https://gitlab.com/manojm18',
    version='0.0.10',
    author='Manoj Manivannan',
    author_email='manojm18@live.in',
    description='A CLI based on the LiveIssTracker Project from https://gitlab.com/manojm18/liveisstracker',
    packages=find_packages(),
    entry_points={
    'console_scripts': ['liveisstracker=liveisstracker.command_line:main'],
    },
    install_requires=requirements,
    include_package_data=True,
)

