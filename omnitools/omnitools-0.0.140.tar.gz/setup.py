from setuptools import setup, find_packages
import json
import os


install_requires = "requirements.txt"
extras_require_fp = "requirements_extra.json"
if os.path.isfile(install_requires):
    install_requires = open(install_requires).read().splitlines()
else:
    install_requires = None
if os.path.isfile(extras_require_fp):
    extras_require = json.loads(open(extras_require_fp).read())
else:
    extras_require = None
setup(
    name="omnitools",
    version="0.0.140",
    keywords=["omnitools python utilities shortcuts misc"],
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
        "Sourcecode": "https://github.com/foxe6/omnitools",
        "Documentation": "https://github.com/foxe6/omnitools/blob/master/test",
        "Example": "https://github.com/foxe6/omnitools/blob/master/omnitools/example",
        "Issues": "https://github.com/foxe6/omnitools/issues",
        "Funding": "https://paypal.me/foxe6",
        "Say Thanks!": "https://saythanks.io/to/foxe6",
    },
    license="AGPL-3.0",
    author="f̣ộx̣ệ6",
    author_email="foxe6@protonmail.com",
    description="Miscellaneous functions written in short forms.",
    long_description=open("README.md", "rb").read().decode(),
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
