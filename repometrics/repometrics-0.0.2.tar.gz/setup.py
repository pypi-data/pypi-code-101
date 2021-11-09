from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='repometrics',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/alextxj/RepoMetrics',
    license='MIT',
    author='Alex Tian Xing Jian',
    author_email='tian.xingjian@hotmail.com',
    description='CLI to display current repository files path and languages.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pygments'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'repometrics = RepoMetrics.RepoMetrics:main'
        ]
    }
)