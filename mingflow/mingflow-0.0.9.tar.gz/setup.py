from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name='mingflow',
    version='0.0.9',
    description='Just wanna make your ML easier',
    licenes='MIT',
    # packages就是包括的文件夹
    packages=['mingflow'],
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        
    ],
    zip_safe=True,
)
