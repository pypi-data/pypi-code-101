from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.3'
DESCRIPTION = 'Desktop Assistant which takes commands as speech & convert to text. Speaks the text provided. Wishes the User as per the Hour of the day. It also can send E-Mails.'
LONG_DESCRIPTION = 'This Desktop Assistant is complete package for a Virtual Assistant of yours. It can do all basic tasks such as Sending E-Mails, Wishing/Greeting. Taking command in speech from the user. Speak the text provided to it.'

# Setting up
setup(
    name="desktopassistant",
    version=VERSION,
    author="Akshat Bhatter (Developer_Akshat)",
    author_email="<bhatterakshat4@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyttsx3', 'speechRecognition', 'comtypes'],
    keywords=['python', 'AI', 'Desktop Assistant', 'Assistant', 'Virtual Assistant'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)