from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.11'
DESCRIPTION = 'Sign Language Recognition tool.'
LONG_DESCRIPTION = 'Sign Language Recognition tool. It works in real time using additionally OpenCV and Mediapipe libraries.'

# Setting up
setup(
    name="SignLanguageRecognition",
    version=VERSION,
    author="Jan Binkowski",
    author_email="<jan.binkowski@wp.pl>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'mediapipe', 'numpy', 'tensorflow'],
    keywords=['python', 'sign language', 'sign language recognition', 'recognition in real time', 'action recognition'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True
)