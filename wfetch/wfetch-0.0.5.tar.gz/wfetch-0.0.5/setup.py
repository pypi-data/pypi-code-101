import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wfetch",
    version="0.0.5",
    author="zJairO",
    author_email="hello@zjairo.com",
    description="Minimal Windows system information tool written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zJairO/wfetch",
    project_urls={
        "Bug Tracker": "https://github.com/zJairO/wfetch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "wfetch"},
    packages=setuptools.find_packages(where="wfetch"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': ['wfetch=wfetch.wfetch:wfetch'],
    }
)