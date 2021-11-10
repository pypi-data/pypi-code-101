"""
Copyright (c) [Year] [name of copyright holder]
[Software Name] is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="dataprime",
    version="0.0.4",
    keywords=("dataframe", "pandas"),
    description="数据智脑开源计算引擎dataprime",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="Mulan PSL v2",
    author="APUSIC",
    author_email="464521059@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "amqp>=5.0.6",
        "billiard>=3.6.4.0",
        "cached-property>=1.5.2",
        "celery>=5.1.2",
        "click==8.0.3",
        "click-didyoumean>=0.3.0",
        "click-plugins>=1.1.1",
        "click-repl>=0.2.0",
        "importlib-metadata>=4.8.2",
        "kombu>=5.2.1",
        "numpy>=1.21.3",
        "pandas>=1.3.4",
        "prompt-toolkit>=3.0.22",
        "python-dateutil>=2.8.2",
        "pytz>=2021.3",
        "redis>=3.5.3",
        "six>=1.16.0",
        "typing-extensions>=3.10.0.2",
        "vine>=5.0.0",
        "wcwidth>=0.2.5",
        "zipp>=3.6.0",
    ]
)
