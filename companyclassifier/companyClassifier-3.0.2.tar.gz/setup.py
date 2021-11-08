# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='companyClassifier',
    version="3.0.2",
    packages=['companyClassifier','companyClassifier.models'],
    package_data={'': ['companyClassifier.models/*.json','companyClassifier.models/*.joblib','companyClassifier.models/*.h5']},
    include_package_data=True,
    install_requires=["wget","keras>=2.6.0","tqdm","joblib","transformers>=4.11.3","numpy>=1.13.3","tensorflow>=2.6.0"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
