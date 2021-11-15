from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


requires = [
    'pytest',
    'pytest-xdist',
    'pytest-parallel',
    'altwalker',
    'selenium<4.0.0',
]


setup(
    name='pythonbook',
    version='1.0',
    # 除外する場合はfind_packages(exclude=['値'])を使う
    packages=find_packages(),
    author='Taishin',
    author_email='taitasu08035@icloud.com',
    url="https://github.com/taitasu555",
    description="this is sample repo",
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
