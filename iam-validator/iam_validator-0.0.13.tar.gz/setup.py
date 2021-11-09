#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import sys
import os
from io import open
from shutil import rmtree



DESCRIPTION = ("Lightweight, extensible schema and IAM validation tool for "
               "AWS Roles.")

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup_requires = (
    ['pytest-runner'] if any(x in sys.argv for x in ('pytest', 'test', 'ptr')) else []
)

"""
Cleanup old terraform files in directory
:return:
"""
paths_to_clean = ['/data_files/terraform', '/data_files/terraform_setup_roles','/data_files/terraform_setup_s3_bucket']
for mypath in paths_to_clean:
    for files in os.listdir(os.getcwd()+mypath):
        files_to_remove = ['.terraform.lock.hcl', 'terraform.tfstate.backup', 'terraform.tfstate','.terraform']

        if files in files_to_remove:
            if os.path.exists(str(os.getcwd()+mypath+'/'+files)):
                print('path exists')
                if os.path.isfile(os.getcwd()+mypath+'/'+files):
                    print('is file')
                    os.remove(os.path.join(os.getcwd()+str(mypath), files))
                else:
                    print('is directory')
                    rmtree(os.path.join(os.getcwd()+str(mypath), files))

setup(
    name='iam_validator',
    version='0.0.13',
    description=DESCRIPTION,
    url='https://github.com/rubelw/iam-validator',
    author='Will Rubel',
    author_email='willrubel@gmail.com',
    license = 'GPLv3+',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=setup_requires,
    tests_require=['pytest','mock'],
    test_suite="iam_validator.tests",
    install_requires=[
        "boto3>=1.4.3",
        "requests>=2.18",
        "Click>=6.7",
        "PyYAML>=3.12",
        "configparser>=3.5.0",
        "pykwalify>=1.6.1",
        "schema>=0.6.8",
        "future>=0.16.0",
        "six>=1.11.0",
        "pip",
        "botocore"
    ],
    keywords=['validation', 'iam', 'scp','aws','python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points="""
        [console_scripts]
        iam-validator=iam_validator.command:cli
    """
)
