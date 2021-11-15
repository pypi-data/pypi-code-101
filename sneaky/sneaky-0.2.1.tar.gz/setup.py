from setuptools import setup, find_packages
import json
import os


readme = "README.md"
install_requires = "requirements.txt"
extras_require = "requirements_extra.json"
if os.path.isfile(readme):
    readme = open(readme).read()
else:
    readme = None
if os.path.isfile(install_requires):
    install_requires = open(install_requires).read().splitlines()
else:
    install_requires = []
if os.path.isfile(extras_require):
    extras_require = json.loads(open(extras_require).read())
else:
    extras_require = {}
setup(
    name="sneaky",
    version="0.2.1",
    keywords=["chromedriver undetected detection antibot prevent avoid recaptcha captcha buster solver bypass audio selenium web bot scraper crawler proxy automation browsermob"],
    packages=find_packages(),
    package_data={
        "": [
            "pkg_data.*",
            "example/*.*",
            "../requirements.txt",
            "../requirements_extra.json",
            "../*.md",
            "../LICENSE",
            "../.gitignore",
        ],
    },
    url="https://github.com/foxe6/",
    project_urls={
        "Sourcecode": "https://github.com/foxe6/sneaky",
        "Documentation": "https://github.com/foxe6/sneaky/blob/master/test",
        "Example": "https://github.com/foxe6/sneaky/blob/master/sneaky/example",
        "Issues": "https://github.com/foxe6/sneaky/issues",
        "Funding": "https://paypal.me/foxe6",
        "Say Thanks!": "https://saythanks.io/to/foxe6",
    },
    license="AGPL-3.0",
    author="f̣ộx̣ệ6",
    author_email="foxe6@protonmail.com",
    description="A sneaky web bot based on Selenium driven by ChromeDriver equipped with undetected-chromedriver (as bot detection bypass), Buster (as a reCAPTCHA solver), ??? (as network traffic monitor), vpncmd (as free VPN rotator) let you breach the Internet as you please.",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Development Status :: 5 - Production/Stable",
    ]
)
