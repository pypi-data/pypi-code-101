import setuptools
from anonupload.main import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="anonupload",
    version=__version__,
    author="Jak Bin",
    author_email="jakbin4747@gmail.com",
    description="upload and upload to anonfile server",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jakbin/anonfile-upload",
    install_requires=["tqdm"],
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='anonfile,anonfile-api,anonfile-cli,anonymous,upload',
    packages=["anonupload"],
    entry_points={
        "console_scripts":[
            "anon = anonupload.main:main"
        ]
    }
)
